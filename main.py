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


def collin_method(df: pd.DataFrame):
    collin_data = df[['victim_count', 'offender_race']].dropna()
    # filtered_data = collin_data[collin_data >= 100]

    sns.catplot(data=collin_data, kind="bar", x="offender_race", y="victim_count")
    plt.xlabel("Offender's Race")
    plt.ylabel('Total Victim Count')
    plt.title('Victim Count by Bias Description')

    # Display the chart
    plt.show()


if __name__ == '__main__':
    main()
