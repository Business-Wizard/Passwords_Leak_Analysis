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


if __name__ == '__main__':
    '''10m_sample'''
    # fig1 = plt.figure()
    # ax1 = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
    # ax1.hist(df_10msample['length'])
    # plt.show()


    '''rockyou EDA'''
    

    '''pwned EDA'''
    
    # df_pwned[0] = df_pwned[0].str.split(pat=':',n=1)
    # eda.explore_df(df_pwned)
    
    '''linkedin EDA'''
    
