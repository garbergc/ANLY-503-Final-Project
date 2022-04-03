#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 12:21:59 2022

@author: eliserust
"""

## Load necessary packages
import plotly
import pandas as pd
#from plotly import express
import plotly.graph_objs as go
import plotly.express as px


## Data
students = pd.read_csv("Clean_Datasets/OECD_Students.csv")
codes = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')
df = px.data.gapminder().query("year==2007")

# Tutorial: https://plotly.com/python/choropleth-maps/
    
fig = go.Figure(data=go.Choropleth(
    locations = students['COUNTRY'],
    z = students['Ratio'],
    text = students['Country'],
    colorscale = 'Blues',
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_tickprefix = '$',
    colorbar_title = 'Male to Female Ratio of Sector Employment',
))

fig.update_layout(
    title_text='Gender Gap in STEM',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    annotations = [dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
        text='Source: <a href="https://www.cia.gov/library/publications/the-world-factbook/fields/2195.html">\
            CIA World Factbook</a>',
        showarrow = False
    )]
)

fig.show()
