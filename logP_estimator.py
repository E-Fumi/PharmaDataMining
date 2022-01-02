import pandas as pd
import os
from sklearn.linear_model import LinearRegression


def train_linear_regressor():
    df = pd.read_csv(os.path.join('chem_datasets', 'all_chems', '0.csv'), delimiter=';', low_memory=False)
    df = df[['Heavy Atoms', 'AlogP', 'Polar Surface Area']]                                  # Select pertinent columns
    df = df.dropna()                                                                         # Drop NaN containing rows
    df = df[~df.eq('None').any(1)]                                                        # Remove None containing rows
    df = df.astype(float)                                                          # Convert all values to float values
    df = df[df['Polar Surface Area'] != 0.]                                           # Drop all rows w/ polar area = 0

    df['Polar A / Heavy Atom Ratio'] = df.apply(lambda x: x['Polar Surface Area'] / x['Heavy Atoms'], axis=1)
    df = df.drop(columns=['Heavy Atoms', 'Polar Surface Area'])
    df = df[df['Polar A / Heavy Atom Ratio'] < 15]

    X = df.iloc[:, 1].values.reshape(-1, 1)                                        # converts values into a numpy array
    Y = df.iloc[:, 0].values.reshape(-1, 1)          # -1 means that calculate the dimension of rows, but have 1 column
    linear_regressor = LinearRegression()                                                 # create object for the class
    linear_regressor.fit(X, Y)                                                              # perform linear regression
    return linear_regressor
