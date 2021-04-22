import pandas as pd
import numpy as np
import src.functions_csv as srcsv
import src.functions_scrapping as srcs
import requests
from bs4 import BeautifulSoup


def converttodf():
    """
    Scrapping
    Creating a df with the scrapped data we want to work with.
    Adding columns and orderind the df
    """
    url = 'https://cincodias.elpais.com/mercados/materias-primas/oro/2/'   #The scrapped URL
    html= requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    tabla = soup.find_all("table")[0]   # Is the first and the last table of the url but we check it out.
    date = []
    values = []
    for f in tabla.find_all("tr"):   # List with table rows.
        fila =[e for e in f.find_all("th")]   # Elements within the row.
        if fila :
            day = {"day": fila[0].text}   # Creating a dic with the day.
            date.append(day)   # Appending the data to the list.
    date.pop(0)   # Deleting the first row to be able to merge it. Contains "Fecha" as first value

    for f in tabla.find_all("tr"):   # List with table rows.
        fila =[e for e in f.find_all("td")]   # Elements within the row.
        if fila:
            value = (fila[0].text)   # Creating a list with the price.
            values.append(value)   # Appending the data to the list.
    
    dfs = pd.DataFrame(date)   # Creating a df with the date
    dfs["price"] = values   # Creating a new column with the price 
    dfs["price"] = dfs.price.apply(srcs.convertir_valor)   # Converting price column from string to float
    dfs=dfs.assign(currency="$")   # Creating a new column with the currency of the prices of the df
    dfs = dfs.drop_duplicates()   # Deliting the dublicate rows (first)

    dfs["year"] = dfs["day"].apply(srcs.year)   # Adding a new column for the years of the Date column
    dfs["month"] = dfs["day"].apply(srcs.month)   # Adding a new column for the months of the Date column
    dfs["day"] = dfs["day"].apply(srcs.day)   # Adding a new column for the years of the Date column
    dfs = dfs[['year','month','day','price','currency']]   # Ordering my df
    dfs = dfs.sort_index(ascending=False)   # Reorganizing the df to merge it later with the dfh
    return dfs