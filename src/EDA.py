import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import EDA_functions as eda
import string
from pyspark.sql import SparkSession



if __name__ == '__main__':
    linkedin_path = '../data/linkedin_leak/linkedin_hash_plain.txt'
    linkedin_test_file = '../data/linkedin_leak/test_write.txt'
    test_read = '../data/10m_sample_common_passwords/test_read.txt'
    test_write = '../data/test_write.txt'
    sample_10m = '../data/10m_sample_common_passwords/10-million-combos.txt'
    rockyou_path = '../data/rockyou_leak/rockyou_copy.txt'
    pwned_path = '../data/have_i_been_pwned_v4/been_pwned_v4_hash_plain.txt'


    # df_linkedin = pd.read_csv(linkedin_path, header=None, sep='\n')
    # df_rockyou = pd.read_csv(rockyou_path, sep='\n')

    '''pwned EDA'''
    df_pwned = pd.read_csv(pwned_path, header=None, sep='\n', columns='password').astype(str)
    df_pwned[0] = df_pwned[0].str.split(pat=':',n=1)
    # eda.explore_df(df_pwned)



    '''10m_sample'''
    # df_10msample = pd.read_csv(sample_10m, header=None, sep='\t').astype(str)
    # df_10msample.columns = ['username', 'password']
    # eda.explore_df(df_10msample)
    # df_10msample['length'] = df_10msample['password'].apply(len)
    # print(df_10msample.tail(10))
    # print( df_10msample.unique() )
    


