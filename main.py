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
    collin_method3(data)
    collin_method4(data)


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


def collin_method3(df: pd.DataFrame):
    collin_data = df[['state_abbr', 'victim_count']].dropna()

    # Calculate total victim count by state
    grouped_data = collin_data.groupby('state_abbr')['victim_count'].sum().reset_index()

    # Create a heat map using Plotly with green and blue color scale
    fig = px.choropleth(grouped_data, locations='state_abbr', locationmode='USA-states', color='victim_count',
                        scope='usa', color_continuous_scale='Greens', labels={'victim_count': 'Total Victim Count'})

    fig.update_layout(title='Hate Crimes by State Heatmap')

    fig.show()


def collin_method4(df: pd.DataFrame):
    collin_data = df[['bias_desc', 'victim_count']].dropna()

    # Calculate total victim count by bias description
    grouped_data = collin_data.groupby('bias_desc')['victim_count'].sum().reset_index()

    # Calculate proportion of victim count
    grouped_data['proportion'] = grouped_data['victim_count'] / grouped_data['victim_count'].sum()

    # Set threshold for excluding categories with low proportions
    threshold = 0.005

    # Filter out categories below the threshold
    filtered_data = grouped_data[grouped_data['proportion'] >= threshold]

    # Create a pie chart using Plotly
    fig = px.pie(filtered_data, values='victim_count', names='bias_desc',
                 title='Proportion of Hate Crimes by Bias Description')
    fig.show()




# sum of victim count across us by state since 2010
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

if __name__ == '__main__':
    main()
