# !/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 2/4/19

import umap
import matplotlib.pyplot as plt
from Features.features import *
from Parser.windows import get_windows
from Parser.reader import read
import warnings


warnings.simplefilter(action='ignore')


features = [apm, aht, gpm, dpm, way_compl]


def get_data(logs: list, features: list) -> list:
    res = []
    for log in logs:
        tmp = {}
        for feature in features:
            tmp[feature] = feature(log)
        res.append(tmp)
    return res



def prepare(features, data):
    res_data = []
    for i in data:
        res_data.append([i[j] for j in features])
    return res_data


if __name__ == '__main__':

    path_human = [
        r'/Users/casatka/Desktop/all/github/2019-knu-bdetect/Union_logs/User/human1',
        r'/Users/casatka/Desktop/all/github/2019-knu-bdetect/Union_logs/User/human2',
        r'/Users/casatka/Desktop/all/github/2019-knu-bdetect/Union_logs/User/human3',
        r'/Users/casatka/Desktop/all/github/2019-knu-bdetect/Union_logs/User/human4',
        r'/Users/casatka/Desktop/all/github/2019-knu-bdetect/Union_logs/User/human5',
        r'/Users/casatka/Desktop/all/github/2019-knu-bdetect/Union_logs/User/human6'
    ]

    path_bot = [
        r'/Users/casatka/Desktop/all/github/2019-knu-bdetect/Union_logs/Bot/bot1',
        r'/Users/casatka/Desktop/all/github/2019-knu-bdetect/Union_logs/Bot/bot2',
        r'/Users/casatka/Desktop/all/github/2019-knu-bdetect/Union_logs/Bot/bot3',
        r'/Users/casatka/Desktop/all/github/2019-knu-bdetect/Union_logs/Bot/bot4'
    ]

    logs_bot = []
    logs_human = []

    for path in path_human:
        for window in get_windows(read(path), interval=10000):
            logs_human.append(window)

    for path in path_bot:
        for window in get_windows(read(path), interval=10000):
            logs_bot.append(window)

    reducer = umap.UMAP()

    feat_h = get_data(logs_human, features)
    feat_b = get_data(logs_bot, features)

    data = prepare(features, feat_h + feat_b)

    data = reducer.fit_transform([i for i in data])

    plt.scatter(data[:, 0], range(len(data[:, 0])), color='red')
    plt.scatter(data[:, 1], range(len(data[:, 1])), color='blue')

    plt.gca().set_aspect('auto', 'datalim')
    plt.title('umap', fontsize=24)
    plt.show()
