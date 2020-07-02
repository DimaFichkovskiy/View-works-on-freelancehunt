import pandas as pd
import argparse

df = pd.read_csv('freelancehunt.csv', names=['date', 'title', 'url'])

parser = argparse.ArgumentParser(description='View works on a freelancehunt')
parser.add_argument('date_from', type=str)
args = parser.parse_args()


def get_data(date_from):
    return df[df.date == date_from][['title', 'url']]


if __name__ == '__main__':
    print(get_data(args.date_from))