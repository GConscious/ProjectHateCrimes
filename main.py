import flake8
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


def main():
    hate_crimes = pd.read_csv("hate_crime.csv")
    income_data = pd.read_csv("income_data.csv")
    hate_crimes_filtered = hate_crimes[(hate_crimes['data_year'] >= 2010) & (hate_crimes['data_year'] <= 2021)]
    # print(num_victims_offender_race(hate_crimes_filtered))
    # victims_line_chart(hate_crimes_filtered)
    # crimes_committed_line(hate_crimes_filtered)
    # biases_pie_chart(hate_crimes_filtered)
    # hate_crimes_state_map(hate_crimes_filtered)
    # counts_vs_income_states(hate_crimes_filtered, income_data)
    # victim_bar_chart(hate_crimes_filtered)


def num_victims_offender_race(df: pd.DataFrame) -> pd.DataFrame:
    """
    num_victims_offender_race calculates the total number of victims for each
    the offender's race. Takes in df, pandas Dataframe, of the hate crime dataset
    Returns a DataFrame with the offender's race and the corresponding victim count.
    """
    collin_data = df[['victim_count', 'offender_race']].dropna()
    grouped_data = collin_data.groupby('offender_race')['victim_count'].sum().reset_index()

    return grouped_data


def victims_line_chart(df: pd.DataFrame) -> None:
    """
    victims_line_chart plots a line chart showing the total victim count from 2010 to 2021.
    Takes in df, pandas Dataframe, of the hate crime dataset. Returns None.
    """
    collin_data = df[['victim_count', 'data_year']].dropna()

    grouped_data = collin_data.groupby('data_year')['victim_count'].sum().reset_index()

    fig = px.line(grouped_data, x='data_year', y='victim_count', markers=True, text='victim_count')
    fig.update_traces(textposition='top center')
    fig.update_layout(
        xaxis=dict(tickmode='linear', tick0=0, dtick=1),
        xaxis_title='Year',
        yaxis_title='Total Victim Count',
        title='Number of Victims (2010-2021)'
    )
    fig.show()


def biases_pie_chart(df: pd.DataFrame) -> None:
    """
    biases_pie_chart creates a pie chart showing the proportion of hate crimes
    by bias type. Takes in df, pandas Dataframe, of the hate crime dataset. Returns None.
    """
    collin_data = df[['bias_desc', 'victim_count']].dropna()
    grouped_data = collin_data.groupby('bias_desc')['victim_count'].sum().reset_index()
    grouped_data['proportion'] = grouped_data['victim_count'] / grouped_data['victim_count'].sum()

    threshold = 0.005
    filtered_data = grouped_data[grouped_data['proportion'] >= threshold]

    fig = px.pie(filtered_data,
                 values='victim_count',
                 names='bias_desc',
                 title='Proportion of Hate Crimes by Bias Description')
    fig.show()


def crimes_committed_line(df: pd.DataFrame) -> None:
    """
    crimes_committed_line plots a line chart showing the number of hate crimes
    committed per year from 2010 to 2021. Takes in df, pandas Dataframe, of the hate crime dataset.
    Returns None
    """
    df = df[['data_year']].dropna()
    hate_crime_counts = df.groupby('data_year').size().reset_index(name='crime_count')
    # print(hate_crime_counts)
    fig = px.line(hate_crime_counts, x='data_year', y='crime_count',
                  title='Number of Hate Crimes by Year (2010-2021)')
    fig.show()


def hate_crimes_state_map(df: pd.DataFrame) -> None:
    """
    hate_crimes_state_map plots a heatmap showing the number of hate crimes by state.
    Takes in df, pandas Dataframe, of the hate crime dataset. Returns none.
    """
    df = df[['data_year', 'state_abbr', 'state_name']].dropna()
    hate_crime_counts = df.groupby(['state_abbr'])['data_year'].size().reset_index(name='count')
    fig = px.choropleth(
        hate_crime_counts,
        locations='state_abbr',
        locationmode='USA-states',
        color='count',
        scope='usa',
        title='Total Number of Hate Crimes by State (2010-2021)',
        labels={'count': 'Number of Crimes'},
        color_continuous_scale='Blues'
    )

    fig.show()


def counts_vs_income_states(hate_crimes: pd.DataFrame, income: pd.DataFrame) -> None:
    """
    counts_vs_income_states generates scatterplots from 2019 to 2022 comparing the
    number of hate crimes with per capita income for each state and year.
    Takes in df, pandas Dataframe, of the hate crime dataset. Returns none.
    """
    hate_filtered = hate_crimes[['data_year', 'state_abbr', 'state_name']].dropna()
    income = income[income['GeoName'] != 'United States']

    for year in range(2019, 2022):
        hate_crime_counts = hate_filtered[hate_filtered['data_year'] == year].groupby(['state_abbr']).agg(
            {'data_year': 'size', 'state_name': 'first'}).reset_index()
        hate_crime_counts = hate_crime_counts.rename(columns={'data_year': 'counts'})
        merged_df = hate_crime_counts.merge(income, left_on='state_name', right_on='GeoName')

        fig = px.scatter(merged_df, x=str(year), y='counts',
                         hover_data=['state_name'],
                         text='state_name',
                         labels={str(year): 'Per Capita Income', 'counts': 'Number of Hate Crimes'})

        fig.update_layout(title=f"Hate Crimes vs Per Capita Income ({year})")
        fig.show()


def victim_bar_chart(df: pd.DataFrame) -> None:
    """
    victim_bar_chart plots a bar chart that displays total hate crimes by victim type.
    Takes in df, pandas Dataframe, of the hate crime dataset. Returns none.
    """
    df = df[df['victim_types'].isin(['Individual', 'Other', 'Business', 'Government',
                                     'Religious Organization', 'Society/Public',
                                     'Business;Individual', 'Unknown'])]
    counts = df['victim_types'].value_counts()

    plt.figure(figsize=(10, 6))
    counts.plot(kind='bar', color='blue')
    plt.xlabel('Victim Types')
    plt.ylabel('Total Hate Crimes')
    plt.title('Total Hate Crimes by Victim Types')

    plt.show()


if __name__ == '__main__':
    main()
