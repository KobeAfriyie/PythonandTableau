# -*- coding: utf-8 -*-
"""
Created on Mon May  2 23:08:23 2022

@author: aguru
"""


import pandas as pd

Data = pd.read_csv ('transaction.csv', sep= ';')

Data.info()

#Definig Variables

CostPerItem =11.73
SellingPricePerItem=21. 
NumberOfItemsPurchased=6

# Mathematical Operations
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased *  ProfitPerItem

CostPerTransaction = NumberOfItemsPurchased * CostPerItem

SellingPricePerTransaction = NumberOfItemsPurchased * SellingPricePerItem

# CostPerTransaction Column Calculation
#CostPerTransaction = NumberOfItemsPurchased * CostPerItem
# To single out one Column, run Variable = data['Column_name']

CostPerItem = Data['CostPerItem']
Data['CostPerTransaction'] = Data ['CostPerItem'] * Data['NumberOfItemsPurchased']

CostPerTransaction = Data ['CostPerTransaction']

SalesPerTransaction = SellingPricePerItem * NumberOfItemsPurchased

Data['SalesPerTransaction']= Data['SellingPricePerItem'] * Data['NumberOfItemsPurchased']

SalesPerTransaction = Data['SalesPerTransaction']

SellingPricePerItem = Data['SellingPricePerItem']

#Profit Calculation = Sales - Cost

Data['ProfitPerTransaction'] = Data ['SalesPerTransaction'] - Data['CostPerTransaction']

ProfitPerTransaction = Data['ProfitPerTransaction']

#Markup = (Sale -Cost)/Cost

Markup = (SalesPerTransaction - CostPerTransaction)/CostPerTransaction

Data ['Markup'] = (Data['ProfitPerTransaction'])/CostPerTransaction

# define Rounding markup
roundmarkup = round (Data['Markup'], 2)

#Add Round markup to Column
Data['Markup'] = round (Data['Markup'], 2)

# Combining Data fields

#eg. my_name = 'Kobe' + 'Afriyie'

my_name = 'Kobe' + 'Afriyie'

# Combining Year, Month, Day columns
# First Change Column data type to a common type, say from int. to str
# Eg. Day is int dtype, Month str dtype, Year int dtype. 
# Change all variable dtype to str or object before combining columns
# Use 'as' function to change dtypes 

#Day = Data ['Day'].astype
#Year = Data ['Year'].astype 

#CheckingColumns, Data type
print(Data['Day'].dtype)

#Changing Column type, we use 'as' function eg. from int to str 
Day = Data ['Day'].astype(str)

Year = Data [ 'Year'].astype(str)

print(Day.dtype)

print(Year.dtype)

my_date = Day + '-'

my_date = Day + '-' + Data['Month'] + '-' + Year

# Using iloc to view specific Columns and Rows

Data.iloc[0]

Data.iloc[-5:]

Data.iloc [0:3]

#Data.iloc [;]

Data.iloc[:]

Data.iloc[:, 2]

Data.iloc[4,2]


# Add new Date Column to Dataframe

Data['Date']= my_date


#Data Transformation
#Using split function to split the ClientKeyword field or column
#new_var = Column.str.split ('sep' , expand =True)
# 'Sep' , expand =True means python is going to separate or split all fields withcomasin one column

Split_Col = Data['ClientKeywords'].str.split (',' , expand =True)

# Spliting Columns into 3 columns namely 0= ClientAge, 1= Client Type, 2= LengthOfContract

Data ['ClientAge'] = Split_Col [0]

Data ['ClientType'] = Split_Col [1]

Data ['LengthOfContract'] = Split_Col [2]


# Replacing the [ ]with nothing to make the new colums clean
# Using the replace function to replace another character in a field or column

Data ['ClientAge'] = Data['ClientAge'].str.replace (']' , '')

Data ['LengthOfContract'] = Data['LengthOfContract'].str.replace (']' , '')


# Using the lower function to change item to lowercase
# changing item Description from Uppercase to a lowercase

Data ['ItemDescription'] = Data ['ItemDescription'].str.lower()


Seasons = pd.read_csv ('value_inc_seasons.csv' , sep = ';')

#Merging files: merge_df = pd.merge (df_old,  , on = 'key')

Data = pd.merge (Data,Seasons, on = 'Month')

#Dropping Columns
#df = df.drop('Columnname' , axis = 1)
# axis = 1 is for a Column whereas axis = 0 is for row

Data = Data.drop ('ClientKeywords' , axis =1)

Data = Data.drop (['Day', 'Month', 'Year'] , axis =1)
#Data = Data.drop ('Year' , axis =1)

#Exporting Transformed or Cleaned Dataframe from python into csv file

#Export into csv

Data.to_csv('ValueInc_Cleaned.csv' , index = False)

#index = False means we want to remove the index Colum from the new Dataframe




