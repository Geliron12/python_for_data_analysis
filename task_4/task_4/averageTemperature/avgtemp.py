import argparse
import pandas as pd
from typing import Union

def avg_year_city(filename: str, date: str, city: str, year: str) -> Union[None, float]:
    if filename[-4:] != '.csv':
        print('This is not a csv file!')
        return None
    try:
        data_df: pd.DataFrame = pd.read_csv(filename, parse_dates=[date])
    except FileNotFoundError:
        print('No such file!')
        return None
    if city not in data_df['city'].values:
        print('This city is not presented!')
        return None
    data_df['year'] = data_df[date].apply(lambda x: x.year)
    if year not in data_df['year'].values:
        print('This year is not presented!')
        return None
    return(data_df[data_df['year'] == year].groupby('city')['AverageTemperature'].mean()[city])

def main():

    parser = argparse.ArgumentParser(description='Returns mean value of temperature in given city in given year in given csv file')
    parser.add_argument('filename', type=str, help='a csv file with input')
    parser.add_argument('date', type=str, help='name of column for dates')
    parser.add_argument('city', type=str, help='name of city')
    parser.add_argument('year', type=int, help='chosen year')

    args = parser.parse_args()
    avg_year_city(args.filename, args.date, args.city, args.year)

if __name__ == '__main__':
    main()
