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

def plot_hist_length(df: pd.DataFrame):
    fig752 = plt.figure(dpi=200, figsize=(11,6))
    ax752 = fig752.add_axes([0.1, 0.1, 0.8, 0.8])
    ax752.hist(df['length'], color=blue_goog)

def plot_hist_score(df: pd.DataFrame):
    fig712 = plt.figure(dpi=200, figsize=(11,6))
    ax712 = fig712.add_axes([0.1, 0.1, 0.8, 0.8])
    ax712.hist(df['score'], align='mid'\
        ,color=blue_goog)
    plt.xticks([0,1,2,3,4] )

def plot_hist_chars(df: pd.DataFrame):
    cols_lst =['lower', 'upper', 'number', 'symbol']

    fig128, axes128 = plt.subplots(nrows=2, ncols=2 \
        ,dpi=200, figsize=(11,6) )
    fig128.suptitle("Distribution of characters in passwords")
    
    for idx, ax in enumerate(axes128.flat ):
        col = cols_lst[idx]
        ax.hist(df[col], color=blue_goog)
        ax.set_xlabel(f"{col} characters")
    plt.tight_layout()

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



