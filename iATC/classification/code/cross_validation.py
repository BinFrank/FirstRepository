# 交叉验证
import numpy as np

from iATC.classification.code.multi_score import aiming
from iATC.classification.code.multi_score import coverage
from iATC.classification.code.multi_score import accuracy
from iATC.classification.code.multi_score import absolute_true
from iATC.classification.code.multi_score import absolute_false
from iATC.classification.code.test import read_data
from skmultilearn.problem_transform import LabelPowerset
from skmultilearn.problem_transform import BinaryRelevance
from skmultilearn.adapt import MLkNN
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier


def k_fold_cross_validation(classifier, X_data, Y_data, k):
    # 第一步：将数据分成K份
    # 随机打乱索引
    index_arr = np.random.permutation(X_data.shape[0])

    # 分成K份
    step = X_data.shape[0] // k  # 每份的样本数量
    k_arr = []
    for i in range(k):
        if i == 0:  # 第一次切分
            temp_arr = index_arr[0:step]
        else:
            if i == (k - 1):  # 最后一次切分
                temp_arr = index_arr[i * step:]
            else:
                temp_arr = index_arr[i * step:(i + 1) * step]
        k_arr.append(temp_arr)

    # 第二步：进行循环训练测试验证
    aiming_arr = []
    coverage_arr = []
    accuracy_arr = []
    absolute_true_arr = []
    absolute_false_arr = []

    for i in range(k):
        # 选取第i份数据作为测试集
        train_data_index = []
        test_data_index = k_arr[i]

        # 剩余部分为训练集
        for m in range(k):
            if m != i:
                train_data_index.append(k_arr[m])

        # 对算法模型进行训练

        # 抽取训练数据
        X_train = []
        for index in train_data_index:
            # X_train.append(X_data[index])
            temp_X_train = X_data[index]
            for each_data in temp_X_train:
                X_train.append(each_data)
        X_train = np.array(X_train).reshape(-1, X_data.shape[1])

        Y_train = []
        for index in train_data_index:
            temp_Y_train = Y_data[index]
            for each_data in temp_Y_train:
                Y_train.append(each_data)
        Y_train = np.array(Y_train).reshape(-1, Y_data.shape[1])

        # 训练
        classifier.fit(X_train, Y_train)

        # 预测
        # 抽取测试数据
        X_test = []
        for index in test_data_index:
            temp_X_test = X_data[index]
            for each_data in temp_X_test:
                X_test.append(each_data)
        X_test = np.array(X_test).reshape(-1, X_data.shape[1])

        Y_test = []
        for index in test_data_index:
            temp_Y_test = Y_data[index]
            for each_data in temp_Y_test:
                Y_test.append(each_data)
        Y_test = np.array(Y_test).reshape(-1, Y_data.shape[1])

        Y_predict = classifier.predict(X_test).toarray()

        # 计算五个评分标准
        aim = aiming(Y_test, Y_predict)
        cover = coverage(Y_test, Y_predict)
        accur = accuracy(Y_test, Y_predict)
        abst = absolute_true(Y_test, Y_predict)
        absf = absolute_false(Y_test, Y_predict)

        aiming_arr.append(aim)
        coverage_arr.append(cover)
        accuracy_arr.append(accur)
        absolute_true_arr.append(abst)
        absolute_false_arr.append(absf)

    # 将K次验证的结果求均值并返回

    return_result = []

    return_result.append(np.mean(aiming_arr))
    return_result.append(np.mean(coverage_arr))
    return_result.append(np.mean(accuracy_arr))
    return_result.append(np.mean(absolute_true_arr))
    return_result.append(np.mean(absolute_false_arr))

    return return_result


X, y = read_data()
print(X.shape)
lp_clf = LabelPowerset(LogisticRegression(solver='liblinear', multi_class='ovr'))
# RandomForestClassifier()
# lp_clf = LabelPowerset(RandomForestClassifier(n_estimators=100))
br_clf = BinaryRelevance(LogisticRegression(solver='liblinear', multi_class='ovr'))
# ml_knn = MLkNN(k=5)
result = k_fold_cross_validation(lp_clf, X, y, 10)
print(result)
result = k_fold_cross_validation(br_clf, X, y, 10)
print(result)

