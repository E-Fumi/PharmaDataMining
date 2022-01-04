import pandas as pd
import double_bond_equivalents
import utils
import webcrawler
import logP_estimator
import numpy as np
import os
import sys
import wget


def clean_data(system_specific):
    file_nrs, origin_path, destination_path = return_files_and_paths(system_specific)
    if os.path.exists(destination_path):
        pass
    else:
        cleaned_dataset = pd.DataFrame()
        download_dataset()
        regressor = logP_estimator.train_linear_regressor()
        for dataframe_nr in range(file_nrs):
            df = clean_dataframe(origin_path, dataframe_nr, system_specific, regressor)
            cleaned_dataset = cleaned_dataset.append(df)
        cleaned_dataset.to_csv(destination_path, index=False, sep=';')
    return destination_path


def return_files_and_paths(system_specific):
    if system_specific:
        return 13, os.path.join('chem_datasets', 'by_system'), os.path.join('cleaned_df_by_system.csv')
    else:
        return 1, os.path.join('chem_datasets', 'all_chems'), os.path.join('cleaned_df_all_chems.csv')


def download_dataset():
    path = os.path.join('chem_datasets', 'all_chems', '0.csv')
    if os.path.exists(path):
        pass
    else:
        def progress_bar(current, total, width=80):
            progress_message = "Downloading Dataset: %d%% [%d / %d] bytes" % (current / total * 100, current, total)
            sys.stdout.write("\r" + progress_message)
            sys.stdout.flush()
        os.makedirs(os.path.join('chem_datasets', 'all_chems'))
        wget.download('https://zenodo.org/record/5813781/files/0.csv?download=1', out=path, bar=progress_bar)


def clean_dataframe(origin_path, dataframe_nr, system_specific, regressor):
    df = init_dataframe(origin_path, dataframe_nr)
    df = find_missing_data(df)
    df = fix_charges(df)
    df['AlogP'] = df.apply(estimate_logp, regressor=regressor, axis=1)
    if system_specific:
        df['target system'] = utils.Systems[dataframe_nr]
    df = df.dropna()
    df['double bond equivalents'] = df.apply(double_bond_equivalents.find_from_formula, axis=1)
    return df


def init_dataframe(path, file):
    df = pd.read_csv(os.path.join(path, f'{file}.csv'), delimiter=';', low_memory=False)
    df = df[utils.selection]
    df = df.replace('None', float('NaN'))
    df = df.dropna(subset=['Name'])
    df[utils.numeric_columns] = df[utils.numeric_columns].apply(pd.to_numeric)
    return df.rename(utils.renaming_dict, axis=1)


def find_missing_data(df):
    gappy_rows = df.isna().any(1)
    gappy_rows = gappy_rows[gappy_rows.eq(True)]
    for gappy_row in range(gappy_rows.shape[0]):
        index = gappy_rows.index[gappy_row]
        compound_details = [df.loc[index, 'Name'], df.loc[index, 'Molecular Formula']]
        scraped_properties = webcrawler.find_missing_values(compound_details)
        df = update_properties(df, index, scraped_properties)
    return df


def update_properties(df, index, scraped_properties):
    if not scraped_properties['retrieval_failure']:
        del scraped_properties['retrieval_failure']
        for chem_property in scraped_properties:
            if pd.isnull(df.loc[index, chem_property]):
                df.loc[index, chem_property] = scraped_properties[chem_property]
    return df


def fix_charges(df):
    df['positive charge'] = df.apply(determine_positive_charge, axis=1)
    df['negative charge'] = df.apply(determine_negative_charge, axis=1)
    return df.drop(columns=['Molecular Species'])


def determine_positive_charge(x):
    if x['Molecular Species'] == 'BASE' or x['Molecular Species'] == 'ZWITTERION':
        return True
    else:
        return isinstance(x['Molecular Formula'], str) and x['Molecular Formula'][-1] == '+'


def determine_negative_charge(x):
    if x['Molecular Species'] == 'ACID' or x['Molecular Species'] == 'ZWITTERION':
        return True
    else:
        return isinstance(x['Molecular Formula'], str) and x['Molecular Formula'][-1] == '-'


def estimate_logp(x, regressor):
    area_viable = pd.notna(x['Topological Polar Surface Area'])
    count_viable = pd.notna(x['Heavy Atom Count'])
    logp_viable = pd.notna(x['AlogP'])
    if logp_viable:
        return x['AlogP']
    elif not area_viable and not count_viable:
        return float('NaN')
    elif x['Inorganic Flag'] == 1 and area_viable and x['Topological Polar Surface Area'] < 10:
        return -1
    elif area_viable and count_viable:
        ratio = np.array(x['Topological Polar Surface Area'] / x['Heavy Atom Count'])
        estimated_logp = regressor.predict(ratio.reshape(1, -1))
        return float(estimated_logp)
    else:
        return float('NaN')
