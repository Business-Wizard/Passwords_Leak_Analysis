import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import csv

def stringify_row(row: str):
    return row.replace(':', ' ').split()

def stringify_rows(data: list):
    return list( map(stringify_row, data)  )


def correct_linkedin(filepath: str, nrows: int=1000):
    """
    open filepath as reader
    chunk processing
    stringify_rows()
    
    """
    with open(filepath) as data1:
        for __ in range(nrows):
            datum = data1.readline()
            corrected = stringify_row(datum)


if __name__ == '__main__':
    # data_linkedin = rows_to_list(filepath='../data/linkedin_leak/linkedin_hash_plain.txt', nrows=1000)
    # data_linkedin = stringify_rows(data_linkedin)

    # data_linkedin = pd.DataFrame(data_linkedin)
    # print(data_linkedin.head(5) )

    # save_csv(filepath='../data/linkedin_leak/tester1.txt', data=data_linkedin)
    linkedin_path = '../data/linkedin_leak/linkedin_hash_plain.txt'
    correct_linkedin(linkedin_path)


    # TODO create string deliminaters 
    # TODO data_linkedin = pd.read_csv('../data/linkedin_leak/linkedin_hash_plain.txt')
    # data_10m_sample = pd.read_csv('../data/10m_sample_common_passwords/10m_combos.txt')
    # data_rockyou = pd.read_csv('../data/rockyou_leak/rockyou.txt')
    # !huge-file data_pwned_v6 = pd.read_csv('../data/pwned_passwords_v6/pwned_ordered_v6.txt', nrows=1000000)
