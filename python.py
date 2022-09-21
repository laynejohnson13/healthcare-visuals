###Loading in packages

import pandas as pd
import numpy as np
print('cell successfully ran')

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as ps

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
dataframe['DATETIME_STRING'] = dataframe['DATESTAMP_MOD_MONTH_YEAR'].astype(str)

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
##dataframe = length -90,000
##selectCounties = length 2,830
##selectCountytime= ???/TBD

selectcountytime = selectCounties

selectcountytime['DATESTAMP_MOD_MONTH_YEAR']


selectCountTime_april2020 = selectcountytime[selectcountytime['DATESTAMP_MOD_MONTH_YEAR'] == '2020-04']
len(selectCountTime_april2020)

selectCountTime_may2020 = selectcountytime[selectcountytime['DATESTAMP_MOD_MONTH_YEAR'] == '2020-05']
len(selectCountTime_may2020)

selectCountTime_aprilmay2020 = selectcountytime[(selectcountytime['DATESTAMP_MOD_MONTH_YEAR'] == '2020-05')|(selectcountytime['DATESTAMP_MOD_MONTH_YEAR'] == '2020-04')]
len(selectCountTime_may2020)

selectCountTime_aprilmay2020.head(50)


###Creating the final dataframe/specific columns/features/attributes that we care about

finalDF = selectCountTime_aprilmay2020[[
    'County',
    'DATESTAMP_MOD',
    'DATESTAMP_MOD_DAY',
    'DATESTAMP_MOD_DAY_STRING',
    'DATETIME_STRING',
    'DATESTAMP_MOD_MONTH_YEAR',
    'C_New', ##cases-new
    'C-Cum', ##cases-total
    'H_New', ##hosptializations -new
    'H-Cum', ##hosptializations - total
    'D-New', ##deaths-new
    'D-Cum' ##deaths-total
]]

finalDF

##Looking at total COVID cases by month

finalDF_dropdups = finalDF.drop_duplicates(subset=['COUNTY', 'DATETIME_STRING'], keep='last' )
finalDF_dropdups


pd.pivot_table(finalDF_dropdups, values='C_Cum', index=['COUNTY'], columns=['DATESTAMP_MOD_MONTH_YEAR'], aggfunc=np.sum)

vis1 = sns.barplot(x='DATESTAMP_MOD_MONTH_YEAR',y='C_Cum', data=finalDF_dropdups)

vis2 = sns.barplot(x='DATESTAMP_MOD_MONTH_YEAR', y='C_Cum', hue='COUNTY', data=finalDF_dropdups)

plotly1 = px.bar(finalDF_dropdups, x='DATETIME_STRING', y='C_Cum', color='COUNTY', barmode='group')
plotly1.show()

plotly2 = px.bar(finalDF_dropdups, x='DATETIME_STRING', y='C_Cum', color='COUNTY', barmode='stack')
plotly2.show()

###Looking at total covid cases by day

daily = finalDF
daily
len(daily)

pd.pivot_table(daily, values='C_Cum', index=['COUNTY'], columns=['DATESTAMP_MOD_DAY'], aggfunc=np.sum)

pd.pivot_table(daily, values='C_Cum', index=['DATESTAMP_MOD_DAY'], columns=['COUNTY'], aggfunc=np.sum)

startdate = pd.to_datetime('2020-04-26').date()
enddate = pd.to_datetime('2020-05-09').date()

maskFilter = (daily['DATESTAMP_MOD_DAY'] >= startdate) & (daily['DATESTAMP_MOD_DAY'] <= enddate)
dailySpecific = daily.loc[maskFilter]
dailySpecific

dailySpecific[dailySpecific['COUNTY'] == 'FULTON']

vis3 = sns.lineplot(data=dailySpecific, x='DATESTAMP_MOD_DAY', y='C_Cum')

vis3 = sns.lineplot(data=dailySpecific, x='DATESTAMP_MOD_DAY', y='C_Cum', hue='COUNTY')

plotly3 = px.bar(dailySpecific, x='DATESTAMP_MOD_DAY', y='C_Cum', color='COUNTY')
plotly3.show()

plotly4 = px.bar(dailySpecific,
                 x='DATESTAMP_MOD_DAY',
                 y='H_New',
                 color='COUNTY',
                 barmode='group')
plotly4.show()

plotly4 = px.bar(dailySpecific,
                 x='DATESTAMP_MOD_DAY',
                 y='H_Cum',
                 color='COUNTY',
                 barmode='group')
plotly4.show()

dailySpecific['newHospandDeathCovid'] = dailySpecific['D_New'].astype(int) + dailySpecific['H_New'].astype(int) + dailySpecific['C_New'].astype(int)
dailySpecific['newHospandDeathCovid']

dailySpecific['newHospandDeath'] = dailySpecific['D_New'].astype(int) + dailySpecific['H_New'].astype(int)
dailySpecific['newHospandDeath']

dailySpecific


plotly8 = px.bar(dailySpecific,
                 x='DATESTAMP_MOD_DAY',
                 y='newHospandDeathCovid',
                 color='COUNTY',
                 title='Georgia 2020 COVID Data: Total New Hospitalizations, Deaths, and COVID cases by County',
                 labels={
                     'DATESTAMP_MOD_DAY': "Time (Month, Day, Year)",
                     'newHospandDeathCovid': "Total Count"
                 },
                 barmode='group')
plotly8.update_layout(
    xaxis=dict(
        tickmode='linear',
        type='category'
    )
)


plotly8.show()