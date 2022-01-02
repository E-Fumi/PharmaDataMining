# Pharmaceutical Compound Data Mining

## Intro

In this project data mining (principal component analysis) is performed on a dataset of over 40,000 bioactive compounds, encompassing information on their structure and chemical properties.

<br/>
<p align="center">
  <img src="./readme_media/phases.gif" width="400" height="360"><br/>
  Projection of compounds by clinical research phase reached
 </p>
<br/>

The data obtained from the [ChEMBL](https://www.ebi.ac.uk/chembl/) database is extensive, but incomplete. Data cleaning and data augmentation are performed, whereby missing values are scraped or estimated through a linear regression model. In the cleaned dataset, each compound has different entries pertaining to its polarity, flexibility, bulkiness, composition, and hydrogen bond donors and acceptors.<br/>

Dimensionality reduction is performed through principal component analysis where the 11-dimensional dataset is transformed to a 4-dimensional dataset maintaining ~85% of the original variation. The resulting data is plotted in 3D (the further dimension being represented through colour), where interesting patterns can be observed.<br/>
<br/>

## Data Cleaning and Augmentation

### Scraping

Text

### LogP Estimation

Text

<br/>
<p align="center">
  <img src="./readme_media/logp.png"><br/>
  Caption
 </p>
<br/>

### Double Bond Equivalents

Text

## Analysis

Text

<br/>
<p align="center">
  <img src="./readme_media/scree_plot.png"><br/>
  Caption
 </p>
<br/>

## Insights

### Clinical Research Phase

Text

<br/>
<p align="center">
  <img src="./readme_media/phases.png"><br/>
  Caption
 </p>
<br/>

<br/>
<p align="center">
  <img src="./readme_media/phases_z.png"><br/>
  Caption
 </p>
<br/>

<br/>
<p align="center">
  <img src="./readme_media/phases_x.png"><br/>
  Caption
 </p>
<br/>

### Target Organ System

Text

<br/>
<p align="center">
  <img src="./readme_media/systems.gif"><br/>
  Caption
 </p>
<br/>

<br/>
<p align="center">
  <img src="./readme_media/nervous_antiinfective.png"><br/>
  Caption
 </p>
<br/>

<br/>
<p align="center">
  <img src="./readme_media/gastric_respiratory.png"><br/>
  Caption
 </p>
<br/>

## Requirements

python 3.x</br>
matplotlib</br>
numpy</br>
pandas</br>
plotly</br>
scikit-learn</br>
selenium</br>
wget</br>
Google Chrome Version 96.0.4664.110<br/>
<br/>
If you do not have it, this last item would need to be installed manually, but it is only necessary if you want to perform the data cleaning youself.<br/>
You do not need it if you use the cleaned datasets provided in the main directory.</br>

## Usage

`git clone https://github.com/E-Fumi/PharmaDataMining.git`</br>
`cd PharmaDataMining`</br>
`pip install -r requirements.txt`</br>
`python main.py`
