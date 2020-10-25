import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import EDA_functions as eda


if __name__ == '__main__':
    linkedin_path = '../data/linkedin_leak/linkedin_hash_plain.txt'
    linkedin_test_file = '../data/linkedin_leak/test_write.txt'
    test_read = '../data/10m_sample_common_passwords/test_read.txt'
    test_write = '../data/10m_sample_common_passwords/test_write.txt'
    sample_10m = '../data/10m_sample_common_passwords/10-million-combos.txt'
    rockyou_path = '../data/rockyou_leak/rockyou_copy.txt'


    # df_linkedin = pd.read_csv(linkedin_path, header=None, sep='\n')
    # df_rockyou = pd.read_csv(rockyou_path, sep='\n')
    df_10msample = pd.read_csv(sample_10m, header=None, sep='\t')






