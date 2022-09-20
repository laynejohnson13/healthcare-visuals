###Loading in packages

import pandas as pd
import numpy as np
print('cell successfully ran')

import seaborn as sns
import matplotlib.pyplot as plt
import plotly

sns.set_theme(style='whitegrid')
print('cell successfully ran')


###Loading in data
dataframe = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_Microcourse_Visualization/main/Data/Georgia_COVID/Georgia_COVID-19_Case_Data.csv')

dataframe

len(dataframe)

dataframe.shape

###Describing the variables
dataframe.info()

list(dataframe)

dataframe['COUNTY'].value_counts()

dataframe_counties = dataframe['COUNTY'].value_counts()
dataframe_counties.head(20)

###Transforming columns
dataframe['DATESTAMP']

dataframe['DATESTAMP_MOD'] = dataframe['DATESTAMP']
print(dataframe['DATESTAMP_MOD'].head(10))
print(dataframe['DATESTAMP_MOD'].dtypes)

dataframe

dataframe['DATESTAMP_MOD'] = pd.to_datetime(dataframe['DATESTAMP_MOD'])
dataframe['DATESTAMP_MOD'].dtypes

dataframe[['DATESTAMP', 'DATESTAMP_MOD']]

dataframe['DATESTAMP_MOD_DAY'] = dataframe['DATESTAMP_MOD'].dt.date
dataframe['DATESTAMP_MOD_DAY']

dataframe['DATESTAMP_MOD_YEAR'] = dataframe['DATESTAMP_MOD'].dt.year
dataframe['DATESTAMP_MOD_MONTH'] = dataframe['DATESTAMP_MOD'].dt.month

dataframe['DATESTAMP_MOD_YEAR']
dataframe['DATESTAMP_MOD_MONTH'] 

dataframe

dataframe['DATESTAMP_MOD_MONTH_YEAR'] = dataframe['DATESTAMP_MOD'].dt.to_period('M')
dataframe['DATESTAMP_MOD_MONTH_YEAR'].sort_values()

dataframe['DATESTAMP_MOD_WEEK'] = dataframe['DATESTAMP_MOD'].dt.week
dataframe['DATESTAMP_MOD_WEEK']

dataframe['DATESTAMP_MOD_QUARTER'] = dataframe['DATESTAMP_MOD'].dt.to_period('Q')
dataframe['DATESTAMP_MOD_QUARTER'].sort_values()

dataframe['DATESTAMP_MOD_DAY_STRING'] = dataframe['DATESTAMP_MOD_DAY'].astype(str)
dataframe['DATESTAMP_MOD_WEEK_STRING'] = dataframe['DATESTAMP_MOD_WEEK'].astype(str)


###Getting the counties required for analysis
##Counties we want to analyze:
    #Cobb
    #DeKalb
    #Fulton
    #Gwinnett
    #Hall

dataframe['COUNTY']

countList = ['COBB', 'DEKALB', 'FULTON', 'GWUINNETT', 'HALL']
countList

selectCounties = dataframe['COUNTY'].isin(countList)
len(selectCounties)

###Getting the specific date/timestamp you want

selectcountytime = selectCounties