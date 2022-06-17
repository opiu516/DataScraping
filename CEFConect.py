import requests
import time
from bs4 import BeautifulSoup
import math
import pandas as pd 
from pathlib import Path
import lxml


cefs = []

table = []
table.append(["Cef Ticker", "Current price" ,"52 Wk Avg price", "52 Wk High price","52 Wk Low price","Current Nav" ,"52 Wk Avg Nav", "52 Wk High Nav","52 Wk Low Nav","Current P/D" ,"52 Wk Avg P/D", "52 Wk High P/D","52 Wk Low P/D"])

def getCefs():
    f = open("cefList.txt", "r")
    for x in f:
        cefs.append(x[:-1])
    f.close
    #print(cefs)

getCefs()

def getInfo(cef):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    adres = "https://www.cefconnect.com/fund/" + cef
    #print(adres)
    response = requests.get(adres, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'})
    responseContent = response.text
    #print(responseContent)
    soup = BeautifulSoup(responseContent, features = "lxml" )
    #print(soup.prettify())
    #if soup.find_all("title").
    info = soup.find_all('td',class_ = "right-align")
    if len(info) == 0:
        return
    values = []
    for i in info:
        values.append(i.get_text().strip())
    table.append([cef,values[0],values[3],values[6],values[9],values[1],values[4],values[7],values[10],values[2],values[5],values[8],values[11]])
    print(cef + " done!")
    
for i in cefs:
    getInfo(i)
pd.DataFrame(table).to_csv(str(Path.cwd())+ "/" + "CefDatabank" + ".csv")
