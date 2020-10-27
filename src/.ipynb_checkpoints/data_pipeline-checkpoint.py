import pandas as pd
import string
from zxcvbn import zxcvbn
from dask.distributed import Client
from dask import delayed
from dask import compute
import dask.dataframe as dd
try: 
    from pyspark import SparkContext as sc
    from pyspark.sql import SparkSession
    spark = SparkSession.builder.appname('Passwords').getOrCreate()
except:
    print("Run from a Spark-capable computer for improved performance")
    spark_available = False

def class_count(password: str):
    lower = set(string.ascii_lowercase)
    upper = set(string.ascii_uppercase)
    number = set(string.digits)
    symbol = set(string.punctuation)
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

def class_expand(df: pd.DataFrame):
    class_split = df['class'].str.split(pat=',', expand=True, n=3)
    df = df.drop('class', axis=1) #,inplace=True)
    df['upper'] = class_split[0]
    df['lower'] = class_split[1]
    df['number'] = class_split[2]
    df['symbol'] = class_split[3]
    
def zxcvbn_score(password: str):
    return zxcvbn(password)['score']

def zxcvbn_guesslog(password: str):
    return zxcvbn(password)['guesses_log10']

def strength_features(df):
    df['score'] = df['password'].apply(zxcvbn_score)
    df['guesses_log'] = df['password'].apply(zxcvbn_guesslog)
    # df['time_guess'] = df['password'].apply(zxcvbn)['']

def standardize_10msample(frac: float=0.1):
    sample_10m = '../data/10m_sample_common_passwords/10-million-combos.txt'
    if spark_available:
        df_10msample = sc.read.csv(sample_10m)
        print(type( df_10msample) )
    
    else:
        df_10msample = pd.read_csv(sample_10m, header=None, sep='\t').astype(str).sample(frac=frac)
        df_10msample.columns = ['username', 'password']
        df_10msample.drop('username', axis=1, inplace=True)
        df_10msample['length'] = df_10msample['password'].apply(len)
        strength_features(df_10msample)
        df_10msample['class'] = df_10msample['password'].apply(class_count)
        class_expand(df_10msample)
    
    return df_10msample

def standardize_10msample_dask(frac: float=0.01):
    sample_10m = '../data/10m_sample_common_passwords/10-million-combos.txt'
    df_10msample = dd.read_csv(sample_10m, header=None, sep='\t').astype(str).sample(frac=frac)
    df_10msample.columns = ['username', 'password']
    df_10msample = df_10msample.drop('username', axis=1)
    df_10msample['length'] = df_10msample['password'].apply(len, meta=('password', 'str'))
    strength_features(df_10msample)
    df_10msample['class'] = df_10msample['password'].apply(class_count, meta=('class', 'str'))
    class_expand(df_10msample)
    return df_10msample

if __name__ == '__main__':
    sample_10m = '../data/10m_sample_common_passwords/10-million-combos.txt'
    test_read = '../data/10m_sample_common_passwords/test_read.txt'
    test_write = '../data/test_write.txt'

    df_10msample = standardize_10msample(frac=0.001)
    print(df_10msample.head(10) )




    linkedin_path = '../data/linkedin_leak/linkedin_hash_plain.txt'
    # df_linkedin = pd.read_csv(linkedin_path, header=None, sep='\n')


    rockyou_path = '../data/rockyou_leak/rockyou_copy.txt'
    # df_rockyou = pd.read_csv(rockyou_path, sep='\n')


    pwned_path = '../data/have_i_been_pwned_v4/been_pwned_v4_hash_plain.txt'
    # df_pwned = pd.read_csv(pwned_path, header=None, \
    #         sep='\n', columns='password')
    #         .astype(str)



