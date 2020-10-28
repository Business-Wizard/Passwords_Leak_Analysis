import pandas as pd
import matplotlib.pyplot as plt
import EDA_functions as eda

# sample_10m = '../data/10m_sample_common_passwords/10m_standard_complete2.csv'
sample_10m = 'data/10m_sample_common_passwords/10m_standard_complete2.csv'
pwned_path = '../data/have_i_been_pwned_v4/been_pwned_v4_hash_plain.txt'
linkedin_path = '../data/linkedin_leak/linkedin_hash_plain.txt'
linkedin_test_file = '../data/linkedin_leak/test_write.txt'
rockyou_path = '../data/rockyou_leak/rockyou_copy.txt'


if __name__ == '__main__':
    '''10m_sample'''
    df_10msample = pd.read_csv(sample_10m)\
        .sample(frac=1)
    null_bool = df_10msample.password.isnull()
    # print(null_bool.describe() )
    df_10msample.dropna(axis=0, inplace=True)
    print( df_10msample[ null_bool].count()  )
    df_10msample.to_csv('data/10m_sample_common_passwords/10m_standard_complete3.csv'\
        ,index=None)
    # eda.explore_df(df_10msample)
    # pd.plotting.scatter_matrix(frame=df_10msample.loc[:,
        # ['score','upper','lower','number','symbol'] ])
    # plt.show()

    '''show chart 1 Length'''
    # eda.plot_hist_length(df_10msample)
    # plt.show()

    '''show chart 2 Strength'''
    # eda.plot_hist_strength(df_10msample)
    # plt.show()

    '''show chart 3 password chars'''
    # eda.plot_hist_chars(df_10msample)
    # plt.show()

    '''show chart 4 - guess v. length'''
    # eda.plot_guess_length(df_10msample)
    # plt.show()

    '''rockyou EDA'''
    '''pwned EDA'''
    # df_pwned[0] = df_pwned[0].str.split(pat=':',n=1)
    # eda.explore_df(df_pwned)
    '''linkedin EDA'''
    
