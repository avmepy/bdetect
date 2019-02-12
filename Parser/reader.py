# !/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 2/6/19

import os
from Parser.log_merger import *
import pandas as pd


def read(path):
    df = pd.read_csv(path, header=0)
    return df


def test(name):
    return name != '.DS_Store'


def catalog_reader(directory):
    categories = os.listdir(directory)
    human_path = []
    bot_path = []
    for category in categories:
        if test(category):
            sessions = os.listdir(directory + '/' + category)
            for session in sessions:
                if test(session):
                    if category == 'User':
                        human_path.append(sorted([directory + '/' + category + '/' + session + '/' + i \
                                           for i in os.listdir(directory + '/' + category + '/' + session) if test(i)]))
                    else:
                        bot_path.append(sorted([directory + '/' + category + '/' + session + '/' + i \
                                           for i in os.listdir(directory + '/' + category + '/' + session) if test(i)]))
    return human_path, bot_path


def read_all(from_direct: str, to_direct: str) -> bool:
    """
    reads Logs from a directory from_direct and writes merged Logs to a directory to_direct
    the directory to_direct must contain the Bot and human folders
    :param from_direct:
    :param to_direct:
    :return: True
    """

    human_path, bot_path = catalog_reader(from_direct)

    index = 0
    for game, touch in human_path:
        index += 1
        df = process_file(game, touch)
        df.to_csv(f'{to_direct}/human{index}')

    index = 0
    for game, touch in bot_path:
        index += 1
        df = process_file(game, touch)
        df.to_csv(f'{to_direct}/Bot{index}')

    return True
