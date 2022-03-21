#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:30:08 2022

@author: eliserust

Munging for OECD Students by Field - by Gender
Data Source: https://stats.oecd.org/Index.aspx?QueryId=109881
"""

## Load in necessary packages
import pandas as pd


## Load in necessary data
students = pd.read_csv("Raw_Datasets/OECD_StudentsByGenderField.csv")


## MUNGING
# 1. Examine data + columns
students.head()
for col in students.columns:
    print(col)

# Summary statistics
students.describe()

# 2. Remove unnecessary columns before further cleaning
students_clean = students.drop(columns = ['COUNTRY', 'INDICATOR', 'Indicator',
                                          'EDUCATION_LEV', 'Education level', 'SEX',
                                          'MOBILITY', 'Mobility status','EDUCATION_FIELD', 
                                          'YEAR', 'Flag Codes', 'Flags'])
print(students_clean)


# 3. Fix incorrect values
students_clean = students_clean[students_clean['Year'] != "Latest available year"] 

# 4. Count NAs across the whole dataframe
students_clean.isna().sum() # 4,585 NAs in column "Value" --> these are useless to us

# Remove rows with NAs for "Value"
students_clean = students_clean[students_clean['Value'].notna()]


# Write to csv
students_clean.to_csv('Clean_Datasets/OECD_Students.csv', index=False)

