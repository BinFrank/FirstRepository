# 数据处理
import numpy as np
import scipy.io as sio
from urllib import request
from numpy.random import RandomState
import re
import json

from sklearn.model_selection import train_test_split


# 读取训练、测试数据集，并进行处理
def read_data():
    # 药物ATC分类数据的获取、处理
    data = sio.loadmat('classification/data/ATC_42_3883.mat')
    atcClass = data.get('atcClass')
    atc_fea = data.get('atc_fea')
    X = atc_fea.T
    y = atcClass.T
    y = np.where(y < 1, 0, 1)

    return X, y


# 对数据进行分割
def split_data(X, y):
    # 切割训练、测试数据集
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)
    return X_train, X_test, y_train, y_test


# 获取所有的药物编号
def get_drugs_code():
    # 读取所有的药物编号，返回一个列表
    code_list = []
    with open('classification/data/drug_code') as drug_info:
        for line in drug_info:
            for i in range(0, len(line)):
                if line[i] == 'D':
                    code_list.append(line[i:i+6])
                    break

    return code_list


# 爬取药物编号对应的SMILES
def spider_smiles():
    # 爬取每个药物编号对应的smiles，返回编号和SMILES组成的数据字典
    url_temp = 'http://ligandbox.protein.osaka-u.ac.jp/ligandbox/cgi-bin/liginf.cgi?id='
    pattern = '<I>SMILES:</I> ([\s\S]*?)<BR>'
    drugs_code = get_drugs_code()
    drug_smiles = dict()

    for drug_code in drugs_code:
        url = url_temp + drug_code
        r = request.urlopen(url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        res = re.findall(pattern, htmls)
        if res:
            drug_smiles[drug_code] = res[0]
        else:
            drug_smiles[drug_code] = None
    return drug_smiles


# 将爬取后形成的数据字典存入json文件中
def save_json():
    # 获取数据字典
    drug_smiles = spider_smiles()

    with open('../data/drug_smiles.json', 'w', encoding='utf-8') as file:
        # .json文本，只能写入状态 如果没有就创建
        json.dump(drug_smiles, file)  # data转换为json数据格式并写入文件
        file.close()  # 关闭文件


# 获取json文件里的数据，且为字典类型
def get_drug_json():
    with open('classification/data/drug_smiles.json', 'r') as fileR:  # 打开文本读取状态
        drug_smiles = json.load(fileR)  # 解析读到的文本内容 转为python数据 以一个变量接收
        fileR.close()  # 关闭文件
    return drug_smiles


# 获取类别编号与类别
def get_type(file):  # classification/data/type.json
    with open(file, 'rb') as fileR:
        drug_type = json.load(fileR)
        fileR.close()

    return drug_type


# 获取属于每一分类的药物编号
def datasets_classification(col):
    X, y = read_data()
    y_cols = y[:, col]
    drug_code_list = get_drugs_code()
    code_list = []
    for i in range(len(y_cols)):
        if y_cols[i] == 1:
            code_list.append(drug_code_list[i])

    return code_list


# 通过某一类的药物编号获取相应的SMILES列表
def get_smiles_by_code(col):
    smiles_list = []
    drug_smiles_dict = get_drug_json()
    drug_code_col = datasets_classification(col)
    for code, smiles in drug_smiles_dict.items():
        for drug_code in drug_code_col:
            if code == drug_code and smiles is not None:
                smiles_list.append(smiles)

    return smiles_list


# 获取前端传来的查询数据，并进行处理
def get_data(data):
    # 处理前端传来的数据

    data_dict = dict()

    drugs = data.split('>')
    for i in range(1, len(drugs)):
        drug = drugs[i].split('\r\n')
        name, smiles = drug[0], drug[1]
        data_dict[name] = smiles

    return data_dict


def get_data_index(data):

    # 获取所有的药物列表
    drug_code_list = get_drugs_code()

    # 获取药物及SMILES
    drug_smiles_dict = get_drug_json()

    data_dict = get_data(data)
    print(data_dict)

    result_dict = dict()

    for name, smiles in data_dict.items():
        result_dict[name] = None
        for code, smiles2 in drug_smiles_dict.items():
            if smiles == smiles2:
                code_index = drug_code_list.index(code)
                result_dict[name] = code_index
                break

        if result_dict[name] is None:
            rdm = RandomState(len(smiles))
            result_dict[name] = rdm.randint(0, 3882)

    return result_dict
