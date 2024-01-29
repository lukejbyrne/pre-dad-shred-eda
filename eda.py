import pandas as pd
import numpy as numpy
import seaborn as sns
import matplotlib.pyplot as plt

#0 Load data
data = pd.read_csv('data.csv')

#1 Understanding the data
print("Understanding the data")
print("----------------------")

print(data.head())
print(data.tail())
print(data.describe())
print(data.shape)
print(data.columns)
print(data.nunique())
print(data['Gym'].unique())

print("-------------------------")

#2 Cleaning the data
print("Cleaning the data")
print("-----------------")

print(data.isnull().sum())
#TODO: For next qnalysis update table to have weekly avg filled in (no NaN) or remove, probably one of each
#       - Change empty gym to 'None'
#       - Any weekly average to be back filled
#       - 
#       - 

print("-------------------------")

# Remove unnecessary columns
data_nocomments = data.drop(['Comments'], axis=1)

#TODO: Check and remove outliers

#3 Relationship Analysis
# Correlation Matrix
correlation = data_nocomments.corr()

# Heatmap: correlation between vars across matrix
# heatmap = sns.heatmap(correlation, xticklabels=correlation.columns, yticklabels=correlation.columns, annot=True)
# plt.show()

# # Pairplot: array of plots for each pairs of vars in dataset
# sns.pairplot(data_nocomments)

# Scatterplot:
# sns.relplot(x='Cardio (kcals from Fitbit)', y='Median Weight', hue='Gym', data=data_nocomments) # bad result
# sns.relplot(x='Cardio (kcals from Fitbit)', y='Weight', hue='Gym', data=data_nocomments) # bad result? linear
# sns.relplot(x='Cardio (kcals from Fitbit)', y='Weight', hue='Steps', data=data_nocomments) # bad result? linear
# sns.relplot(x='Kcals in', y='Weight', hue='Gym', data=data_nocomments) # linear relationship at calories
# sns.relplot(x='Kcals in', y='Weight', hue='Steps', data=data_nocomments) # linear relationship at calories
# sns.relplot(x='Kcals in', y='Weight', hue='Cardio (kcals from Fitbit)', data=data_nocomments) # linear relationship at calories
# sns.relplot(x='Kcals in', y='Weight', hue='Cardio (kcals from Fitbit)', data=data_nocomments) # linear relationship at calories
# sns.relplot(x='Kcals in', y='Weight', hue='Weight', data=data_nocomments) # linear relationship at calories