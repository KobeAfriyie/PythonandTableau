# -*- coding: utf-8 -*-
"""
Created on Fri May  6 02:48:14 2022

@author: aguru
"""

#import json into python
import json
import pandas as pd
import matplotlib.pyplot as plt

#method 1 to read json data. open and load
json_file = open('loan_data_json.json')
data = json.load(json_file)

#method 2 to read json data.
with open('loan_data_json.json')as json_file:
    data = json.load(json_file)

#transform json lists into a nice pandas dataframe we will call loandata
loandata = pd.DataFrame(data)

#finding unique values for the purpose column for example
loandata['purpose']. unique()

#describe the data. 
# It gives for example the Count, Mean, standard Diviation, Minimum value, Maximum value, 25%, 50%, 75% of the various Columns

loandata.describe()

#describe the data for a specific column , eg. Int.rate column

loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#install numpy library. For windows, use Anaconda Prompt, and fror Mac use Terminal
#pip install numpy
#import the numpy into python and run

import numpy as np

#Using Exponential EXP() to getannual income for column log.annual.inc
income = np.exp(loandata['log.annual.inc'])

#Adding new annualincome variable or column to the loandata dataframe
loandata['annualincome'] = income

#Working with arrays
#0D array, 1D array, 2D array

arr = np.array(43)
arr = np.array([1,2,3,4])
arr = np.array([[1,2,3],[4,5,6]])

#Working with IF Statements
a = 40
b = 500
if b>a:
     print('b is greater than a')

#let's add more conditions
a=40
b=500
c=1000
if b>a and b<c:
    print('b is greater than a but less than c')
    
#what if a condition is not met?
a=40
b=500
c=20
if b>a and b<c:
    print('b is greater than a but less than c')
else:
    print ('No condtion met')

#another condition, different metrics
a=40
b=500
c=30

if b>a and b<c:
    print('b is greater than a but less than c')
elif b > a and b>c:
    print('b is greater than a and c')
else:
    print('No condition met')
    
#another example
a=40
b=0
c=30

if b>a and b<c:
    print('b is greater than a but less than c')
else:
    print('No condition met')
#IF Statement for FICO
#FICO Score

fico = 700

# fico >= 300 and < 400:'Very Poor'
# fico >= 400 and ficoscore < 600:'Poor'
# fico >= 601 and ficoscore < 660:'Fair'
# fico >= 660 and ficoscore < 700:'Good'
# fico >=700:'Excellent'

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 601 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico <700:
    ficocat = 'Good'
elif fico >=700:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown'
print(ficocat)

fico = 350

# fico >= 300 and < 400:'Very Poor'
# fico >= 400 and ficoscore < 600:'Poor'
# fico >= 601 and ficoscore < 660:'Fair'
# fico >= 660 and ficoscore < 780:'Good'
# fico >=780:'Excellent'

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 601 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico <700:
    ficocat = 'Good'
elif fico >=700:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown'
print(ficocat)



fico = 559

# fico >= 300 and < 400:'Very Poor'
# fico >= 400 and ficoscore < 600:'Poor'
# fico >= 601 and ficoscore < 660:'Fair'
# fico >= 660 and ficoscore < 780:'Good'
# fico >=780:'Excellent'

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 601 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico <700:
    ficocat = 'Good'
elif fico >=700:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown'
print(ficocat)


fico = 250

# fico >= 300 and < 400:'Very Poor'
# fico >= 400 and ficoscore < 600:'Poor'
# fico >= 601 and ficoscore < 660:'Fair'
# fico >= 660 and ficoscore < 780:'Good'
# fico >=780:'Excellent'

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 601 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico <700:
    ficocat = 'Good'
elif fico >=700:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown'
print(ficocat)


fico = 544

if fico >= 300 and fico <= 400:
    ficocat = 'very poor'
elif fico >= 400 and fico <= 600:
    ficocat = 'poor'
elif fico >= 601 and fico <= 660:
    ficocat = 'Fair'
elif fico >= 660 and fico <=700:
    ficocat = 'Good'
elif fico >=700:
    ficocat = 'Excellent'
else :
    ficocat = 'Unknown'
print(ficocat)
    

# For loops
fruits= ['apple', 'pear', 'banana']
for x in fruits:
    print(x)

#for loop based on position
for x in range (0,3):
    y = fruits [x]
    print(y)
    

# applying for loops to loandata
#using first 10, where x is fico, y is category

ficocat =[]
for x in range (0,10):
    Category = loandata['fico'][x]
    if Category >= 300 and Category <= 400:
        Cat = 'very poor'
    elif Category >= 400 and Category <= 600:
        Cat = 'poor'
    elif Category >= 601 and Category <= 660:
        Cat = 'Fair'
    elif Category >= 660 and Category <=700:
        Cat = 'Good'
    elif Category >= 700:
        Cat = 'Excellent'
    else :
        Cat = 'Unknown'
    ficocat.append(Cat)
    
# length function, to find the number of rows in your dataframe.
# Instead of a range (0,10), use (0,length)

length = len(loandata)
ficocat =[]
for x in range (0,length):
    Category = loandata['fico'][x]
    if Category >= 300 and Category <= 400:
        Cat = 'very poor'
    elif Category >= 400 and Category <= 600:
        Cat = 'poor'
    elif Category >= 601 and Category <= 660:
        Cat = 'Fair'
    elif Category >= 660 and Category <=700:
        Cat = 'Good'
    elif Category >= 700:
        Cat = 'Excellent'
    else :
        Cat = 'Unknown'
    ficocat.append(Cat)
  
ficocat = pd.Series(ficocat)

loandata ['fico.Category'] = ficocat


# #While loops
# i = 1
# while i < 10:
#     print (i)
#     i = i = 1

length = len(loandata)
ficocat =[]
for x in range (0,length):
    Category = 'red'

    try:
        if Category >= 300 and Category <= 400:
            Cat = 'very poor'
        elif Category >= 400 and Category <= 600:
            Cat = 'poor'
        elif Category >= 601 and Category <= 660:
            Cat = 'Fair'
        elif Category >= 660 and Category <=700:
            Cat = 'Good'
        elif Category >= 700:
            Cat = 'Excellent'
        else :
            Cat = 'Unknown'
    except:
        Cat = 'Unknown'
        
        
#Dataframe Conditional Statements
#df.loc as Conditional Statements.
#df.loc[df[Columnname] condition, newColumn = 'Value of the condition is met'

# Thus, a condition is applied to a Column to create  a new Column with a value if the condition is met.
# for int.rate, a new Column is wanted if the rate >0.12 then the value is High for the new column, else low.

loandata.loc[loandata['int.rate'] >0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <=0.12, 'int.rate.type'] = 'low'

#playing around with plot
# First install metplotlib library for ploting on python using Anaconda prompt for windows and terminal for mac.

#pip install matplotlib
# import matplotlib.pyplot as plt

#Example, how many borrowers belong to the various fico categories of very poor, poor, Fair, Good, and Excellent?

# number of loans/rows by fico.Category using groupby function
Catplot = loandata.groupby (['fico.Category']).size()

Purposecount= loandata.groupby (['purpose']).size()

#Plot Categories in a bar chart
Catplot.plot.bar()
plt.show()

#you can change say the color of the bar chart, the size or width of the bars, etc

Catplot = loandata.groupby (['fico.Category']).size()
Catplot.plot.bar(Color = 'green', width = 0.1)
plt.show()


Purposecount= loandata.groupby (['purpose']).size()
Purposecount.plot.bar (color = 'Red' , width =0.2)
plt.show ()

# Scatter plots (x and y values are selected fro the loandata variables)
xpoint = loandata ['dti']
ypoint = loandata ['annualincome']
plt.scatter (xpoint, ypoint, color = 'blue')

#Writing to CSV into your working directory

loandata.to_csv('loan_cleaned.csv', index =True)



