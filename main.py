import pandas as pd
import flake8
import seaborn as sns
import matplotlib.pyplot as plt


# Line chart for number of crimes committed per year
def line_chart(df: pd.DataFrame):
    pass


def main():
    hate_crimes = pd.read_csv("hate_crime.csv")
    data = hate_crimes[(hate_crimes['data_year'] >= 2010) & (hate_crimes['data_year'] <= 2021)]
    collin_method(data)
    print(collin_method(data))


def collin_method1(df: pd.DataFrame):
    collin_data = df[['victim_count', 'offender_race']].dropna()
    grouped_data = collin_data.groupby('offender_race')['victim_count'].mean()

    mean_data = pd.DataFrame({'offender_race': grouped_data.index, 'victim_count': grouped_data.values})

    sns.barplot(data=mean_data, x='offender_race', y='victim_count')
    plt.xlabel("Offender's Race")
    plt.ylabel('Total Victim Count (Thousands)')
    plt.title('Victim Count by Offender\'s Race')
    plt.xticks(rotation=90)
    plt.show()


if __name__ == '__main__':
    main()
