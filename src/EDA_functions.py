import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import string

def stringify_row(row: str):
    row_split = row.replace(':', ' ').split()
    return row_split

def stringify_rows(data: list):
    return map(stringify_row, data)

def chunk_to_csv(*, file_in: str, file_out: str, chunksize:int=10000):
    reader = pd.read_csv(file_in, chunksize=chunksize, sep=',')
    for chunk in reader:
        result = chunk
        result.to_csv(file_out, mode='a', index=False, header=False)

def text_to_csv():
    with open(test_write, 'w') as writer:
        with open(test_read, 'r') as data:
            # csvwriter = csv.writer(writer)
            # csvwriter.writerow(data)
            iter = 1
            for line in data:
                # line = line.split('\t')
                # print(line)
                # datum = str( line.split('\t') ) + ',' + '\n'
                # print(datum[0])
                # print(datum)
                writer.write(str( line.replace('\n', '').split('\t') ) + ',' + '\n')
                if iter > 20:
                    break
                iter += 1

def explore_df(df: pd.DataFrame):
    print(df.info(), '\n',
    df.describe(), '\n',
    df.columns, '\n',
    df.head(10), '\n',
    )

def class_count(password: str):
    lower = set(string.ascii_lowercase)
    upper = set(string.ascii_uppercase)
    number = set(string.digits)
    symbol = set(string.punctuation)
    count_dict = {
        'lower': 0,
        'upper': 0,
        'number': 0,
        'symbol': 0
    }

    for char in password:
        if char in upper:
            count_dict['upper'] += 1
        elif char in lower:
            count_dict['lower'] += 1
        elif char in number:
            count_dict['number'] += 1
        else:
            count_dict['symbol'] += 1

    return f"{count_dict['upper']},{count_dict['lower']},{count_dict['number']},{count_dict['symbol']}"

if __name__ == '__main__':
    pass



