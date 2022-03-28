## Elise Rust
## ANLY 503
## Final Project
## March 2022

## OECD Ratio of Genders in various fields --> global map
## Data: https://stats.oecd.org/Index.aspx?QueryId=109881#

## Load necessary packages
library(ggplot2)
library(tidyverse)
library(maps)
library(viridis)

## Load necessary data
students <- read.csv("Clean_Datasets/OECD_Students.csv")
#test_scores <- read.csv("Clean_Datasets/OECD_Test_Scores_Clean.csv")

## Get polygon data for countries
world <- map_data("world")
ggplot(world_map, aes(x = long, y = lat, group = group)) +
  geom_polygon(fill = "lightgray", colour = "white")

# Remove OECD Average and European Union data for later
averages <- students %>%
  filter(Country == "European Union 22 members in OECD" | Country == "OECD - Average")
students <- students %>%
  filter(Country != "European Union 22 members in OECD") %>%
  filter(Country != "OECD - Average")

## Get list of countries in dataset
list_countries <- students %>%
  select(Country) %>%
  distinct()
list_countries = as.list(list_countries)

## Get list of acceptable region names --> have to align list with map_data accepted names
sort(unique(map_data("world")$region)) 
  
## Recode country names as necessary
students <- students %>%
  ## Recode certain entries
  mutate(Country = recode(str_trim(Country), "United States" = "USA",
                         "United Kingdom" = "UK",
                         "Korea" = "South Korea", # I think
                         "Slovak Republic" = "Slovakia"))

# Join datasets by region
worldSubset <- merge(world, students, by.x = "region", by.y = "Country", all.y = TRUE)

# theme for all maps
world_theme <- theme(
  plot.background = element_blank(),
  panel.background = element_blank(),
  plot.title = element_text(size = 17, family = "Helvetica", face = "bold", hjust = 0.5),
  plot.subtitle = element_text(size = 10, family = "Helvetica", face = "italic", hjust = 0.5),
  axis.title = element_blank(),
  axis.ticks = element_blank(),
  axis.text = element_blank(),
  panel.grid = element_blank(),
  legend.position = "bottom",
  legend.direction = "horizontal",
  legend.title = element_blank(),
  legend.spacing.x = unit(.12, 'cm'),
  plot.caption = element_text(size = 9, family = "Helvetica", face = "italic"),
  plot.margin = margin(1, 0, 0, 0, "cm")
)

## Visualize
worldSubset %>%
  filter(Year == 2017) %>%
  filter(Field == "Arts and humanities") %>%
  ggplot(data = worldSubset, mapping = aes(x = long, y = long, group = group)) +
    geom_polygon(aes(fill = Ratio)) +
  world_theme

