import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
plt.style.use('ggplot')
blue_goog = '#4285F4'
green_goog = '#0F9D58'
red_goog = '#DB4437'
yellow_goog = '#F4B400'

def explore_df(df: pd.DataFrame):
    print(df.info(), '\n',
    df.describe(), '\n',
    df.columns, '\n',
    df.head(10), '\n',
    )

def plot_hist():
    pass

def plot_guess_length(df):
    fig476,axes476 = plt.subplots(ncols=1,nrows=1,\
        figsize=(11, 6), dpi=200)
    length = df.length
    guesses = df.guesses_log
    guess_length = axes476
    
    #* Scatter of passwords
    guess_length.scatter(length, guesses, alpha=0.25, color=blue_goog)
    
    #* Trendline of random passwords
    strong_trend_vals = np.linspace(start=5, stop=30, num=1000)
    guess_length.plot(strong_trend_vals, strong_trend_vals, \
        label="Strongest or Random", color=green_goog, alpha=0.8)
    #* Guess_log = 10
    guess_length.axhline(y=10, xmin=0.0, xmax=1.0\
        ,color=yellow_goog, label='2-weeks to crack'\
        , alpha=0.6, linestyle='--')
    #* Guess_log = 8
    guess_length.axhline(y=7, xmin=0.0, xmax=1.0\
        ,color=red_goog, label='17-minutes to crack'\
        , alpha=0.6, linestyle='--')
    
    guess_length.set_title('Guesses v. Password Length')
    guess_length.set_xlabel('Password Length')
    guess_length.set_ylabel('Guesses to Crack(Log)')
    guess_length.set_xlim(2,30)
    guess_length.legend(loc=0)
    plt.tight_layout()
    plt.show()



if __name__ == '__main__':
    pass



