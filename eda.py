import pandas as pd
import numpy as numpy
import seaborn as sns
import matplotlib.pyplot as plt
import itertools
import re
import os

#TODO: Remove code duplication

# Toggle used to know whether the data is daily or weekly
time_toggle = ''

def main(df, original_df):

    while True:
        print("Please enter: \n1  - Understand Data\n2a - Clean (daily)\n2b - Clean Data (weekly)\n3  - Relationship Analysis - Heatmap\n4  - Relationship Analysis - Pairplot\n5  - Relationship Analysis - Scatterplot\n6  - Relationship Analysis - Histogram\n7  - Relationship Analysis - Catplot\nr  - Reset data\nq  - Quit")
        user_input = input()
        global time_toggle

        if user_input == 'q':
            print("Exiting...")
            break
        elif user_input == '1':
            print("You entered 1")
            understand(df)
        elif user_input == '2a':
            print("You entered 2")
            time_toggle = 'Daily'
            df = clean(df, user_input)            
        elif user_input == '2b':
            print("You entered 2")
            time_toggle = 'Weekly'
            df = clean(df, user_input)
        elif user_input == '3':
            print("You entered 3")
            heatmap(df)
        elif user_input == '4':
            print("You entered 4")
            pairplot(df)
        elif user_input == '5':
            print("You entered 5")
            scatterplot(df)        
        elif user_input == '6':
            print("You entered 6")
            histogram(df)
        elif user_input == '7':
            print("You entered 7")
            catplot(df)
        elif user_input == 'r':
            print("You entered r")
            df = original_df
        else:
            print("Invalid input. Please try again.")

def understand(df):
    #1 Understanding the data
    print("Understanding the data")
    print("----------------------")

    try:
        print(df.head())
        print(df.tail())
        print(df.describe())
        print(df.shape)
        print(df.columns)
        print(df.nunique())
        print(df['Gym'].unique())

    except Exception as error:
        print("An exception occurred:", error)

    print("-------------------------")

def clean(df, user_input):
    #2 Cleaning the data
    print("Cleaning the data")
    print("-----------------")

    try:
        print(df.isnull().sum())

        # Remove unnecessary columns
        df = df.drop(['Comments'], axis=1)

        columns = df.columns.values.tolist()

        weekly_cols = []

        # Remove columns that include week
        for i in columns:
            if re.search('week', i, re.IGNORECASE) or re.search('median', i, re.IGNORECASE) or re.search('mean', i, re.IGNORECASE):
                weekly_cols.append(i)

        # Make a daily column list
        if(user_input == "2a"):
            df = df.drop(weekly_cols, axis=1)
        # Make a weekly column list
        elif(user_input == "2b"):
            df = df[weekly_cols]

    except Exception as error:
        print("An exception occurred:", error)

    print("New Cols:", weekly_cols)
    print("-------------------------")

    return df

#3 Relationship Analysis
def heatmap(df):
    # Correlation Matrix
    correlation = df.corr()

    # Heatmap: correlation between vars across matrix
    heatmap = sns.heatmap(correlation, xticklabels=correlation.columns, yticklabels=correlation.columns, annot=True)
    plt.tight_layout()

    # Create 'weekly' / 'daily' directory if it doesn't exist
    os.makedirs(time_toggle, exist_ok=True)
    os.makedirs('{}/Heatmap'.format(time_toggle), exist_ok=True)
    plt.savefig("{}/Heatmap/Figure{}.png".format(time_toggle, plt.gcf().number))

def pairplot(df):
    # Pairplot: array of plots for each pairs of vars in dataset
    sns.pairplot(df)
    plt.tight_layout()
    os.makedirs('{}/Pairplot'.format(time_toggle), exist_ok=True)
    plt.savefig("{}/Pairplot/Figure{}.png".format(time_toggle, plt.gcf().number))

def scatterplot(df):
    # Define columns
    columns = df.columns.values.tolist()

    # Create combinations of columns
    column_combinations = list(itertools.combinations(columns, 2))

    # Create 'weekly' / 'daily' directory if it doesn't exist
    os.makedirs(time_toggle, exist_ok=True)
    
    # Iterate through each combination and plot it
    for i in columns:
        for j, (x_col, y_col) in enumerate(column_combinations):
            if i != x_col and i != y_col:
                print(f"{i} ----- {x_col} ----- {y_col}")
                plt.figure() 
                sns.scatterplot(x=x_col, y=y_col, hue=i, data=df)
                plt.tight_layout()
                os.makedirs('{}/Scatterplot/{}'.format(time_toggle,i), exist_ok=True)
                plt.savefig("{}/Scatterplot/{}/Figure{}.png".format(time_toggle, i, plt.gcf().number))

def histogram(df):
    # Define columns
    columns = df.columns.values.tolist()

    for i in columns:
        plt.figure() 
        sns.displot(df[i])
        plt.tight_layout()
        os.makedirs('{}/Histogram/{}'.format(time_toggle,i), exist_ok=True)
        plt.savefig("{}/Histogram/{}/Figure{}.png".format(time_toggle, i, plt.gcf().number))

def catplot(df):
    # Define columns
    columns = df.columns.values.tolist()

    for i in columns:
        plt.figure() 
        sns.catplot(x=i, kind = 'box', data=df)
        plt.tight_layout()
        os.makedirs('{}/Catplot/{}'.format(time_toggle,i), exist_ok=True)
        plt.savefig("{}/Catplot/{}/Figure{}.png".format(time_toggle, i, plt.gcf().number))

if __name__ == "__main__":
    #0 Load data
    df = pd.read_csv('data.csv')
    original_df = pd.read_csv('data.csv')
    
    main(df, original_df)