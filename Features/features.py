# !/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 2/6/19

import pandas as pd
import numpy as np


def apm(df: pd.DataFrame) -> float:
    """
    count average number of actions per minute
    :param df: DataFrame object of union log file
    :return: apm
    """
    time = abs(list(df['Time'])[-1] - list(df['Time'])[0]) / 60000  # in minutes
    act = list(df['Event'])
    num_act = act.count(' Fight') + act.count(' Drop')
    try:
        return num_act / time
    except ZeroDivisionError:
        return 0


def aht(df: pd.DataFrame) -> float:
    """
    average duration of pressing per session
    :param df: DataFrame object of union log file
    :return: aht
    """
    times = list(df['move-time'])
    res = []
    for i in times:
        if not str(i).isalpha():
            res.append(i)
    if res:
        return sum(res) / len(res)
    return 0


def reflection(df: pd.DataFrame) -> float:
    """
    average time of the reflection
    :param df: DataFrame object of union log file
    :return: avt
    """
    indices = []

    for i in range(len(list(df['Event']))):
        if list(df['Event'])[i] == ' Touch':
            indices.append(i)

    times = []

    for i in indices[1:]:
        times.append(abs(list(df['Time'])[i] - list(df['Time'])[i-1]))

    if times:
        return sum(times) / len(times)
    return 0

def gpm(df: pd.DataFrame) -> float:
    """
    count average number of drops per minute
    :param df: DataFrame object of union log file
    :return: gpm
    """
    time = abs(list(df['Time'])[-1] - list(df['Time'])[0]) / 60000  # in minutes
    gold = list(df['Event']).count(' Drop')
    if time:
        return gold / time
    return 0


def dpm(df: pd.DataFrame) -> float:
    """
    count average number of fights per minute
    :param df: DataFrame object of union log file
    :return: dpm
    """
    time = abs(list(df['Time'])[-1] - list(df['Time'])[0]) / 60000  # in minutes
    dragon = list(df['Event']).count(' Fight')
    if time:
        return dragon / time
    return 0


def way_compl(data):

    def _index(data, index):
        for i, row in data.iterrows():
            if i > index and row['Event'] == ' Touch':
                return row['X-coord'], row['Y-coord'], row['Time']

    V = 0.3
    comp = 0
    touches = 0
    for index, row in data.iterrows():
        if index < len(data)-1:
            if row['Event'] == ' Touch':
                last = (row['X-coord'], row['Y-coord'], row['Time'])
                next = _index(data, index)
                if next is None:
                    touches += 1
                else:
                    distance = np.sqrt((last[0] - next[0])**2 + (last[1] - next[1])**2)
                    time = next[2] - last[2]
                    tmp = distance / V
                    if distance / V <= time:
                        comp += 1
                    touches += 1
    return np.abs(comp - touches)