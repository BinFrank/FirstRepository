# 算法测试
import json
import numpy as np
import scipy.io as sio

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression

from skmultilearn.problem_transform import BinaryRelevance
from skmultilearn.problem_transform import LabelPowerset

from iATC.classification.code.multi_score import aiming
from iATC.classification.code.multi_score import coverage
from iATC.classification.code.multi_score import accuracy
from iATC.classification.code.multi_score import absolute_true
from iATC.classification.code.multi_score import absolute_false
from iATC.classification.code.data_process import read_data
from iATC.classification.code.data_process import split_data


# 读取训练、测试数据集，并进行处理
def read_data():
    # 药物ATC分类数据的获取、处理
    data = sio.loadmat('../data/ATC_42_3883.mat')
    atcClass = data.get('atcClass')
    atc_fea = data.get('atc_fea')
    X = atc_fea.T
    # X = X[:, 28:]
    y = atcClass.T
    y = np.where(y < 1, 0, 1)

    return X, y


# 对数据进行分割
def split_data(X, y):
    # 切割训练、测试数据集
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    return X_train, X_test, y_train, y_test


# 获取所有的药物编号
def get_drugs_code():
    # 读取所有的药物编号，返回一个列表
    code_list = []
    with open('../data/drug_code') as drug_info:
        for line in drug_info:
            for i in range(0, len(line)):
                if line[i] == 'D':
                    code_list.append(line[i:i+6])
                    break

    return code_list


# 获取属于每一分类的药物编号
def datasets_classification(col):
    X, y = read_data()
    # index_list = []
    y_cols = y[:, col]
    drug_code_list = get_drugs_code()
    code_list = []
    for i in range(len(y_cols)):
        if y_cols[i] == 1:
            # index_list.append(i)
            code_list.append(drug_code_list[i])

    return code_list


def get_drug_json():
    with open('../data/drug_smiles.json', 'r') as fileR:  # 打开文本读取状态
        drug_smiles = json.load(fileR)  # 解析读到的文本内容 转为python数据 以一个变量接收
        fileR.close()  # 关闭文件
    return drug_smiles


def write_to_txt(predict_dict, out_path):
    with open(out_path, 'w', encoding='utf-8') as txt:
        for name, kind in predict_dict.items():
            print(name, kind)
            txt.write(name + ' ' + str(kind) + '\n')
        txt.close()


def write_to_txt2(predict_dict, out_path):
    with open(out_path, 'w', encoding='utf-8') as txt:
        i = 1
        for code, smi in predict_dict.items():
            if smi is not None:
                txt.write(">Compound-%s\n%s\n" % (i, smi))
                if i == 300:
                    break
                else:
                    i += 1
            else:
                pass
        txt.close()


# drug_dict = get_drug_json()
# out_path = '../data/example.txt'
# write_to_txt2(drug_dict, out_path)
# ex = {"张三": 20, "李四": 19, "王五": 23}
# print(type(ex))
# print(len(ex))
# i = 1
# smi = 'AVSGGG'
# print(">Compound-%s\n%s\n"% (i, smi))
