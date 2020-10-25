import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import csv

def chunk_to_csv(*, file_in: str, file_out: str, chunksize:int=10000):
    reader = pd.read_csv(file_in, chunksize=chunksize, sep=',')
    for chunk in reader:
        result = chunk
        result.to_csv(file_out, mode='a', index=False, header=False)

def stringify_row(row: str):
    row_split = row.replace(':', ' ').split()
    return row_split

def stringify_rows(data: list):
    return map(stringify_row, data)

def txt_to_csv(file_in: str, file_out: str, size: int=1000):
    """
    open filepath as reader
    chunk processing
    stringify_rows()
    """
    with open(file_in) as data:
        data_list = data.readlines(size)
        corrected = pd.Series( stringify_rows(data_list) )
        # print(corrected)
        corrected.to_csv(file_out, mode='a', header=False, index=None)


if __name__ == '__main__':
    linkedin_path = '../data/linkedin_leak/linkedin_hash_plain.txt'
    linkedin_test_file = '../data/linkedin_leak/test_write.txt'
    test_read = '../data/10m_sample_common_passwords/test_read.txt'
    test_write = '../data/10m_sample_common_passwords/test_write.txt'
    sample_10m = '../data/10m_sample_common_passwords/10-million-combos.txt'

    
    with open(test_write, 'w') as writer:
        with open(test_read, 'r') as data:
            # csvwriter = csv.writer(writer)
            # csvwriter.writerow(data)
            iter = 1
            for line in data:
                # line = line.split('\t')
                # print(line)
                # datum = str( line.split('\t') ) + ',' + '\n'
                # print(datum[0])
                # print(datum)
                writer.write(str( line.replace('\n', '').split('\t') ) + ',' + '\n')
                if iter > 20:
                    break
                iter += 1
    
    df = pd.read_csv(test_write, header=None)
    # df.drop(2, axis=1, inplace=True)
    
    # df['passwords'].astype(str)
    # df.columns = ['username','password']
    # print(df)

    # print(df.info() )
    # print(df.dtypes)
    # # df['passwords'] = df[0].str.split()

    # df.to_csv(test_write, index=False)

        

    # txt_to_csv(file_in=linkedin_path, file_out=linkedin_test_file, size=1000)
    # print( stringify_row('test_read') )
    # df_test = pd.read_csv(linkedin_test_file, header=None)
    # print( df_test.iloc[:5, 0:1]) 

    
    # chunk_to_csv(file_in=linkedin_path, file_out=linkedin_test_file, chunksize=10000)

    # data_linkedin = rows_to_list(filepath='../data/linkedin_leak/linkedin_hash_plain.txt', nrows=1000)
    # data_linkedin = stringify_rows(data_linkedin)
    # data_linkedin = pd.DataFrame(data_linkedin)
    # print(data_linkedin.head(5) )

    # save_csv(filepath='../data/linkedin_leak/tester1.txt', data=data_linkedin)
    
    # correct_linkedin(linkedin_path)


    # TODO create string deliminaters 
    # TODO data_linkedin = pd.read_csv('../data/linkedin_leak/linkedin_hash_plain.txt')
    # data_10m_sample = pd.read_csv('../data/10m_sample_common_passwords/10m_combos.txt')
    # data_rockyou = pd.read_csv('../data/rockyou_leak/rockyou.txt')
    # !huge-file data_pwned_v6 = pd.read_csv('../data/pwned_passwords_v6/pwned_ordered_v6.txt', nrows=1000000)
