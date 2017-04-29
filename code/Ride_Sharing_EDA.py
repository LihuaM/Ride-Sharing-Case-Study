from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def get_data(file_path):
    df = pd.read_json(file_path)
    df.set_index('login_time', inplace=True)
    df['login_time_count'] = 1
    df = df.resample('15T').count()
    df['year'] = df.index.year
    df['month'] = df.index.month
    df['day'] = df.index.day
    df['hour'] = df.index.hour
    df['minute_interval'] = df.index.minute
    df['dayofweek'] = df.index.dayofweek
    df['weekend'] = df['dayofweek'].apply(lambda x: 1 if x in range(5,7) else 0)
    df['dayofweek_1'] = df['dayofweek'].map({0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday',\
    4:'Friday', 5:'Saturday', 6:'Sunday'})
    df_new = df[df.month != 8]
    return df_new

def demand_based_on_month(df_new):
    plt.rcParams['figure.figsize'] = (8,6)
    df_new.groupby('month').login_time_count.sum().plot('bar', rot=0)
    plt.title('Login Count Based on Month')
    plt.show()

def demand_based_on_dayofmonth(df_new):
    df_new.groupby('day').login_time_count.sum().plot('bar', rot=0)
    plt.title('Login Count Based on Day of Month')
    plt.show()

def demand_based_on_dayofmonth_eachmonth(df_new):
    fig, axs = plt.subplots(7,1, sharey=True, sharex=True)
    for index, month in enumerate(df_new.month.unique()):
        df_new[df_new.month == month].groupby('day').login_time_count.sum().plot('bar', axs[index],\
        rot=0, title = 'Month %s'%month, figsize=(15,15))
    plt.show()

def demand_based_on_dayofweek(df_new):
    df_new_dayofweek= df_new.groupby('dayofweek_1').login_time_count.sum()
    df_new_dayofweek.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday', 'Sunday']).\
    plot('bar',rot=0)
    plt.title('Login Count Based on Day of Week')
    plt.show()

def demand_based_on_weekday(df_new):
    df_new[df_new.weekend == 0].groupby('hour').login_time_count.sum().plot('bar', rot=0)
    plt.title('Hourly Login Count on Weekday')
    plt.show()

def demand_based_on_weekand(df_new):
    df_new[df_new.weekend == 1].groupby('hour').login_time_count.sum().plot('bar', rot=0)
    plt.title('Hourly Login Count on Weekend')
    plt.show()

def demand_based_on_minuteinterval_weekday(df_new):
    plt.rcParams['figure.figsize'] = (20,10)
    df_new[df_new.weekend == 0].groupby(['hour', 'minute_interval']).login_time_count.sum().\
    unstack().plot(kind='bar', rot=0)
    plt.title('Minute_Interval Login Count on Weekday', fontsize=30)
    plt.show()

def demand_based_on_minuteinterval_weekend(df_new):
    plt.rcParams['figure.figsize'] = (20,10)
    df_new[df_new.weekend == 1].groupby(['hour', 'minute_interval']).login_time_count.sum().\
    unstack().plot(kind='bar', rot=0)
    plt.title('Minute_Interval Login Count on Weekend', fontsize=30)
    plt.show()

if __name__ == '__main__':
    file_path = file_path
    demand_based_on_month(df_new)
    demand_based_on_dayofmonth(df_new)
    demand_based_on_dayofmonth_eachmonth(df_new)
    demand_based_on_dayofweek(df_new)
    demand_based_on_weekday(df_new)
    demand_based_on_weekand(df_new)
    demand_based_on_minuteinterval_weekend(df_new)
    demand_based_on_minuteinterval_weekend(df_new)
