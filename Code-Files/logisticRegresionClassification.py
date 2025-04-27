'''
binary classification which divides into 2 classification values then its called as binary classification
'''

# To work with dataframes
import pandas as pd
# To perform numerical operations
import numpy as np
# To perform data visualization
import seaborn as sns

# to partition the data
from sklearn.model_selection import train_test_split

# Importing library for Logistic regression
from sklearn.linear_model import LogisticRegression

# Importing performance metrics -accuracy score & confusion matrix
from sklearn.metrics import accuracy_score, confusion_matrix

#assigning a df. to a string
income = pd.read_csv('File-path/income.csv')

# Creating a copy of original data            
data = income.copy()

"""
#Exploratory data analysis:

#1.Getting to know the data
#2.Data preprocessing (Missing values)
#3.Cross tables and data visualization
"""

#**** To check variables' data type
print(data.info())

#**** Check for missing values             
data.isnull()
#boolean values where true incates the missing data and whereas false indicates no missing data

       
print('Data columns with null values:\n', data.isnull().sum())
#**** No missing values !


#**** Summary of numerical variables
summary_num = data.describe()
print(summary_num)            


#**** Summary of categorical variables
summary_cat = data.describe(include='O')
print(summary_cat)            

#**** gives detailed Summary of variables
data['JobType'].value_counts()
data['occupation'].value_counts()

'''
data['JobType'].value_counts()

Output[]: 
JobType
Private             22286
Self-emp-not-inc     2499
Local-gov            2067
?                    1809
State-gov            1279
Self-emp-inc         1074
Federal-gov           943
Without-pay            14
Never-worked            7
Name: count, dtype: int64

'''

#**** Checking for unique classes
print(np.unique(data['JobType'])) 
print(np.unique(data['occupation']))
#**** There exists ' ?' instesd of nan


"""
Go back and read the data by including "na_values[' ?']" to consider ' ?' as nan !!!
"""
income = pd.read_csv('File-path/income.csv', na_values=[" ?"])

data.isnull().sum()
#**** Check for missing values  and give its missing values per variable in num correspondingly


missing = data[data.isnull().any(axis=1)]
# axis=1 => to consider at least one column value is missing in a row


""" Points to note:
1. Missing values in Jobtype    = 1809
2. Missing values in Occupation = 1816 
3. There are 1809 rows where two specific 
   columns i.e. occupation & JobType have missing values
4. (1816-1809) = 7 => You still have occupation unfilled for 
   these 7 rows. Because, jobtype is Never worked
   
   in this case its very complex to fill the missing values need to model the data to generate the missing data.
   instead we removing the data is the best way. until it doesnot effect the other variables 
"""

data2 = data.dropna(axis=0)
#used to remove the missing values 

data3 = data2.copy()
data4 = data3.copy()


# Realtionship between independent variables
correlation = data2.corr()


'''
# Cross tables & Data Visualization
'''

# Extracting the column names
data2.columns   

'''
# Gender proportion table:
'''
gender = pd.crosstab(index = data2["gender"], columns  = 'count', normalize = True)
print(gender)


'''
#  Gender vs Salary Status:
'''

#Two way table
gender_salstat = pd.crosstab(index = data2["gender"],columns = data2['SalStat'], margins = True, normalize =  'index') 
# Include row and column totals
print(gender_salstat)


# Frequency distribution of 'Salary status'
SalStat = sns.countplot(data2['SalStat'])

"""  
75 % of people's salary status is <=50,000      
& 25% of people's salary status is > 50,000
"""

'''  Histogram of Age   '''
sns.distplot(data2['age'], bins=10, kde=False)
# People with age 20-45 age are high in frequency


#Box Plot - Age vs Salary status
sns.boxplot(x='SalStat', y='age', data=data2)
data2.groupby('SalStat')['age'].median()

## people with 35-50 age are more likely to earn > 50000 USD p.a
## people with 25-35 age are more likely to earn <= 50000 USD p.a


#*** Jobtype
JobType     = sns.countplot(y=data2['JobType'],hue = 'SalStat', data=data2)
job_salstat =pd.crosstab(index = data2["JobType"],columns = data2['SalStat'], margins = True, normalize =  'index')  
round(job_salstat*100,1)


#*** Education
Education   = sns.countplot(y=data2['EdType'],hue = 'SalStat', data=data2) 
# data = data2 here data is an keyword which asks for dataframe. and data2 is dataframe
EdType_salstat = pd.crosstab(index = data2["EdType"], columns = data2['SalStat'],margins = True,normalize ='index')  
round(EdType_salstat*100,1)
# multipies the EdType_salstat - with 100 to make the proportions into persentages and then round method is used to make the persentage into float of 1 decimal to make it better readability


#*** Occupation
Occupation  = sns.countplot(y=data2['occupation'],hue = 'SalStat', data=data2)
occ_salstat = pd.crosstab(index = data2["occupation"], columns =data2['SalStat'],margins = True,normalize = 'index')  
round(occ_salstat*100,1)

#*** Capital gain
sns.distplot(data2['capitalgain'], bins = 10, kde = False)

sns.distplot(data2['capitalloss'], bins = 10, kde = False)

# =============================================================================
# LOGISTIC REGRESSION


# Reindexing the salary status names to 0,1cuz the mmachine learning model can't understand the raw data. it understands 0,1 only
data2['SalStat']=data2['SalStat'].map({' less than or equal to 50,000':0,' greater than 50,000':1})
print(data2['SalStat'])
# here we map using the dictionary key mapping. we can even invert the integer values to get labels back 
#{label:integer}
#to make all string type values to integer type values

new_data=pd.get_dummies(data2, drop_first=True)
#.get_dummies using it we can convert cat. variables into dummy variables which is called as onehot  encoding


# Storing the column names 
columns_list=list(new_data.columns)
print(columns_list)


# Separating the input names from data
features=list(set(columns_list)-set(['SalStat']))
print(features)
#removing the 'SalStat' from set column_list and storing the removed output it in a form of list into a char- features

# Storing the output values of SalStat - in y
y=new_data['SalStat'].values  
print(y)


# Storing the values from input features
x = new_data[features].values
print(x)


# Splitting the data into train and test
train_x,test_x,train_y,test_y = train_test_split(x,y,test_size=0.3, random_state=0)
#70 , 30 , 70, 30
'''
#train_test_split is module used for training,testing,spliting the data
the out put is saved into four DF's - train_x,test_x,train_y,test_y
test_size=0.3 which is of 30% of total data , splitted into 100- 70-train & 30-test
random_state=0 - which means -take the data from the provided dataframe only for testing
'''

# Make an instance of the Model LogisticRegression Classifier
logistic = LogisticRegression()

# Fitting the values for x and y - .fit() is used to fit the data into instance
logistic.fit(train_x,train_y)
# training the instance of LogisticRegression Classifier sing the taining data from train_test_split method


#extraction of attributes of logistic regression classifier model
logistic.coef_
# returns the coffecient values from LogisticRegression Classifier model
logistic.intercept_
# returns the intercept values from LogisticRegression Classifier model

# Prediction from test data
prediction = logistic.predict(test_x)
print(prediction)


# Confusion matrix - used to evaluate the classification model
confusion_matrix = confusion_matrix(test_y, prediction)
print(confusion_matrix)
'''
test_y - actual output values 
prediction - predicted uotput values from test_x using logistic regression classifier
'''

# Calculating the accuracy
accuracy_score=accuracy_score(test_y, prediction)
print(accuracy_score)
#84% predictions are correct


# Printing the misclassified values from prediction
print('Misclassified samples: %d' % (test_y != prediction).sum())
#test_y != prediction -doesnot match with original 


'''
# LOGISTIC REGRESSION - REMOVING INSIGNIFICANT VARIABLES
'''

# Reindexing the salary status names to 0,1
data3['SalStat']=data3['SalStat'].map({' less than or equal to 50,000':0,' greater than 50,000':1})
print(data3['SalStat'])


cols = ['gender','nativecountry','race','JobType']
new_data = data3.drop(cols,axis = 1) 
#The parameter axis=1 indicates that the operation is performed along the column axis (as opposed to rows).
print(cols)

new_data=pd.get_dummies(new_data, drop_first=True)

'''
The reason for converting categorical variables into dummy variables in the new_data DataFrame 
is to enable these variables to be used in machine learning models, 
which typically require numerical input. Dummy variables represent each category as a separate binary column (0 or 1),
allowing the model to understand and analyze categorical data effectively. This is crucial for algorithms like linear regression and logistic regression, 
which cannot directly process categorical data.
'''

# Storing the column names 
columns_list2=list(new_data.columns)
print(columns_list2)

# Separating the input names from data
features2=list(set(columns_list2)-set(['SalStat']))
print(features2)

# Storing the output values in y
y2=new_data['SalStat'].values
print(y2)

# Storing the values from input features
x2 = new_data[features2].values
print(x2)

# Splitting the data into train and test
train_x2,test_x2,train_y2,test_y2 = train_test_split(x2,y2,test_size=0.3, random_state=0)

# Make an instance of the Model
logistic2 = LogisticRegression()

# Fitting the values for x and y
logistic2.fit(train_x2,train_y2)

# Prediction from test data
prediction2 = logistic2.predict(test_x2)


# Prediction from test data
prediction2 = logistic.predict(test_x)
print(prediction2)


# Confusion matrix - used to evaluate the classification model
confusion_matrix2 = confusion_matrix(test_y, prediction)
print(confusion_matrix2)
'''
test_y - actual output values 
prediction - predicted uotput values from test_x using logistic regression classifier
'''

# Calculating the accuracy
accuracy_score2=accuracy_score(test_y, prediction)
print(accuracy_score2)
#84% predictions are correct


# Printing the misclassified values from prediction
print('Misclassified samples: %d' % (test_y2 != prediction2).sum())

'''
# END 
'''