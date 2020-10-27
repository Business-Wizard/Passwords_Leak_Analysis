import pandas as pd
from dask.distributed import Client
import dask.dataframe as dd
import string
from zxcvbn import zxcvbn

try: 
    from pyspark import SparkContext as sc
    from pyspark.sql import SparkSession
except:
    spark_available = False
try:
    spark = SparkSession.builder.appName('Passwords').getOrCreate()
except:
    print("Errors with starting SparkSession")


class DataSet():
    def __init__(self, filepath: str, delimiter: str, df_type: str='pandas'):
        self.filepath = filepath
        self.delimiter = delimiter
        self.df_type = identify_dataframe_type(df_type)

    def identify_dataframe_type(self, df_type):
        if df_type == 'dask':
            self.df_type = dd.core.DataFrame
        elif df_type == 'pandas':
            self.df_type = pd.core.frame.DataFrame
        elif df_type == 'spark':
            print('pyspark DataFrame not yet implemented')
            self.df_type = pd.core.frame.DataFrame
        return self.df_type
        
    def pass_class(password: str):
        lower = set(string.ascii_lowercase)
        upper = set(string.ascii_uppercase)
        number = set(string.digits)
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





'''
class daskDataSet(DataSet):
    def __init__(self):

class pysparkDataSet(DataSet):
    def __init__(self):
'''

def pass_class(df: pd.core.frame.DataFrame):
    class_split = df['class'].str.split(pat=',', expand=True, n=3)
    df['upper'] = class_split[0]
    df['lower'] = class_split[1]
    df['number'] = class_split[2]
    df['symbol'] = class_split[3]
    
    if isinstance(df, pd.core.frame.DataFrame):
        df.drop('class', axis=1, inplace=True)
    else:
        df = df.drop('class', axis=1)


def zxcvbn_score(password: str):
    return zxcvbn(password)['score']

def zxcvbn_guesslog(password: str):
    return zxcvbn(password)['guesses_log10']

def strength_features(df):
    df['score'] = df['password'].apply(zxcvbn_score)
    df['guesses_log'] = df['password'].apply(zxcvbn_guesslog)
    # df['time_guess'] = df['password'].apply(zxcvbn)['']


def to_csv(df, filename: str='../data/data.csv'):
    if isinstance(df, dd.core.DataFrame):
        df.to_csv(filename, single_file=True)
    else:
        df.to_csv(filename)

def standardize_10msample(frac: float=0.01):
    sample_10m = '../data/10m_sample_common_passwords/10-million-combos.txt'
    # if spark_available:
    #     df_10msample = spark.read.csv(sample_10m, delimiter='\t').sample(fraction=frac)\
    #         .withColumnRenamed('_c0', 'username')\
    #         .withColumnRenamed('_c1', 'password')
    # df_10msample.columns = ['username', 'password']
    
    df_10msample = pd.read_csv(sample_10m, header=None, delimiter='\t').astype(str).sample(frac=frac)
    df_10msample.columns = ['username', 'password']
    df_10msample.drop('username', axis=1, inplace=True)
    df_10msample['length'] = df_10msample['password'].apply(len)
    strength_features(df_10msample)
    df_10msample['class'] = df_10msample['password'].apply(withPassClass)
    class_expand(df_10msample)
    to_csv(df_10msample, filename='../data/10m_sample_common_passwords/10m_normalized.csv')
    return df_10msample

def standardize_10msample_dask(frac: float=0.01):
    sample_10m = '../data/10m_sample_common_passwords/10-million-combos.txt'
    df_10msample = dd.read_csv(sample_10m, header=None, delimiter='\t').astype(str).sample(frac=frac)
    df_10msample.columns = ['username', 'password']
    df_10msample = df_10msample.drop('username', axis=1)
    df_10msample['length'] = df_10msample['password'].apply(len, meta=('password', 'str'))
    strength_features(df_10msample)
    df_10msample['class'] = df_10msample['password'].apply(withPassClass, meta=('class', 'str'))
    class_expand(df_10msample)
    to_csv(df_10msample, filename='../data/10m_sample_common_passwords/10m_normalized.csv')
    return df_10msample

if __name__ == '__main__':
    sample_10m = '../data/10m_sample_common_passwords/10-million-combos.txt'
    test_read = '../data/10m_sample_common_passwords/test_read.txt'
    test_write = '../data/test_write.txt'

    # df_10msample = standardize_10msample(frac=1)
    # df_10msample.to_csv('../data/10m_sample_common_passwords/10m_normalized.csv', single_file=True)
    # print( df_10msample.head() )




    linkedin_path = '../data/linkedin_leak/linkedin_hash_plain.txt'
    # df_linkedin = pd.read_csv(linkedin_path, header=None, delimiter='\n')

    rockyou_path = '../data/rockyou_leak/rockyou_copy.txt'
    # df_rockyou = pd.read_csv(rockyou_path, delimiter='\n')

    pwned_path = '../data/have_i_been_pwned_v4/been_pwned_v4_hash_plain.txt'
    # df_pwned = pd.read_csv(pwned_path, header=None, \
    #         delimiter='\n', columns='password')
    #         .astype(str)



