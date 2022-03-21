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
students = pd.read_csv("OECD_StudentsByGenderField.csv")


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
                                          'MOBILITY', 'EDUCATION_FIELD', 'YEAR', 
                                          'Flag Codes', 'Flags'])

# 3. Remove rows with NAs for "Value"


# 4. Fix incorrect values