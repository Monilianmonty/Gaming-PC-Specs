from bs4 import BeautifulSoup
import requests
import csv
import time
import random
import pandas as pd
from tabulate import tabulate

class prebuilt:     #classes for prebuilt
    def __init__(self, name, link, picLink):
        self.link = link
        self.name = name
        self.picLink = picLink

def main():
    linkCount = 0
    URL = "https://www.newegg.com/Gaming-Desktops/SubCategory/ID-3742"
    r = requests.get(URL) #getting all of the url
    soup = BeautifulSoup(r.content, "html.parser")  #parses html data into readable info
    


    contents = []

    for item in soup.find_all('div',attrs = {'class':['item-container']}):      #the class for item container which has the 
        link = item.a["href"]   
        name = item.a.img["alt"]         
        picLink = item.a.img["src"]
        contents.append(prebuilt(name, link, picLink)) #appen adds class to contents
        
    for pc in contents:     #loop through every element in array contents
        time.sleep(random.random()*8)
        r = requests.get(pc.link)
        soup = BeautifulSoup(r.content, "html.parser")     
        table = soup.find_all("table",attrs = {'class':['table-horizontal']})
        df = pd.read_html(str(table))[0:15]
        print(tabulate(df, headers='keys', tablefmt='psql'))



if __name__ == "__main__":
    main() 