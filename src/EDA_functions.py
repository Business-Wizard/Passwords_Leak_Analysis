import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import csv

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


if __name__ == '__main__':
    pass



