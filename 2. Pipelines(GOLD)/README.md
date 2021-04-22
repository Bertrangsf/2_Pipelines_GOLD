![portada](https://es.fxmag.com/images/cache/article_header_filter/images/articles/explicando-el-precio-del-oro-con-la-inflacion.jpg)

# Project: Data Pipeline

## Overview

Gold, like other commodities, varies in price on a daily basis even though it is one of the safest values. So, in this project I have downloaded a database of historical gold prices (from 1950 to 2020) and merge it with the data scanned from a website that updates daily the price of gold. After having inserted the file in the executable folder when turning on the computer, the dataframe will be updated with the new gold price, creating little by little my own database. 

## Table of Contents
1. [General Info](#general-info)
2. [Data treatment](#Data-treatment)
3. [Libraries](#Libraries)
4. [Technology](#Technology)
5. [Methodology](#Methodology)

## General Info

In this analysis we try to generate a df with the gold price uptate. I've download the csv from Kaggle https://www.kaggle.com/tunguz/gold-prices, and I scrapp the data from https://cincodias.elpais.com/mercados/materias-primas/oro/2/

## Data treatment

The realization of the project is divided into up to 3 parts: 

1. Cleaning of the dataset.csv. (Analysis)
2. Scrapping the price by day and cleaning of the dataset. (Analysis)
3. Merging booth and daily update of the df. (Analysis)
4. Visualization

## Libraries

```
### DataFrames:
pandas 
numpy 
functions_csv.py
functions_scrapping.py
functions_scrap_final.py
requests
from bs4 BeautifulSoup

### Visualization:
pandas
numpy
seaborn
matplotlib.pyplot
plotly.express
```
## Technology: 

A list of technologies used within the project:

1. [Jupyter Notebook](https://jupyter.org/) : Version 6.1.4
2. [Python](https://www.python.org/): Version 3.8
3. [Visual Studio Code](https://code.visualstudio.com/)

## Methodology: 

The realization of the project is divided into up to 3 parts: 

1. Preliminary cleaning of the dataset. 

* Import the csv from the files.
* - Adding columns (year, month, day, currency)

2. Scrapping. 

* Requesting to the URL the data from the table.
* - Coverting the price into float.
* - Adding columns (year, month, day, currency).
* - Deleting the duplicate info.
* - Import the df from the csv and concatenating it with the df obtained by scrapping.

3. Final df

* Importing the concatenated df and applying the function to add the new result of that day.
* - Deleting the duplicate info.

4. Vizualization

* Plt of the historical gold prices (1970-2020)
* Plt of the actual gold prices (2021 - actual)

## Author

* **Bertrán Gil de Santivañes Finat** - *Initial work* - (https://github.com/Bertrangsf/2.-Pipelines-GOLD)
