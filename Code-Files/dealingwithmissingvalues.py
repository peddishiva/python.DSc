import os
import pandas as pd

#os.chdir(" ") # file path inside the(" ")

#importing data from csv file 
cars=pd.read_csv('File-path/Toyota.csv', index_col=0, na_values=["??","????"])

cars2= cars.copy()
cars3= cars.copy()

'''
• In Pandas dataframes, missing data is represented
by NaN (an acronym for "Not a Number")

• To check null values in Pandas dataframes,
isnull() and isna() are used

• These functions returns a dataframe of Boolean (True, False)
values which are True for NaN values

#syntax:
    Dataframe..isna().sum()    or
    Dataframe..isnull().sum() - both are same methods returns same result
'''

cars2.isna().sum() 
#(or)
cars2.isnull().sum()
# the above code gives the result : each row are missing in each column

#Identifying missing values Subsetting the rows that have one or more missing values
missing = cars2[cars2.isna().any(axis=1)]


'''
Approached to fill the missing values
 Two ways of 
approach:
    1.Fill the missing values by mean / median, in case of numerical variable
    2.Fill the missing values with the class which has maximum count, in case of categorical variable

'''

#Imputing missing values
#Syntax - DataFrame.describe()

cars2.describe()
# returns Statistical summary of data

#imputing missing values of ‘Age’
# Calculating the mean value of the Age variable

cars2['Age'].mean()

'''
 To fill NA/NaN values using the specified value
 DataFrame.fillna()
'''

cars2['Age'].fillna(cars2['Age'].mean(),inplace =True)
#replaces nan values with the mean value

#Imputing missing values of 'KM'
#• Calculating the median value of the KM variable
cars2["KM"].median()

cars2['KM'].fillna(cars2['KM'].median(),inplace =True)
#replaces nan values with the median value

'''
Imputing missing values of ‘HP’
 • Calculating the mean value of the HP variable
 syntax: Dataframe.mean()
'''

cars2['HP'].mean()

cars2['HP'].fillna(cars2['HP'].mean(),inplace =True)

cars2.isnull().sum()

'''
Imputing missing values of ‘FuelType’
 Syntax:             Series.value_counts()
 • Returns a Series containing counts of unique values
 • The values will be in descending order so that the 
first element is the most frequently-occurring 
element
 • Excludes NA values by default
'''
cars2['FuelType'].value_counts()
# returns the variables corresponding in most frequently-occurring element


cars2['FuelType'].fillna(cars2['FuelType'].value_counts().index[0],inplace =True)
# fills the nan values withe the most freq. repeated value

cars2['MetColor'].mode()
#calculate the mode for MetColor cause its not a scalar value

cars2['MetColor'].fillna(cars2['MetColor'].mode()[0],inplace=True)

cars2.isnull().sum()
#to check the missing values in a dataframe

'''
Imputing missing values using lambda functions
 • To fill the NA/ NaN values in both numerical and categorial variables at one stretch


 • here we use an if-else function i.e after calculating the every variables/columns and 
the result which are in the form of float fells into else block.

'''

cars3=cars3.apply(lambda x:x.fillna(x.mean()) if x.dtype=='float' else x.fillna(x.value_counts().index[0]))
# lambda is the autonomous funtion which is used allover the df. 
#here we use an if-else function i.e after calculating the every variables/columns and the result which are in the form of float fells into else block.

cars3.isnull().sum()












































