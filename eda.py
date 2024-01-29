import pandas as pd
import numpy as numpy
import seaborn as sns

# Load data
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

# Cleaning the data
print("Cleaning the data")
print("-----------------")

print(data.isnull().sum())
#TODO: For next qnalysis update table to have weekly avg filled in (no NaN) or remove, probably one of each
#       - Change empty gym to 'None'
#       - Any weekly average to be back filled
#       - 
#       - 

print("-------------------------")
