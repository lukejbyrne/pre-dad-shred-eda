import pandas as pd

def main(df, original_df):
    print(df.head())
    df = pd.to_numeric(df['Date'], errors='coerce')
    print(df.head())

if __name__ == "__main__":
    #0 Load data
    df = pd.read_csv('data.csv')
    original_df = pd.read_csv('data.csv')
    
    main(df, original_df)