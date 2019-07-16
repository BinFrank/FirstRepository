# 多标签评分方法
import numpy as np


def aiming(y_true, y_predict):
    sum = 0.0
    for i in range(len(y_true)):
        y_true_q = []
        y_predict_q = []
        for j in range(len(y_true[i])):
            if y_true[i, j] == 1.0:
                y_true_q.append(j + 1)
            if y_predict[i, j] == 1:
                y_predict_q.append(j + 1)
        if len(y_predict_q) != 0:
            sum += len(list(set(y_true_q) & set(y_predict_q))) * 1.0 / len(y_predict_q)
    aimi = sum / len(y_true)
    return aimi


def coverage(y_true, y_predict):
    sum = 0.0
    for i in range(len(y_true)):
        y_true_q = []
        y_predict_q = []
        for j in range(len(y_true[i])):
            if y_true[i, j] == 1.0:
                y_true_q.append(j + 1)
            if y_predict[i, j] == 1:
                y_predict_q.append(j + 1)
        if len(y_true_q) != 0:
            sum += len(list(set(y_true_q) & set(y_predict_q))) * 1.0 / len(y_true_q)
    cover = sum / len(y_true)
    return cover


def accuracy(y_true, y_predict):
    sum = 0.0
    for i in range(len(y_true)):
        y_true_q = []
        y_predict_q = []
        for j in range(len(y_true[i])):
            if y_true[i, j] == 1.0:
                y_true_q.append(j + 1)
            if y_predict[i, j] == 1:
                y_predict_q.append(j + 1)
        if len(y_true_q) != 0:
            sum += len(list(set(y_true_q) & set(y_predict_q))) * 1.0 / len(list(set(y_true_q) | set(y_predict_q)))
    accur = sum / len(y_true)
    return accur


def absolute_true(y_true, y_predict):
    sum = 0.0
    for i in range(len(y_true)):
        y_true_q = []
        y_predict_q = []
        for j in range(len(y_true[i])):
            if y_true[i, j] == 1.0:
                y_true_q.append(j + 1)
            if y_predict[i, j] == 1:
                y_predict_q.append(j + 1)
        sum += np.float(y_true_q == y_predict_q)
    abs_true = sum / len(y_true)
    return abs_true


def absolute_false(y_true, y_predict):
    sum = 0.0
    m = 14
    for i in range(len(y_true)):
        y_true_q = []
        y_predict_q = []
        for j in range(len(y_true[i])):
            if y_true[i, j] == 1.0:
                y_true_q.append(j + 1)
            if y_predict[i, j] == 1:
                y_predict_q.append(j + 1)
        sum += (len(list(set(y_true_q) | set(y_predict_q))) - len(list(set(y_true_q) & set(y_predict_q)))) * 1.0 / m
    absf = sum / len(y_true)
    return absf
