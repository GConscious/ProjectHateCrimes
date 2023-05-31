import pandas as pd
import flake8
import seaborn as sns


# Line chart for number of crimes committed per year
def line_chart():
    print('start')


def main():
    df = pd.read_csv("hate_crime.csv")
    print(df['state_name'])


def collin_method():
    pass


if __name__ == '__main__':
    main()
