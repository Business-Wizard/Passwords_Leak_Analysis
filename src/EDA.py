import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import EDA_functions as eda

sample_10m = '../data/10m_sample_common_passwords/10m_standard_complete2.csv'
pwned_path = '../data/have_i_been_pwned_v4/been_pwned_v4_hash_plain.txt'
linkedin_path = '../data/linkedin_leak/linkedin_hash_plain.txt'
linkedin_test_file = '../data/linkedin_leak/test_write.txt'
rockyou_path = '../data/rockyou_leak/rockyou_copy.txt'


if __name__ == '__main__':
    '''10m_sample'''
    df_10msample = pd.read_csv(sample_10m).sample(frac=0.01)
    # eda.explore_df(df_10msample)
    # pd.plotting.scatter_matrix(frame=df_10msample)
    
    eda.plot_guess_length(df_10msample)
    
    # fig1 = plt.figure()
    # ax1 = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
    # ax1.hist(df_10msample['length'])
    # plt.show()


    '''rockyou EDA'''
    
    '''pwned EDA'''
    # df_pwned[0] = df_pwned[0].str.split(pat=':',n=1)
    # eda.explore_df(df_pwned)
    
    '''linkedin EDA'''
    
