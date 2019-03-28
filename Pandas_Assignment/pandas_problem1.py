# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 12:15:39 2019

@author: SREEKUTTY
"""

#PANDAS ASSIGNMENT

# Qn.1. How-to-count-the-distance-to-the-previous-zero
# For each value, count the difference of the distance from the previous zero(or the start of the Series, whichever is closer) and if there are no previous zeros, print the position
# Consider a DataFrame df where there is an integer column{'X':[7,2,0,3,4,2,5,0,3,4]}
# The values should therefore be [1,2,0,1,2,3,4,0,1,2]. Make this a new column 'Y'/


import numpy as np
import pandas as pd

df=pd.DataFrame({'X':[7,2,0,3,4,2,5,0,3,4]})

#Counting the distance to the previous zero

X=[7,2,0,3,4,2,5,0,3,4]

count=1
Y=[]
for items in X:
    if items==0:
        count=0
    
    Y.append(count)
    count+=1
print('Y = ',Y)

df=pd.DataFrame({'X':[7,2,0,3,4,2,5,0,3,4],'Y':[1, 2, 0, 1, 2, 3, 4, 0, 1, 2]})


### Qn.2. Create a Datetimeindex that contains each business day of 2015 and use it to index a Series of random numbers

DtIndex = pd.date_range('2015-01-01', '2015-12-31',freq='B')  #freq='B' stands for 'Business day' starting from 1st Jan to 31st Dec of 2015
DtIndex

    #making s as the series of random numbers and using my DtIndex to index s
s=pd.Series(np.random.rand(len(DtIndex)),index=DtIndex)
s                  #created a DatetimeIndex that contains each businessday of 2015 and that has been used to index to a series of random numbers

BD = pd.DataFrame(data = s, index= DtIndex)
    #Created a dataframe with DtIndex as 'index' and 's' as attribute
BD.columns=['s']        #naming column as 's'
BD.head()     
BD.shape



# Qn.3 Find the sum of the values in s for every Wednesday

        #I have created the dataframe BD with attribute 's'. So taking sum of all wednesdays in 2015 from BD
BD.head()
BD['Day']=DtIndex.day_name() #creating a column for showing the corresponding days for the date 
BD.head(7)
BD1=BD.copy()
BD1=BD1.groupby(['Day']).sum()
BD1

        #Another method for finding the sum of s for all Wednesday
BD2=BD.copy()
sum_of_s=BD2[BD2.Day=="Wednesday"].s.sum()
sum_of_s

# Qn.3.Average for each calendar month


BD.resample('M').mean() #finding the average for each month in 2015

# Qn.5. For each group of four consecutive calendar months in s, find the date on which the highest value occurred

BD.head(10)
BD.groupby(pd.Grouper(freq='M')).max()[:4] #finding date on which s was highest for 4 consecutive months


