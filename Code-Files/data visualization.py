import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing data from csv file 
cars=pd.read_csv('File-path/Toyota.csv', index_col=0, na_values=["??","????"])

cars.dropna(axis=0, inplace=True)
#Dataframe.dropna(axis=0, inplace=True) 

'''
axis=0 --which means remove the nan values from rows, 
implace=True -- which means reflect the changes in the Dataframe. if not used it doesn't reflrct on df.'
'''
#SCATTER PLT

plt.scatter(cars['Age'], cars['Price'], c="red")
# syntax: plt.scatter(x,y,kwargs) a,y are variables assigned to axies  

plt.title("scatter plot of price vs age of the cars")
#adds the title for the graph/ plot

plt.xlabel('age (momnths)')
plt.ylabel('Price (Euros)')

# plt.xlabel(), plt.ylabel() are used to label the values for axies 

plt.show()
#to show the plot/graph after changes

#HISTOGRAM 

plt.hist(cars['KM'],color='green',edgecolor='white',bins=10)
# plt.hist() is used for hostogram graphs/plots

'''
diff. btwn bar graphs and histogram - this is used numerical variable & for continueos data and deosn't have gaps 
where as bar graph has gaps btw bars and not continueos & its represents categorical variable 

'''
#BAR PLOT

counts=[792,120,12]
fuelType =('Petrol','Diesel','CNG')
index = np.arange(len(fuelType))

plt.bar(index,counts,color=['blue','red','cyan']) # index - x and height of the bars - counts
plt.title('Bar plt for fuels')
plt.xlabel('Fuel Type')
plt.ylabel('Frequency')
plt.xticks(index, fuelType, rotation = 0) # to assign the values for the bars using xticks
plt.show()

'''
#SEABORN LIBRARY - based on matpltlib 

Importing necessary libraries 

import pandas as pd
import numpy as np
import matplotlib.pyplt as plt
import seaborn as sns

'''
import seaborn as sns

sns.set(style='darkgrid')        
#regplt - regression plot

sns.regplot(x=cars['Age'],y=cars['Price'])

sns.regplot(x=cars['Age'],y=cars['Price'], marker="*", fit_reg = False)
# fit_reg = True - by default it calculates the coefficient of x and plots a regression line on graph
#fit_reg = False -- to remove the regression line
        
'''
scatter points are called as markers 
and the boxs are called as grids

xlabel adn ylabel are not used in sns cuz it takes the labels from the variable we assign
we can change the shape of theh markers using method  --  marker ="*"

Using hue parameter, including another variable to show the fuel
types cåtegories with different colors

'''
sns.lmplot(x='Age',y='Price', data = cars , fit_reg = False, hue='FuelType',legend = True, palette ="Set1")        

'''
similarly we can custom the appearance of the markers using:
transparency
shape
size
 
'''

#HISTOGRAM USING SEABORN

'''
Histogram with default kernel density estimate - curve
sns.distplot()- distribution plot #used to take continueos variable onlt
'''

sns.distplot(cars['Age']) 

# "kde = False" to  remove the curve from the graph 
# bins = 5 used to set the bars count by merging the original bars

'''
#BAR PLOT USING SNS - barplots are used on categorical variable to check the freq.
Frequency distribution of fuel type of the cars


'''
sns.countplot(x="FuelType", data = cars)

sns.countplot(x="FuelType", data = cars, hue = "Automatic")
# hue = 'Variable/col.name' to get graph corresponding to the barplot
 
'''
#Box and whiskers plot - numerical variable
Box and whiskers plot of Price to visually interpret the
five-number summary
q1, q2, q3 -- q:quantile
highest - max
lowest - min
'''

sns.boxplot(y=cars['Price'])
#dots are Outliers which are the extreme values, 

'''
Box and whiskers plot
• Box and whiskers plot for numerical vs categorical variable
'''

sns.boxplot(x=cars['FuelType'],y=cars['Price'])

'''
Grouped box and whiskers plot
• Grouped box and whiskers plot of Price vs FuelType and Automatic

'''
sns.boxplot(x=cars['FuelType'],y=cars['Price'], hue ="Automatic", data=cars)        
# desiel and cng doesnot have any automatic vechiles so they dont have automatic graph


'''
#Box-whiskers plot and Histogram

• Let's plot box-whiskers plot and histogram on the same window
• Split the plotting window into 2 parts
'''

f,(ax_box,ax_hist)=plt.subplots(2, gridspec_kw={"height_ratios":(.15,.85)})
   # 1.f- figure and 2.(ax_box,ax_hist) - variable for 
   #.subplots(no of partions to divide, ratio of the each partion) - used to divide the graph 
   # ratio of the each partion - is given using the method gridspec_kw ={"height_ratios" : (.15,.85)} - sum of partion ratio need to be 1



sns.boxplot(cars['Price'],ax=ax_box)

sns.distplot(cars['Price'],ax=ax_hist, kde=False)

'''
Pairwise plots
• It is used to plot pairwise relationships in a dataset
• Creates scatterplots for joint relationships and histograms for
univariate distributions
'''

sns.pairplot(cars, kind = "scatter", hue = "FuelType")
# returns all the possible outcomes as a graphs 
plt.show()






        
        
        
        
        
        
        
        