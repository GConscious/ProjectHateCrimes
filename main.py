import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


# Line chart for number of crimes committed per year


def main():
    hate_crimes = pd.read_csv("hate_crime.csv")
    income_data = pd.read_csv("income_data.csv")
    hate_crimes_filtered = hate_crimes[(hate_crimes['data_year'] >= 2010) & (hate_crimes['data_year'] <= 2021)]
    print(num_victims_offender_race(hate_crimes_filtered))
    victims_line_chart(hate_crimes_filtered)
    crimes_committed_line(hate_crimes_filtered)
    biases_pie_chart(hate_crimes_filtered)
    hate_crimes_state_map(hate_crimes_filtered)
    counts_vs_income_states(hate_crimes_filtered, income_data)
    victim_bar_chart(hate_crimes_filtered)

# Victims based on offender race

def num_victims_offender_race(df: pd.DataFrame) -> pd.DataFrame:
    collin_data = df[['victim_count', 'offender_race']].dropna()
    grouped_data = collin_data.groupby('offender_race')['victim_count'].sum().reset_index()

    return grouped_data


# Line chart number of victims per year
def victims_line_chart(df: pd.DataFrame) -> None:
    collin_data = df[['victim_count', 'data_year']].dropna()

    grouped_data = collin_data.groupby('data_year')['victim_count'].sum().reset_index()

    fig = px.line(grouped_data, x='data_year', y='victim_count', markers=True, text='victim_count')
    fig.update_traces(textposition='top center')
    fig.update_layout(
        xaxis=dict(tickmode='linear', tick0=0, dtick=1),
        xaxis_title='Year',
        yaxis_title='Total Victim Count',
        title='Victim Count Over the Years'
    )
    fig.show()


# Pie chart for biases.
def biases_pie_chart(df: pd.DataFrame) -> None:
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


# Line chart for number of crimes committed per year
def crimes_committed_line(df: pd.DataFrame) -> None:
    df = df[['data_year']].dropna()
    hate_crime_counts = df.groupby('data_year').size().reset_index(name='crime_count')
    # print(hate_crime_counts)
    fig = px.line(hate_crime_counts, x='data_year', y='crime_count',
                  title='Number of Hate Crimes by Year (2010-2021)')
    fig.show()


# Heatmap displays number of hate crimes by state
def hate_crimes_state_map(df: pd.DataFrame) -> None:
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


# Plots 3 scatterplots showing amount of hate crimes versus per capita income for each state
def counts_vs_income_states(hate_crimes: pd.DataFrame, income: pd.DataFrame) -> None:
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


# Plots bar chart of the number of hate crimes by victim types.
def victim_bar_chart(df: pd.DataFrame) -> None:
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
