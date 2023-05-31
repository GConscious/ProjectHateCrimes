import pandas as pd
import flake8


def main():
    df = pd.read_csv("hate_crime.csv")
    print(df)


def collin_method():
    print('hello')


if __name__ == '__main__':
    main()
