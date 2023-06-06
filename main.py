import pandas as pd
import flake8
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# Line chart for number of crimes committed per year


def main():
    hate_crimes = pd.read_csv("hate_crime.csv")
    income_data = pd.read_csv("income_data.csv")
    data = hate_crimes[(hate_crimes['data_year'] >= 2010) & (hate_crimes['data_year'] <= 2021)]
    # mykyt_method(data)
    # amrith_map(data)
    # amrith_compare_income(data, income_data)
    # amrith_line_chart(data)
    # collin_method1(data)
    # collin_method2(data)
    # collin_method3(data)
    # collin_method4(data)


def collin_method1(df: pd.DataFrame):
    collin_data = df[['victim_count', 'offender_race']].dropna()
    grouped_data = collin_data.groupby('offender_race')['victim_count'].sum().reset_index()

    print(grouped_data)


def collin_method2(df: pd.DataFrame):
    collin_data = df[['victim_count', 'data_year']].dropna()

    grouped_data = collin_data.groupby('data_year')['victim_count'].sum().reset_index()

    fig = px.line(grouped_data, x='data_year', y='victim_count')
    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='Total Victim Count',
        title='Victim Count Over the Years'
    )
    fig.show()


def collin_method3(df: pd.DataFrame):
    collin_data = df[['state_abbr', 'victim_count']].dropna()
    grouped_data = collin_data.groupby('state_abbr')['victim_count'].sum().reset_index()

    fig = px.choropleth(
        grouped_data,
        locations='state_abbr',
        locationmode='USA-states',
        color='victim_count',
        scope='usa',
        color_continuous_scale='Greens',
        labels={'victim_count': 'Total Victim Count'})
    fig.update_layout(title='Hate Crimes by State Heatmap')

    fig.show()


def collin_method4(df: pd.DataFrame):
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


def amrith_line_chart(df: pd.DataFrame):
    df = df[['data_year']].dropna()
    hate_crime_counts = df.groupby('data_year').size().reset_index(name='crime_count')

    fig = px.line(hate_crime_counts, x='data_year', y='crime_count',
                  title='Number of Hate Crimes by Year')
    fig.show()


def amrith_map(df: pd.DataFrame):
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


def amrith_compare_income(hate_crimes, income):
    hate_filtered = hate_crimes[['data_year', 'state_abbr', 'state_name']].dropna()
    income = income[income['GeoName'] != 'United States']

    for year in range(2017, 2021):
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


def mykyt_method(df: pd.DataFrame) -> None:
    df = df[['victim_count', 'state_abbr']].dropna()
    state_victim_counts = df.groupby('state_abbr')['victim_count'].sum().reset_index()
    # Create a choropleth map using plotly.express
    fig = px.choropleth(
        state_victim_counts,
        locations='state_abbr',
        locationmode='USA-states',
        color='victim_count',
        color_continuous_scale='YlOrRd',
        labels={'victim_count': 'Victim Count'},
        title='Victim Count across US (2010-2021)'
    )
    fig.update_layout(
        geo_scope='usa',
        height=600,
        width=800
    )
    fig.show()


def mykyt_method_2(df: pd.DataFrame) -> None:
    df = df[df['victim_types'].isin(['Individual', 'Other', 'Business', 'Government',
                                     'Religious Organization', 'Society/Public',
                                     'Business;Individual', 'Unknown'])]
    counts = df['victim_types'].value_counts()

    # Plot the bar graph
    plt.figure(figsize=(10, 6))
    counts.plot(kind='bar', color='blue')
    plt.xlabel('Victim Types')
    plt.ylabel('Total Hate Crimes')
    plt.title('Total Hate Crimes by Victim Types')

    # Show the plot
    plt.show()


if __name__ == '__main__':
    main()
