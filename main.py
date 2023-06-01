import pandas as pd
import flake8
import seaborn as sns
import matplotlib as plt


# Line chart for number of crimes committed per year
def line_chart(df: pd.DataFrame):



def main():
    hate_crimes = pd.read_csv("hate_crime.csv")
    data = hate_crimes[(hate_crimes['data_year'] >= 2010) & (hate_crimes['data_year'] <= 2021)]
    # print(collin_method(hate_crimes))
    print(line_chart(hate_crimes))


def collin_method(df: pd.DataFrame):
    collin_data = df[['victim_count', 'bias_desc']].dropna()
    grouped_data = collin_data.groupby('bias_desc')['victim_count'].sum()
    return grouped_data


if __name__ == '__main__':
    main()
