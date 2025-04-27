import os
import pandas as pd
import numpy as np

df=pd.read_csv('C:/Users/peddi/OneDrive/Pictures/Desktop/contacts.csv')

'''
df=pd.read_csv('File-path/contacts.txt', delimeter="/t")
pd.read_txt -- for txt
pd.read_xlxs -- for excel
'''
df.shape # returns the dimentionality of the file (column, rows) 
df.index #returns the index values start, stop, step
df.columns # returns the name of the colunms 
df.size #returns the size of the file (col*rows)

df.memory_usage() # returns the memory usage of each coloum and also returns the datatype of "output"
df.ndim #used to return the total number of dimensions 

df.head() #Returns the first five rows by default/ you can even specify the number value btw () to fetch rows 
df.tail() #Returns the last five rows by default/ you can even specify the number value btw () to fetch rows

''' used after sorting and append funtion to check'''

'''

To access the scaler value - 
at[] method is used to fetch the req. value 
iat[] method is used to frtch using integer based values

'''
 
df.at[1,'First Name'] # [row value, 'column name'] to fetch the required Value
df.iat[1,18] #[row no, column no] to fetch the required Value

''' .loc[] method used to access a group of rowa and columns by label(s)'''

df.loc[:,'First Name']
#slicing operator is used for .loc method [:,'column name'] you can also give multiple col's.

df.dtypes
# returns the data types containing in the Dataframe

''' returns the count of diff. datatypes '''
df.dtypes.value_counts()

'''
pandas.DataFrame.select_dtypes ( )
returns a subset of the columns from dataframe based on column dtypes
Syntax:
    
DataFrame.select_dtypes(include=None,exclude=None)
'''
df.select_dtypes(exclude=[object])
print(df)

df.info()  
#returns indetail info of the dataframe with corresponding dtype and column name

'''
unique() is used to find the unique elements of a column
Syntax: numpy.unique(array)
it can't take multiple columns. it only on column. 
'''
print(np.unique(df['First Name']))
#returns the every element in the column 


carsdf=pd.read_csv('C:/Users/peddi/OneDrive/Pictures/Desktop/NPTEL/pythonfiles/Toyota.csv', index_col=0, na_values=["??","????"])

#returns the information of dataframe
carsdf.info() 

'''
astype()
method is used to explicitly convert data types from one to another
Syntax: DataFrame.astype(dtype)
'''

carsdf['MetColor'] = carsdf['MetColor'].astype('object')
carsdf['Automatic']= carsdf['Automatic'].astype('object')

'''
nbytes() is used to get the total bytes consumed by the elements of the columns
Syntax: ndarray.nbytes
'''

carsdf['FuelType'].nbytes 
# coverts the obj to category and returns the bytes
carsdf['FuelType'].astype('category').nbytes

'''
replace() is used to replace a value with the desired value
Syntax:
DataFrame.replace([to_replace,value, inplace=true])
'''

carsdf['Doors'].replace('three',3,inplace=True)
carsdf['Doors'].replace('four',4,inplace=True)
carsdf['Doors'].replace('five',5,inplace=True)

#To convert a col. in datatype to another datatype
carsdf['Doors'] =carsdf['Doors'].astype('int64')

#To check the df if there are any missing values or not in the numeric values
carsdf.isnull().sum()

#returns true if the object consists missing values
carsdf.isnull()

carsdf.info()


''' Control flow statements'''

carsdf.insert(10,'price_class',"")
#.insert(position,column name, Blank values- total col has blank values)

'''
# for loop:
    
    
for i in range(0, len(carsdf['price']), 1):
    if (carsdf['price'][i]<=8450): 
        casrdf['price_class'][i]="LOW"
    elif(carsdf['price'][i]>11950):
        casrdf['price_class'][i]="HIGH"
    else:
        casrdf['price_class'][i]="MEDIUM"

# while loop:

    
i=0

while i<len(carsdf['price']):
    if (carsdf['price'][i]<=8450): 
        casrdf['price_class'][i]="LOW"
    elif(carsdf['price'][i]>11950):
        casrdf['price_class'][i]="HIGH"
    else:
        casrdf['price_class'][i]="MEDIUM"

i=i+1        
'''

# returns series of Unique functions
# syntax: series.value_counts()

carsdf['price_class'].value_counts() # returns the values  

'''
def function_name(parameters):
    statements
'''

carsdf.insert(11,'Age_converted',0)

def cov(val):
    val_converted = val/12
    return val_converted

carsdf["Age_converted"]=cov(carsdf["Age"])
# conv function used to convert months to years

carsdf["Age_converted"]=round(carsdf["Age_converted"],1)
# round(col.name, demcimal values req after integer.)

carsdf.insert(12,'km_per_month',0)

def covert(val1,val2):
    val_converted = val1/12
    ratio = val2/val1
    return [val_converted,ratio]

carsdf['val_converted'],carsdf['km_per_month'] = covert(carsdf['Age'], carsdf['KM'])


carsdf['km_per_month']=round(carsdf["km_per_month"],1)
carsdf['val_converted']=round(carsdf["val_converted"],1) 
# removed  extra decimals using above round value

carsdf.head()
#to check the first five values after changes


    








