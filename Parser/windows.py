# !/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 2/6/19


import pandas as pd


def get_windows(df: pd.DataFrame, interval=30000) -> list:
    """
    split the file into long windows at a specified interval
    :param df: DataFrame object of union log file
    :param interval: interval in ms
    :return: list of windows
    """
    windows = []
    index = [0]

    time = list(df['Time'])

    cur = 0
    while cur < len(time):
        if time[cur] - time[index[-1]] >= interval:
            index.append(cur)
        cur += 1

    for i in range(len(index) - 1):
        windows.append(df[index[i]: index[i+1]])

    return windows