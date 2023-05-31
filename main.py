import pandas as pd
import flake8
import seaborn as sns
import matplotlib as plt


# Line chart for number of crimes committed per year
def line_chart():
    print('start')


def main():
    df = pd.read_csv("hate_crime.csv")
    # print(df)
    return df
    print(df['state_name'])


def collin_method(df: pd.DataFrame):
    grouped_data = df.groupby('bias_desc')['victim_count'].sum()
    return grouped_data


if __name__ == '__main__':
    main()
    print(collin_method(main()))
