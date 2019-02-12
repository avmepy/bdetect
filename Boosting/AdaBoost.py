# !/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 2/6/19


from Classifier.classifier import *
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier


def AdaBoost(bot: list, human: list, roc=False):
    training, test = classifier(bot, human)

    m = AdaBoostClassifier(base_estimator=DecisionTreeClassifier())
    m.fit(*training)
    predict = m.predict(test[0])
    matrix = confusion_matrix(test[1], predict)

    if roc:
        x, y, _ = roc_curve(test[1], roc_helper(predict), pos_label=1)
        roc_stats['KNeighbors'] = (x, y)

    return m.score(*test), matrix, classification_report(test[1], predict)


if __name__ == '__main__':

    bot, human = get_data(path_bot, path_human)
    score, matrix, report = AdaBoost(bot, human, roc=True)
    print('AdaBoost')
    print(f'accuracy: {score}')
    print(matrix)
    print(report)

    rocCurve(roc_stats, 'AdaBoost')