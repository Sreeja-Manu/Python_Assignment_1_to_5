# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 11:50:24 2019

@author: SREEKUTTY
"""
# Qn. This assignment is for visualization using matplotlib:
# data to use:
# url=https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv
#titanic=pd.read_csv(url)
#Charts to plot:
#1. Create a pie chart representing the male/female proportion
#2. Create a scatterplot with the Fare paid and the Age, differ the plot color by gender


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

titanic=pd.read_csv("https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv")
titanic.head()


#1. Create a pie chart representing the male/female proportion
gender=titanic['sex'].value_counts()
gender

labels = 'Male','Female'
sizes= gender         #gender=titanic['sex'].value_counts()
colors= ['#92DFE4','#F394E7'] #got from RGB Hex code

explode = (0,0.02)  # to "explode" the 2nd slice,ie.,showing the 2nd slice as a separated piece

fig,ax = plt.subplots(figsize=(10,5))   #Creates a figure and one subplot
ax.set_title("Male/Female Proportion")

ax.pie(sizes, explode=explode, labels=labels,colors=colors)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

plt.show()

# Qn.2.Create a scatterplot with the Fare paid and the Age, differ the plot color by gender


import seaborn as sns

titanic.head()
titanic.columns

gender1=pd.factorize(titanic['sex'])
fig, ax = plt.subplots()
ax.scatter(titanic['age'], titanic['fare'], c = gender1[0])
plt.show()

    #another method to plot using machine learning. for this we cannot have null values in the column 'sex'
titanic.dtypes
titanic.sex.isnull().sum()

titanic.sex.fillna(method = "ffill", inplace=True)
titanic.sex.isnull().sum()

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
g=LabelEncoder().fit_transform(titanic['sex'].values)

fig, ax = plt.subplots()
ax.scatter(titanic['age'], titanic['fare'], c = g )
plt.show()


  
