import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import EDA_functions as eda


if __name__ == '__main__':
    linkedin_path = 'data/linkedin_leak/linkedin_hash_plain.txt'
    # sample_10m_path = 'data/10m_sample_common_passwords/10-million-combos.txt'
    write_path = '../data/linkedin_leak/tester1.txt'

    reader = pd.read_csv(linkedin_path, chunksize=1000)
    print(reader.__next__() )

    # reader10m = pd.read_csv(sample_10m_path,sep='\t', header=None, chunksize=200000)
    # * Successful
    # ? how to detect difference in data?
    # for chunk in reader10m:
        # chunk.to_csv('test_write.csv', mode='a')





