import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

boston_df = pd.read_csv("path)

boston_df

display(boston_df)

#if any missing values
boston_df.isnull().sum()

plt.figure(figsize=(20,9))
plt.plot(boston_df['AGE'])
plt.title("Age line plot")
plt.xlabel("Row of index")
plt.ylabel("Row")
plt.show()

plt.figure(figsize=(20,9))
plt.bar(x=boston_df['ZN'], height = boston_df['AGE'], width=1.5, color ='deeppink')
plt.title("Bar plot", fontsize = 13)
plt.xlabel("Row of index")
plt.ylabel("Row")
plt.show()

'''
# Range of Data vs Frequency of Values b/w range (Bins)
1 - 60
[4, 5, 7, 11, 15, 21, 24, 31, 33, 36, 42, 44, 44, 45, 47, 51, 59]
1-10 : 3
11-20 : 2
21-30 : 2
'''

# Bins = 20
plt.figure(figsize = (13,9))
plt.hist(boston_df['MEDV'], bins = 20)
plt.title("Hist Plot", fontsize = 13)
plt.xlabel("MEDV")
plt.ylabel("Frequency in Range")
plt.show()

iris_df = pd.read_csv("https://raw.githubusercontent.com/ammishra08/MachineLearning/master/Datasets/iris.csv", sep = ',')
display(iris_df)

iris_df['species'].unique()

iris_df['species'].unique()

plt.scatter(x=iris_df['sepal_length'], y=iris_df['petal_length'])

# Merging two seperate plots into one plot 
plt.figure(figsize = (13,9))
plt.scatter(x = iris_df['sepal_length'], y = iris_df['petal_length'], color = 'deeppink', label = "Petal Length")
plt.scatter(x = iris_df['sepal_length'], y = iris_df['petal_width'], color = 'purple', label = "Petal Width")
plt.title("Scatter Plot", fontsize = 13)
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length / Petal Width")
plt.show()


iris_df['species'].value_counts()

plt.figure(figsize=(12,8))
sns.scatterplot(x='sepal_length', y= 'petal_length', data = iris_df, hue='species')



Pie chart

plt.figure(figsize= (8,8))
plt.pie(iris_df['species'].value_counts(), autopct='%0.2f%%', labels = ['setosa', 'versicolor', 'virginica'], 
        explode = (0, 0, 0.2))
plt.legend(loc = 2)
plt.show()

Distributional plot

# If Sample is Normally Distributed 
plt.style.use('ggplot')
plt.figure(figsize= (11,8))
sns.distplot(boston_df['MEDV'])
plt.show()

plt.style.use('ggplot')
plt.figure(figsize= (11,8))
sns.boxplot(data = iris_df)

plt.style.use('ggplot')
plt.figure(figsize= (11,8))
sns.boxplot(data = iris_df, orient='h')

plt.figure(figsize=(14,10))
sns.heatmap(boston_df.corr(), annot = True)

#Reject features which shows corr closer to 0 and extremly closer to +1 or -1 (threshold limit 0.85)



