#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 20:39:31 2022

@author: claregarberg
"""

# final project: kaggle data munging

# importing necessary libraries
import pandas as pd
import numpy as np
import os

os.chdir("/Users/claregarberg/Documents/Graduate School/Spring 2022 Semester/503 Data Visualization/Final Project/ANLY-503-Final-Project")

# checking the working directory
path = os.getcwd()
path

kaggle = pd.read_csv("Raw_Datasets/Kaggle_WomenInDataScience/multipleChoiceResponses.csv", dtype = {"Q8": "str"})

# now let's take a look at the data
kaggle.head()
kaggle.columns

# for data viz purposes let's only keep Q16 and other relevant variables
tokeep = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", 
          "Q16_Part_1", "Q16_Part_2", "Q16_Part_3", "Q16_Part_4", 
          "Q16_Part_5", "Q16_Part_6", "Q16_Part_7", "Q16_Part_8", "Q16_Part_9", "Q16_Part_10", 
          "Q16_Part_11", "Q16_Part_12", "Q16_Part_13", "Q16_Part_14", "Q16_Part_15", "Q16_Part_16", 
          "Q16_Part_17", "Q16_Part_18"]

kaggle = kaggle[tokeep]

# changing to more descriptive col names
newname = ["gender", "age", "country", "education", "undergrad_major", "professional_title", 
           "professional_industry", "experience_years", "compensation_usd", 
          "Q16_Part_1", "Q16_Part_2", "Q16_Part_3", "Q16_Part_4", 
          "Q16_Part_5", "Q16_Part_6", "Q16_Part_7", "Q16_Part_8", "Q16_Part_9", "Q16_Part_10", 
          "Q16_Part_11", "Q16_Part_12", "Q16_Part_13", "Q16_Part_14", "Q16_Part_15", "Q16_Part_16", 
          "Q16_Part_17", "Q16_Part_18"]

namingdict = dict(zip(tokeep, newname))

kaggle = kaggle.rename(columns=namingdict)

# it's clear that this data is in wide format, it must be in long format to be tidy
kaggle_tidy = pd.melt(kaggle, id_vars=["gender", "age", "country", "education", "undergrad_major", 
                                       "professional_title", "professional_industry", "experience_years", 
                                       "compensation_usd"], 
                     var_name = "q16", value_name="programming_skill")
kaggle_tidy.head()

# dropping first row
kaggle_tidy = kaggle_tidy.drop(labels=0, axis=0)

# dropping q16 var
kaggle_tidy = kaggle_tidy.drop(labels="q16", axis=1)

kaggle_tidy.head()

# now we need to summarize by gender and count of skill
kaggle_agg = kaggle_tidy.groupby(['gender', 'programming_skill'])['programming_skill'].size().reset_index(name = "counts")

# total gender counts of those answering this Q
gender_counts = kaggle_agg.groupby(['gender'])['counts'].sum().reset_index(name = "counts")

# getting ratios as well
kaggle_agg["ratio"] = None

for index in kaggle_agg.index:
    if kaggle_agg["gender"][index] == "Male":
        kaggle_agg["ratio"][index] = kaggle_agg["counts"][index]/gender_counts.loc[gender_counts['gender'] == "Male", 'counts'].iloc[0]
    elif kaggle_agg["gender"][index] == "Female":
        kaggle_agg["ratio"][index] = kaggle_agg["counts"][index]/gender_counts.loc[gender_counts['gender'] == "Female", 'counts'].iloc[0]
    else:
        continue


# for viz purposes let's only look at those who self identify as male or female
kaggle_agg = kaggle_agg[(kaggle_agg.gender == "Male") | (kaggle_agg.gender == "Female")]

# checking... ratios should sum to 1
kaggle_agg.groupby(['gender'])['ratio'].sum().reset_index(name = "sum") # looks good!

# now we have an aggregation ready for visualization 

# saving to a csv
kaggle_agg.to_csv("Clean_Datasets/Kaggle_WomenInDataScience_viz.csv", index=False)































