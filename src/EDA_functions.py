import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

#! Customizations of specific color choices and theme parameters.
#! If intending to use different colors, must assign to the following variables
#! or change the colors manually in each function as needed.
#TODO Edit functions to take in color arguments
plt.style.use('ggplot')
plt.rcParams.update({'font.size': 14})
blue_goog = '#4285F4'
green_goog = '#0F9D58'
red_goog = '#DB4437'
yellow_goog = '#F4B400'



def explore_df(df: pd.core.Frame.DataFrame):
    """Simple function for printing common information of a DataFrame

    Args:
        df (pd.core.Frame.DataFrame): dataframe to be analyzed
    """
    print(df.info(), '\n',
    df.describe(), '\n',
    df.columns, '\n',
    df.head(10), '\n',
    )

def plot_hist_length(df: pd.DataFrame):
    """Generates (but does not show|save) bar chart for viewing distribution of passwords lengths

    Args:
        df (pd.core.Frame.DataFrame): DataFrame with a column "length" with password lengths
    """
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
    """Generates (but does not show|save) bar chart for viewing distribution of passwords strength

    Args:
        df (pd.core.Frame.DataFrame): DataFrame with a column "guesses_log" with password guess estimates
    
    Usage:
        See function zxcvbn_guesslog in included data_pipeline.py file for generating needed "guesses_log" column
    """
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

def plot_hist_chars(df: pd.DataFrame, strength:int=8):
    """Generates (but does not show|save) bar charts for viewing distribution of password character types used,
    at the given strength level passed.

    Args:
        df (pd.DataFrame): [description]
        strength (int, optional): [description]. Defaults to 8.

    Usage:
        One popular usage of this function is to create a loop for saving the images using .savefig\
            and passing through a giph animation generator.
    """
    #TODO Create version of function with .savefig method to ease generating giph animations.
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
    """Generates (but does not show|save) scatter plot of df.guesses_log vs. df.length,
    with horizontal lines at the 7, 10, and 12 levels of password strength (guesses to crack in log-scale)

    Args:
        df (pd.core.Frame.DataFrame): DataFrame with a column "guesses_log" and "length"\
            of password guess estimates and lengths.
    
    Usage:
        See standardize_10msample function in included data_pipeline.py file\
            for help creating "guesses_log" and "length" columns.
    """
    fig476,axes476 = plt.subplots(ncols=1,nrows=1,\
        figsize=(11, 6), dpi=200)
    length = df.length
    guesses = df.guesses_log
    guess_length = axes476
    
    #* Scatter of passwords
    guess_length.scatter(length, guesses, alpha=0.25\
        ,color=blue_goog, marker='.')
    
    #* Trendline of random passwords - useful for highlighting max strength at each length
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



