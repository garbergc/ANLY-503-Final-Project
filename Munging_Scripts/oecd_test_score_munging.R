## Install/load all necessary libraries 
library(tidyverse)
library(tidyr)
library(styler)
library(dplyr)
library(data.table)

## Read in all data files 
math <- read.csv('OECD_MathScores.csv')
reading <- read.csv('OECD_ReadingScores.csv')
science <- read.csv('OECD_ScienceScores.csv')

## View individual data sets 
head(math)
head(reading)
head(science)

## Combine all three data sets  
all_subject <- rbind(math,reading,science)

## Understand the number of rows and columns 
nrow(all_subject)
ncol(all_subject)

## Remove all columns/variables not needed using index number 
all_subject <- all_subject[-c(4,5,8)]

## Count missing values for each variable
## No missing values 
sapply(all_subject, function(x) sum(is.na(x)))

## Look at all data types
## All types are correct 
str(all_subject)

## View the distribution of numeric variables to detect ouliers
## No unreasonable or unexpected values 
boxplot(all_subject$Value, main="Value Distribution")

## Convert all column names to lowercase 
names(all_subject) <- tolower(names(all_subject))

## Trim indicator values to only show the subject
all_subject$indicator = substring(all_subject$indicator, 5)

## Rename columns to better represent the meaning of values 
names(all_subject)[names(all_subject) == 'subject'] <- 'gender'
names(all_subject)[names(all_subject) == 'location'] <- 'country_code'
names(all_subject)[names(all_subject) == 'value'] <- 'test_score'
names(all_subject)[names(all_subject) == 'indicator'] <- 'subject'
names(all_subject)[names(all_subject) == 'time'] <- 'year'

## Convert values to lowercase to better display on visualizations 
all_subject$gender = tolower(all_subject$gender)
all_subject$subject = tolower(all_subject$subject)

## Check unique values in categorical columns
## All values look acceptable 
## Note: total value (tot) is left in the data set for visualization purposes 
unique(all_subject[c("subject")])
unique(all_subject[c("gender")])
unique(all_subject[c("country_code")])

## Check for duplicates 
## No duplicate rows as the count is one for all rows
setDT(all_subject)[,list(Count=.N),names(all_subject)]

## View final data frame 
head(all_subject)

## Write data frame to csv file 
write_csv(all_subject, "/Users/kajaltiwary/ANLY-503-Final-Project/Clean_Datasets/OECD_Test_Scores_Clean.csv")

