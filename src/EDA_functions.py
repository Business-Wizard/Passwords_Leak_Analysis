import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rcParams.update({'font.size': 14})

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
    fig752, ax752 = plt.subplots(dpi=200, figsize=(11,6))
    bins = range(18)
    
    ax752.hist(df.length, color=blue_goog, align='left'\
        ,density=True, bins=bins, rwidth=0.8)
    plt.xticks(ticks=range(0,18,2))

    ax752.set_title('Distribution of Password Length')
    ax752.set_xlabel('Password Length')
    ax752.set_ylabel('Density of Length')
    plt.tight_layout()

def plot_hist_strength(df: pd.DataFrame):
    fig712,ax712 = plt.subplots(dpi=200, figsize=(11,6))
    bins = range(18)
    counts = df.guesses_log
    
    ax712.hist(x=counts, align='left', density=True\
        ,color=blue_goog, bins=bins, rwidth=0.8)
    plt.xticks(ticks=range(0,18,2))
    
    ax712.set_title('Distribution of Password Strength')
    ax712.set_xlabel('Password Strength(Log-Guesses)')
    ax712.set_ylabel('Density of Strength')
    plt.tight_layout()

def plot_hist_chars(df: pd.DataFrame, strength:int=4):
    cols_lst =['lower', 'upper', 'number', 'symbol']
    
    fig128, axes128 = plt.subplots(nrows=2, ncols=2 \
        ,dpi=200, figsize=(11,6) )
    fig128.suptitle(f"Characters in Strength:{strength}-{strength+2} Passwords")
    for idx, ax in enumerate(axes128.flat):
        col = cols_lst[idx]
        # score_and_length = df
        score_and_length = df[(df.guesses_log <= strength+2) & (df.guesses_log >= strength)]
        data = score_and_length[col]
        args_lst = [
            {'x':data, 'density':True, 'color':blue_goog\
                ,'align':'left' ,'bins':range(0,28)},
            {'x':data, 'density':True, 'color':blue_goog\
                ,'align':'left' ,'bins':range(0,10)},
            {'x':data, 'density':True, 'color':blue_goog\
                ,'align':'left' ,'bins':range(0,20)},
            {'x':data, 'density':True, 'color':blue_goog\
                ,'align':'left' ,'bins':range(0,6)}
        ]
        ax.hist(**args_lst[idx])
        ax.set_xlabel(f"{col} characters")
        plt.tight_layout()
    
def plot_guess_length(df):
    fig476,axes476 = plt.subplots(ncols=1,nrows=1,\
        figsize=(11, 6), dpi=200)
    length = df.length
    guesses = df.guesses_log
    guess_length = axes476
    
    #* Scatter of passwords
    guess_length.scatter(length, guesses, alpha=0.25\
        ,color=blue_goog, marker='.')
    
    #* Trendline of random passwords
    # strong_trend_vals = np.linspace(start=5, stop=30, num=1000)
    # guess_length.plot(strong_trend_vals, strong_trend_vals, \
    #     label="Strongest or Random", color=green_goog, alpha=0.8)
    
    #* Guess_log = 12
    guess_length.axhline(y=12, xmin=0.0, xmax=1.0\
        ,color=green_goog, label='(12):3 years'\
        , alpha=0.6, linestyle='--')
    #* Guess_log = 10
    guess_length.axhline(y=10, xmin=0.0, xmax=1.0\
        ,color=yellow_goog, label='(10):2 weeks'\
        , alpha=0.6, linestyle='--')
    #* Guess_log = 7
    guess_length.axhline(y=7, xmin=0.0, xmax=1.0\
        ,color=red_goog, label='(7):17 minutes'\
        , alpha=0.6, linestyle='--')
    
    guess_length.set_title('Guesses v. Password Length')
    guess_length.set_xlabel('Password Length')
    guess_length.set_ylabel('Guesses to Crack(Log-scale)')
    guess_length.set_xlim(2,30)
    guess_length.legend(loc=0)
    plt.tight_layout()



if __name__ == '__main__':
    pass



