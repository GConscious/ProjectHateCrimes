import pandas as pd
import flake8
import seaborn as sns
import matplotlib as plt


# Line chart for number of crimes committed per year
def line_chart(df: pd.DataFrame):
    pass


def main():
    df = pd.read_csv("hate_crime.csv")
    hate_crimes = df.dropna()
    print(len(hate_crimes['state_name']))
    print(collin_method(df))


def collin_method(df: pd.DataFrame):
    collin_data = df[['victim_count', 'bias_desc']].dropna()
    grouped_data = collin_data.groupby('bias_desc')['victim_count'].sum()
    return grouped_data


if __name__ == '__main__':
    main()
