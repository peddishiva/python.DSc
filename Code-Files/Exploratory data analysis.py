import os
import pandas as pd
import numpy as np


carsdf=pd.read_csv('File-path/Toyota.csv', index_col=0, na_values=["??","????"])

carsdf.info()
carsdf.head()

#Creating copy of original data
c2 = carsdf.copy()


'''FREQUENCY table -- pandas.crosstab() method is used

returns the frequency of each type i.e for ex: CNG- 15 vechiles
output:
    
col_0     count
FuelType       
CNG          15
Diesel      144
Petrol     1177
'''

pd.crosstab(index=c2['FuelType'],columns='count',dropna=True)
#dropna - its drops nan values from the variables[column]

'''
TWO- WAY TABLES -- pandas.crosstab() method is used
# uses same function as freq. table

0- Manual gear box
1 - Automatic gearbox

'''
pd.crosstab(index=c2['Automatic'],columns=c2['FuelType'],dropna=True)
#returns the  Two Way table i.e (FuelType X Automatic)

'''
joint probability :
Two-way table - joint probability 
- also uses pandas.crosstab() method

'''

pd.crosstab(index=c2['Automatic'],
            columns=c2['FuelType'],
            normalize=True,
            dropna=True)
#reeturns output values in "proportionality of probability" instead of integers
#ex:
'''
    FuelType        CNG    Diesel    Petrol
    Automatic                              
    0          0.011228  0.107784  0.826347
    1          0.000000  0.000000  0.054641
'''

'''
   Two-way table - marginal probability
   marginal probability: Marginal probability is the probability of the occurrence of the single event
  --- pandas.crosstab() method
'''

pd.crosstab(index=c2['Automatic'],
            columns=c2['FuelType'],
            normalize= True,
            margins = True,
            dropna=True)
'''
Out[]: 
    
FuelType        CNG    Diesel    Petrol       All-(probobility)
Automatic                                        
0          0.011228  0.107784  0.826347  0.945359
1          0.000000  0.000000  0.054641  0.054641
All        0.011228  0.107784  0.880988  1.000000

#returns sum of rows and sum of columns.
'''

'''
Two-way table - conditional probability
pandas crosstab()
   1. Conditional probability is the probability of an event (A), 
   given that another event ( B ) has already occurred
   2. Given the type of gear box, probability of different fuel type
'''

pd.crosstab(index=c2['Automatic'],
            columns=c2['FuelType'],
            normalize= 'index', # which makes the sum of the row values is = 1
            margins = True,
            dropna=True)

'''
Out[59]: 
FuelType        CNG    Diesel    Petrol
Automatic                              
0          0.011876  0.114014  0.874109 - sum= 1.00000
1          0.000000  0.000000  1.000000
All        0.011228  0.107784  0.880988 - probability
'''

'''
Two-way table - conditional probability
-pandas.crosstab() method used 
  1.Conditional probability is the probability of an event (A),given that another event ( B ) has already occurred

'''
pd.crosstab(index=c2['Automatic'],
            columns=c2['FuelType'],
            normalize= 'columns',
            margins = True,
            dropna=True)

'''
Out[]: 
FuelType   CNG  Diesel    Petrol       All- probability 
Automatic                                 
0          1.0     1.0  0.937978  0.945359 
1          0.0     0.0  0.062022  0.054641
                     sum-1.000000
'''

'''
Correlation
DataFrame,corr(se1f, method='pearson')
  1.To compute pairwise correlation of columns excluding NA/null
values
  2.Excluding the categorical variables to find the Pearson's
correlation

'''

#excluding the variable datatype i.e objects from the new dataframe called numdata
numdata = c2.select_dtypes(exclude=[object])

print(numdata.shape)
#This returns the shape of the dataframe 

# Dataframe.corr(self,method="pearson"): syntax 
corr_mat = numdata.corr()

#we can also use multiple mehods in correlation like method='spearman',"pearson","kendall" etc.
#IMPORTANT
