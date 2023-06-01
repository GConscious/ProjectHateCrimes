import pandas as pd
import flake8
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# Line chart for number of crimes committed per year
def line_chart(df: pd.DataFrame):
    pass


def main():
    hate_crimes = pd.read_csv("hate_crime.csv")
    data = hate_crimes[(hate_crimes['data_year'] >= 2010) & (hate_crimes['data_year'] <= 2021)]
    collin_method1(data)
    collin_method2(data)


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


def collin_method2(df: pd.DataFrame):
    collin_data = df[['victim_count', 'data_year']].dropna()

    # Calculate total victim count by year
    grouped_data = collin_data.groupby('data_year')['victim_count'].sum().reset_index()

    # Create a line plot using Plotly
    fig = px.line(grouped_data, x='data_year', y='victim_count')
    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='Total Victim Count',
        title='Victim Count Over the Years'
    )
    fig.show()


if __name__ == '__main__':
    main()
