# Pharmaceutical Compound Data Mining

## Intro

In this project, data mining (principal component analysis) is performed on a dataset of over 40,000 bioactive compounds, encompassing information on their structure and chemical properties.

<br/>
<p align="center">
  <img src="./readme_media/phases.gif" width="400" height="360"><br/>
  Projection of compounds color coded<br/>
  by clinical research phase reached
 </p>
<br/>

The data obtained from the [ChEMBL](https://www.ebi.ac.uk/chembl/) database is extensive, but incomplete. Data cleaning and data augmentation are performed, whereby missing values are scraped or estimated through a linear regression model, and double bond equivalents are calculated for each molecule. In the cleaned dataset, each compound has different entries pertaining to its polarity, flexibility, bulkiness, composition, and hydrogen bond donors and acceptors.<br/>

Dimensionality reduction is performed through principal component analysis where the 10-dimensional dataset is transformed to a 4-dimensional dataset maintaining ~85% of the original variation. The resulting data is plotted in 3D (the further dimension being represented through colour), where interesting patterns can be observed.<br/>

If you would like to run the code and take a look at the 3D plots yourself, you can do so by following the instructions in the Usage section.<br/>
<br/>

## Data Cleaning and Augmentation

### Scraping

Text

### LogP Estimation

Text

<br/>
<p align="center">
  <img src="./readme_media/logp.png" width="400"><br/>
  Caption
 </p>
<br/>

### Double Bond Equivalents

Text

## Analysis

Text

<br/>
<p align="center">
  <img src="./readme_media/scree_plot.png" width="400"><br/>
  Caption
 </p>
<br/>

## Insights

### Clinical Research Phase

In the figure below, one can see the >40,000 pharmaceutical compounds projected along the three principal component dimensions, color coded by which clinical phase they reached. Each point is transparent (alpha = 20%) to limit how much data points crowd each other out in the visual representation.<br/>

<br/>
<p align="center">
  <img src="./readme_media/phases.png" width="650"><br/>
  Caption
 </p>
<br/>

<br/>
<p align="center">
  <img src="./readme_media/phases_z.png" width="650"><br/>
  Caption
 </p>
<br/>

<br/>
<p align="center">
  <img src="./readme_media/phases_x.png" width="650"><br/>
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
If you do not have it, this last item would need to be installed manually, but it is only necessary if you want to perform the data cleaning youself. You do not need it if you use the cleaned datasets provided in the main directory.</br>

## Usage

`git clone https://github.com/E-Fumi/PharmaDataMining.git`</br>
`cd PharmaDataMining`</br>
`pip install -r requirements.txt`</br>
`python main.py`</br>
</br>
There are two boolean variables in main.py that can be changed to alter the datasets, and presentation.</br>
Should you wish to run the data cleaning scripts yourself, you can do so by renaming the csv files in the main directory.
