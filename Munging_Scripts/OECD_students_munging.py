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
import numpy as np


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
students_clean = students.drop(
    columns=[
        "INDICATOR",
        "Indicator",
        "EDUCATION_LEV",
        "Education level",
        "SEX",
        "MOBILITY",
        "Mobility status",
        "EDUCATION_FIELD",
        "YEAR",
        "Flag Codes",
        "Flags",
    ]
)
print(students_clean)


# 3. Fix incorrect values
students_clean = students_clean[students_clean["Year"] != "Latest available year"]

# 4. Count NAs across the whole dataframe
students_clean.isna().sum()  # 4,585 NAs in column "Value" --> these are useless to us

# Remove rows with NAs for "Value"
students_clean = students_clean[students_clean["Value"].notna()]

# Filter out EU and OECD totals later

# 5. Spread
students_wide = students_clean.pivot(
    index=["COUNTRY", "Country", "Year", "Field"], columns="Gender", values="Value"
)

# Make indices into columns
students_wide = students_wide.reset_index(level=["COUNTRY", "Country", "Year", "Field"])

# 5. Feature generation
## Add column "Ratio" for the ratio of male to female entrants in each field (by year and country)
students_wide["Ratio"] = students_wide["Male"] / students_wide["Female"]
students_wide["Ratio"] = students_wide["Ratio"].replace(["inf"], 0)

## Add column "Difference" for the percentage points higher men are than women
students_wide["Difference"] = students_wide["Male"] - students_wide["Female"]

## Add column "STEM_Status" to indicate whether the field is a stem or non-stem field
students_wide["STEM_Status"] = np.select(
    [
        students_wide["Field"].isin(
            [
                "Agriculture, forestry, fisheries and veterinary",
                "Engineering, manufacturing and construction",
                "Health and welfare",
                "Information and Communication Technologies (ICTs)",
                "Natural sciences, mathematics and statistics",
            ]
        ),
        students_wide["Field"].isin(
            [
                "Arts and humanities",
                "Business, administration and law",
                "Education",
                "Generic programmes and qualifications",
                "Services",
                "Social sciences, journalism and information",
            ]
        ),
    ],
    ["STEM", "Non-STEM"],
    default=" ",
)

## Now gather back 
students_long = students_wide.melt(id_vars = ['COUNTRY', 'Country', 'Year', 'Field', 'STEM_Status'], 
                                   value_vars = ['Total', 'Female', 'Male', 'Ratio'], var_name = 'Type')

# Write to csv
students_wide.to_csv("Clean_Datasets/OECD_Students.csv", index=False)
