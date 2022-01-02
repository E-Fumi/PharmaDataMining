from sklearn import preprocessing
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import utils
import plotly.express as px

labels = [f'PC {x}' for x in range(1, len(utils.pca_columns) + 1)]


def run(path):
    data = pd.read_csv(path, delimiter=';')
    pca_outputs = {}
    pca_data = data[utils.pca_columns]
    scaled_data = preprocessing.scale(pca_data)
    pca = PCA()
    pca.fit(scaled_data)
    transformed_data = pca.transform(scaled_data)
    df = pd.DataFrame(transformed_data, columns=labels)
    df = pd.concat([df, data['Max Phase']], axis=1)
    if 'target system' in data.columns:
        df = pd.concat([df, data['target system']], axis=1)
    pca_outputs['transformed_data'] = df
    pca_outputs['explained_variance'] = np.round(pca.explained_variance_ratio_ * 100, decimals=1)
    pca_outputs['loadings'] = pd.DataFrame(pca.components_.T, columns=labels, index=pca_data.columns)
    return pca_outputs


# print(loadings[['PC 1', 'PC 2', 'PC 3']])
def scree_plot(pca_outputs):
    var = pca_outputs['explained_variance']
    plt.bar(x=range(1, len(var) + 1), height=var, tick_label=labels, color='midnightblue')
    plt.ylabel('Percentage of Explained Variance')
    plt.xlabel('Principal Component')
    plt.title('Scree Plot')
    plt.show()


def plot_loadings(pca_outputs):
    pass


def scatter_plot(pca_outputs, phase_selection):
    df = pca_outputs['transformed_data']
    df = df.drop(columns=labels[3:])
    if phase_selection:
        df = df[df['Max Phase'] > 2]
    if 'target system' not in df.columns:
        df = df.sort_values(by=['Max Phase'])
        df['Max Phase'] = df['Max Phase'].astype(str)
    fig = px.scatter_3d(df, x='PC 1', y='PC 2', z='PC 3',
                        color=return_color_determinant(df),
                        color_discrete_sequence=return_color_scheme(df))
    fig = adjust_fig(fig, df)
    fig.show()


def return_color_determinant(df):
    if 'target system' in df.columns:
        return 'target system'
    else:
        return 'Max Phase'


def return_color_scheme(df):
    phase_colors = utils.colors_by_phase
    if df['Max Phase'].nunique() == 2:
        phase_colors = [phase_colors[0], phase_colors[-1]]
    if 'target system' in df.columns:
        return utils.colors_by_system
    else:
        return phase_colors


def adjust_fig(fig, df):
    if 'target system' not in df.columns:
        fig.update_traces(marker={'size': 3})
        fig.update_traces(marker={'opacity': 0.2})
    else:
        fig.update_traces(marker={'opacity': 0.5})
    return fig
