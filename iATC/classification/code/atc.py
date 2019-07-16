# 算法实现
from skmultilearn.problem_transform import LabelPowerset
from .multi_score import aiming, coverage, accuracy, absolute_true, absolute_false
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


class iatc():

    def __init__(self):
        # 需要使用的算法，创建一个算法模型
        # self.cls = LabelPowerset(LogisticRegression(solver='liblinear', multi_class='auto'))
        self.cls = LabelPowerset(LogisticRegression(solver='liblinear', multi_class='ovr'))

    def fit(self, X_train, y_train):
        # 训练模型
        return self.cls.fit(X_train, y_train)

    def predict(self, x_test):
        # 预测单条数据，返回预测结果
        x_test = x_test.reshape(1, -1)
        predict = self.cls.predict(x_test).toarray()
        predict = predict[0]
        predict_result = []
        for i in range(len(predict)):
            if predict[i] == 1:
                predict_result.append(i + 1)
        return predict_result
