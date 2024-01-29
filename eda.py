import pandas as pd
import numpy as numpy
import seaborn as sns
import matplotlib.pyplot as plt
import itertools

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

# # Heatmap: correlation between vars across matrix
# heatmap = sns.heatmap(correlation, xticklabels=correlation.columns, yticklabels=correlation.columns, annot=True)
# plt.show()

# # Pairplot: array of plots for each pairs of vars in dataset
# sns.pairplot(data_nocomments)

# Scatterplot:

# Define columns for scatterplot
scatter_columns = ['Gym', 'Gym Sessions', 'Cardio (kcals from Fitbit)', 'Weekly Cardio (kcals)',
                   'Steps', 'Weekly Steps', 'Kcals out', 'Kcals in',
                   'Weekly average (kcals)', 'Net Diff (kcals)', 'Weight',
                   'Mean Weight', 'Median Weight', 'Weekly Body Weight loss %']

# Create combinations of columns
column_combinations = list(itertools.combinations(scatter_columns, 2))

# Define hue for each scatterplot
hue = 'Weight'

# Iterate through each combination and plot it
for i, (x_col, y_col) in enumerate(column_combinations):
    sns.scatterplot(x=x_col, y=y_col, hue=hue, data=data_nocomments)
    plt.show()

# plt.show()

#TODO: scatterplot for each potential grouping?