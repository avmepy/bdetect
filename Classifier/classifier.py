# !/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 2/3/19

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve
from Features.features import *
from Parser.reader import read
from Parser.windows import get_windows
import warnings
import matplotlib.pyplot as plt

warnings.simplefilter(action='ignore')


roc_stats = {}


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


BOT = 0
HUMAN = 1
features = [apm, aht, gpm, dpm, way_compl]


def prepare_data(df: pd.DataFrame, player=BOT, features=features):
    """
    prepares data for use in the Classifier
    :param df: DataFrame object
    :param player: BOT / HUMAN
    :param features: list of Features name
    :return:
    """
    return [[i(df) for i in features], [player]]


def classifier(bot: list, human: list) -> tuple:

    features_bot = []
    results_bot = []

    features_human = []
    results_human = []

    for i in bot:
        cur = prepare_data(i)
        features_bot.append(cur[0])
        results_bot.append(cur[1])

    for i in human:
        cur = prepare_data(i, player=HUMAN)
        features_human.append(cur[0])
        results_human.append(cur[1])

    tmp = train_test_split(features_human + features_bot, results_human + results_bot)
    training = (tmp[0], tmp[2])
    test = (tmp[1], tmp[3])

    return training, test


def out(res):
    score, matrix, report = res

    print(f'accuracy : {score}')
    print(matrix)
    print(report)


def main(func_name: callable):

    #  get windows from all Logs
    bot, human = get_data(path_bot, path_human)

    print(func_name.__name__)
    out(func_name(bot, human))


def roc_helper(y_predicted):
    return np.array([y_predicted[i] == 1 for i in range(len(y_predicted))])



def get_data(path_bot, path_human):
    human = []
    bot = []

    for path in path_human:
        human += get_windows(read(path), interval=10000)

    for path in path_bot:
        bot += get_windows(read(path), interval=10000)

    return bot, human


def rocCurve(roc_stats, func_name, zoom_xlim=(0, 1), zoom_ylim=(0, 1.1)):

    for name, roc_x_y in roc_stats.items():
        plt.plot(*roc_x_y, label=name)

    plt.xlim(*zoom_xlim)
    plt.ylim(*zoom_ylim)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel('False positive rate')
    plt.ylabel('True positive rate')
    plt.title(f'ROC {func_name}')
    plt.legend(loc='best')
    plt.show()
