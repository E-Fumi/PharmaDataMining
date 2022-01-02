# Pharmaceutical Compound Data Mining

## Intro

In this project data mining (principal component analysis) is performed on a dataset of over 40,000 bioactive compounds, encompassing information on their structure and chemical properties.

<br/>
<p align="center">
  <img src="./readme_media/phases.gif" width="400" height="360"><br/>
  Projection of structure and properties by clinical research phase reached.
 </p>
<br/>

The data obtained from the [ChEMBL](https://www.ebi.ac.uk/chembl/) database is extensive, but incomplete. Data cleaning and data augmentation are performed, whereby missing values are scraped or estimated through a linear regression model. In the cleaned dataset, each compound has different entries pertaining to its polarity, flexibility, bulkiness, composition, and hydrogen bond donors and acceptors.<br/>

Dimensionality reduction is performed through principal component analysis where the 11-dimensional dataset is transformed to a 4-dimensional dataset maintaining ~85% of the original variation. The resulting data is plotted in 3D (the further dimension being represented through colour), where interesting patterns can be observed.<br/>

## Data Cleaning and Augmentation

### Scraping

### LogP Estimation

### Double Bond Equivalents

## Analysis

## Insights

### Clinical Research Phase

### Target Organ System

## Requirements

## Usage
