import pandas as pd
import numpy as numpy
import seaborn as sns
import matplotlib.pyplot as plt
import itertools
import re
import os

# Toggle used to know whether the data is daily or weekly
time_toggle = ''

def main(data, original_data):

    while True:
        print("Please enter: \n1  - Understand Data\n2a - Clean (daily)\n2b - Clean Data (weekly)\n3  - Relationship Analysis - Heatmap\n4  - Relationship Analysis - Pairplot\n5  - Relationship Analysis - Scatterplot\nr  - Reset data\nq  - Quit")
        user_input = input()
        global time_toggle

        if user_input == 'q':
            print("Exiting...")
            break  # Exit the loop if the user enters 'q'

        if user_input == '1':
            print("You entered 1")
            understand(data)
        elif user_input == '2a':
            print("You entered 2")
            time_toggle = 'Daily'
            data = clean(data, user_input)            
        elif user_input == '2b':
            print("You entered 2")
            time_toggle = 'Weekly'
            data = clean(data, user_input)
        elif user_input == '3':
            print("You entered 3")
            heatmap(data)
        elif user_input == '4':
            print("You entered 4")
            pairplot(data)
        elif user_input == '5':
            print("You entered 5")
            scatterplot(data)
        elif user_input == 'r':
            print("You entered r")
            data = original_data
        else:
            print("Invalid input. Please enter 1, 2, 3, 4 or 5.")

def understand(data):
    #1 Understanding the data
    print("Understanding the data")
    print("----------------------")

    try:
        print(data.head())
        print(data.tail())
        print(data.describe())
        print(data.shape)
        print(data.columns)
        print(data.nunique())
        print(data['Gym'].unique())

    except Exception as error:
        print("An exception occurred:", error)

    print("-------------------------")

def clean(data, user_input):
    #2 Cleaning the data
    print("Cleaning the data")
    print("-----------------")

    try:
        print(data.isnull().sum())

        # Remove unnecessary columns
        data = data.drop(['Comments'], axis=1)

        columns = data.columns.values.tolist()

        weekly_cols = []

        # Remove columns that include week
        for i in columns:
            if re.search('week', i, re.IGNORECASE) or re.search('median', i, re.IGNORECASE) or re.search('mean', i, re.IGNORECASE):
                weekly_cols.append(i)

        # Make a daily column list
        if(user_input == "2a"):
            data = data.drop(weekly_cols, axis=1)
        # Make a weekly column list
        elif(user_input == "2b"):
            data = data[weekly_cols]

    except Exception as error:
        print("An exception occurred:", error)

    print("New Cols:", weekly_cols)
    print("-------------------------")

    return data

#3 Relationship Analysis
def heatmap(data):
    # Correlation Matrix
    correlation = data.corr()

    # Heatmap: correlation between vars across matrix
    heatmap = sns.heatmap(correlation, xticklabels=correlation.columns, yticklabels=correlation.columns, annot=True)
    plt.tight_layout()
    # Create 'weekly' / 'daily' directory if it doesn't exist
    os.makedirs(time_toggle, exist_ok=True)
    plt.savefig("{}/Heatmap.png".format(time_toggle))

def pairplot(data):
    # Pairplot: array of plots for each pairs of vars in dataset
    sns.pairplot(data)
    plt.tight_layout()
    plt.savefig("{}/Pairplot.png".format(time_toggle))

def scatterplot(data):
    # Scatterplot:

    # Define columns for scatterplot
    columns = data.columns.values.tolist()

    # Create combinations of columns
    column_combinations = list(itertools.combinations(columns, 3))

    # Create 'weekly' / 'daily' directory if it doesn't exist
    os.makedirs(time_toggle, exist_ok=True)

    # Iterate through each combination and plot it
    for i, (x_col, y_col, hue) in enumerate(column_combinations):
        plt.figure() 
        sns.scatterplot(x=x_col, y=y_col, hue=hue, data=data)
        plt.tight_layout()
        os.makedirs('{}/{}'.format(time_toggle,hue), exist_ok=True)
        plt.savefig("{}/{}/Figure{}.png".format(time_toggle, hue, plt.gcf().number))

    #TODO: wheres my date column gone for looking across time? and then graphs / plots

if __name__ == "__main__":
     #0 Load data
    data = pd.read_csv('data.csv')
    original_data = pd.read_csv('data.csv')
    
    main(data, original_data)