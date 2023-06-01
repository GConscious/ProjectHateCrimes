import pandas as pd
import flake8
import seaborn as sns
import matplotlib.pyplot as plt


# Line chart for number of crimes committed per year
def line_chart(df: pd.DataFrame):



def main():
    df = pd.read_csv("hate_crime.csv")
    hate_crimes = df.dropna()
    print(len(hate_crimes['state_name']))
    collin_method(df)
    hate_crimes = pd.read_csv("hate_crime.csv")
    data = hate_crimes[(hate_crimes['data_year'] >= 2010) & (hate_crimes['data_year'] <= 2021)]
    print(line_chart(hate_crimes))


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
