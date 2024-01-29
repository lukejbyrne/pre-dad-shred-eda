import pandas as pd
import numpy as numpy
import seaborn as sns
import matplotlib.pyplot as plt
import itertools

def main():
    #0 Load data
    data = pd.read_csv('data.csv')
    original_data = pd.read_csv('data.csv')

    while True:
        print("Please enter: \n1 - Understand Data\n2 - Clean Data\n3 - Relationship Analysis - Heatmap\43 - Relationship Analysis - Pairplot\n5 - Relationship Analysis - Scatterplot\n6 - Reset data\nq - Quit")
        user_input = input()

        if user_input == 'q':
            print("Exiting...")
            break  # Exit the loop if the user enters 'q'

        if user_input == '1':
            print("You entered 1")
            understand(data)
        elif user_input == '2':
            print("You entered 2")
            data = clean(data)
        elif user_input == '3':
            print("You entered 3")
            heatmap(data)
        elif user_input == '4':
            print("You entered 4")
            pairplot(data)
        elif user_input == '5':
            print("You entered 5")
            scatterplot(data)
        elif user_input == '6':
            print("You entered 6")
            data = original_data
        else:
            print("Invalid input. Please enter 1, 2, 3, 4 or 5.")

def understand(data):
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

def clean(data):
    #2 Cleaning the data
    print("Cleaning the data")
    print("-----------------")

    try:
        print(data.isnull().sum())

        # Remove unnecessary columns
        data = data.drop(['Comments'], axis=1)

        #TODO: Check and remove outliers
    except Exception as error:
        print("An exception occurred:", error)

    print("-------------------------")

    return data

#3 Relationship Analysis
def heatmap(data):
    # Correlation Matrix
    correlation = data.corr()

    # Heatmap: correlation between vars across matrix
    heatmap = sns.heatmap(correlation, xticklabels=correlation.columns, yticklabels=correlation.columns, annot=True)
    plt.show()

def pairplot(data):
    # Pairplot: array of plots for each pairs of vars in dataset
    sns.pairplot(data)
    plt.show()

def scatterplot(data):
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
        plt.figure() 
        sns.scatterplot(x=x_col, y=y_col, hue=hue, data=data)

    plt.show()

    #TODO: wheres my date column gone for looking across time?

if __name__ == "__main__":
    main()