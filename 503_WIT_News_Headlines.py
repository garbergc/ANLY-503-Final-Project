"""
Created on Sat Nov  6 12:10:55 2021
@author: kajaltiwary
"""
import requests
import re 
import pandas as pd
from pandas import DataFrame
from sklearn import datasets
from sklearn import tree
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


topics=["women in STEM", "gender equality", "gender inequality", "women in tech", "gender pay gap"]


filename="NewHeadlines_2022_02_13_v2.csv"


MyFILE=open(filename,"w")
WriteThis="Topic,Date,Source,Headline,Content\n"
MyFILE.write(WriteThis)
MyFILE.close()

End="https://newsapi.org/v2/everything"

for topic in topics: 

## Build a dictionary object for the URL post 
    URLPost = {'apiKey':'6843ef1035cf4e17a7d60be812f1b18d',
                    'q': topic, }

    response1=requests.get(End, URLPost)
    print(response1)
    jsontxt = response1.json()
    print(jsontxt)


    MyFILE=open(filename, "a")
    LABEL=topic

    for items in jsontxt["articles"]:
        print(items, "\n\n\n")
    
        Source=items["source"]["id"]
        print(Source)
    
        Date=items["publishedAt"]
        NewDate=Date.split("T")
        Date=NewDate[0]
        print(Date)
    
    ## CLEAN the Title
        Title=items["title"]
        Title=re.sub(r'[,.;@#?!&$\-\']+', ' ', Title, flags=re.IGNORECASE)
        Title=re.sub(' +', ' ', Title, flags=re.IGNORECASE)
        Title=re.sub(r'\"', ' ', Title, flags=re.IGNORECASE)
    
        Title=re.sub(r'[^a-zA-Z]', " ", Title, flags=re.VERBOSE)
        Title=Title.replace(',', '')
        Title=' '.join(Title.split())
        Title=re.sub("\n|\r", "", Title)
    
        Description=items["content"]
        Description=re.sub(r'[,.;@#?!&$\-\']+', ' ', Description, flags=re.IGNORECASE)
        Description=re.sub(' +', ' ', Description, flags=re.IGNORECASE)
        Description=re.sub(r'\"', ' ', Description, flags=re.IGNORECASE)
        Description=re.sub(r'[^a-zA-Z]', " ", Description, flags=re.VERBOSE)

        Description=Description.replace(',', '')
        Description=' '.join(Description.split())
        Description=re.sub("\n|\r", "", Description)
    
        Description = ' '.join([wd for wd in Description.split() if len(wd)>3])
    
        print(Title)
        print(Description)
    
        WriteThis= str(LABEL)+ "," +str(Date)+ "," +str(Source)+ "," + str(Title) + "," + str(Description) + "\n"
        MyFILE.write(WriteThis)
    
## CLOSE THE FILE
MyFILE.close()

