import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import EDA_functions as eda
import csv
import string

sample_10m = '../data/10m_sample_common_passwords/10-million-combos.txt'
pwned_path = '../data/have_i_been_pwned_v4/been_pwned_v4_hash_plain.txt'
linkedin_path = '../data/linkedin_leak/linkedin_hash_plain.txt'
linkedin_test_file = '../data/linkedin_leak/test_write.txt'
rockyou_path = '../data/rockyou_leak/rockyou_copy.txt'

test_read = '../data/10m_sample_common_passwords/test_read.txt'
test_write = '../data/test_write.txt'


if __name__ == '__main__':
    '''10m_sample'''
    df_10msample = pd.read_csv(sample_10m, header=None, sep='\t').astype(str)
    df_10msample.columns = ['username', 'password']
    df_10msample.drop('username', axis=1, inplace=True)
    df_10msample['length'] = df_10msample['password'].apply(len)

    df_10msample['class'] = df_10msample['password'].apply(eda.class_count)
    class_split = df_10msample['class'].str.split(pat=',', expand=True)
    df_10msample['upper'] = class_split[0]
    df_10msample['lower'] = class_split[1]
    df_10msample['number'] = class_split[2]
    df_10msample['symbol'] = class_split[3]

    print(df_10msample.head(10))

    # fig1 = plt.figure()
    # ax1 = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
    # ax1.hist(df_10msample['length'])
    # plt.show()




    '''rockyou EDA'''
    # df_rockyou = pd.read_csv(rockyou_path, sep='\n')

    '''pwned EDA'''
    # df_pwned = pd.read_csv(pwned_path, header=None, sep='\n', columns='password').astype(str)
    # df_pwned[0] = df_pwned[0].str.split(pat=':',n=1)
    # eda.explore_df(df_pwned)
    
    '''linkedin EDA'''
    # df_linkedin = pd.read_csv(linkedin_path, header=None, sep='\n')

