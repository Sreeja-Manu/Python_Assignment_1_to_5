# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 06:45:51 2019

@author: SREEKUTTY
"""

import numpy as np
import pandas as pd


df=pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')

df.describe()
df.head()
df.tail()
df.isnull()

#Qn.1. Delete unnamed columns

df.columns
df1=df.copy()
del df1['Unnamed: 0'] #using delete method 
df1.head()
df2=df.copy()
df2.drop('Unnamed: 0',axis=1,inplace=True)#using drop method


#Qn.2. Show the distribution of male and female


df1.head()

female=df1[df1.Gender=='F']
f=female['Gender'].value_counts()

male=df[df1.Gender=='M']
m=male['Gender'].value_counts()

both_genders=df1['Gender'].value_counts()

    #another way to show the distribution
genders=df.groupby(['Gender'])
genders.describe()

#Qn.3.Show the top 5 most preferred names

preferred_name=df1['Name'].value_counts()
preferred_name.head()                          #knowing the most preffered name by knowing the value_counts for the 'Name 'column in df1 dataframe 

#Qn.4.What is the median name occurence in the dataset

df1.head()
df1.Id.median()
median_name=df1[df1['Id']==df1.Id.median()]
median_name

# Qn.5. Distribution of male and female born count by states
distribution=df1.groupby(['Gender','State']).count()
        #Showing the distribution of male and female with respect to each State
distribution.loc[: , 'Count']

pd.crosstab(index=df1.Gender,columns=df1.State) #distribution in a more formatted way
