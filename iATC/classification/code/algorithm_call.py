# 算法调用
from .atc import iatc
from .data_process import read_data
from .data_process import split_data
from .data_process import get_data_index
from .data_process import get_type
from .batch_predict import get_data_index2


'''调用封装的函数，传入需要预测的数据，返回预测结果和评分'''


# 少量预测，单个预测
def drug_predict(data):
    # 获取并处理数据集
    X, y = read_data()

    # 切分训练测试数据集
    X_train, X_test, y_train, y_test = split_data(X, y)

    # 创建模型并进行训练
    atc = iatc()
    atc.fit(X_train, y_train)

    drug_dict = get_data_index(data)
    print(drug_dict)

    predict_dict = dict()

    # 预测结果
    for name, drug_index in drug_dict.items():
        predict = atc.predict(X[drug_index])
        predict_dict[name] = predict

    return predict_dict


# 批量预测
def batch_drug_predict(data):
    # 获取并处理数据集
    X, y = read_data()

    # 切分训练测试数据集
    X_train, X_test, y_train, y_test = split_data(X, y)

    # 创建模型并进行训练
    atc = iatc()
    atc.fit(X_train, y_train)

    drug_dict = get_data_index2(data)
    print(drug_dict)

    # 获取类别列表
    json_path = 'classification/data/type.json'
    kind_dict = get_type(json_path)

    predict_dict = dict()

    # 预测结果
    for name, drug_index in drug_dict.items():
        predict = atc.predict(X[drug_index])
        kind_list = []
        for i in predict:
            for code, kind in kind_dict.items():
                if i == int(code):
                    kind_list.append(kind)
        predict_dict[name] = kind_list

    return predict_dict
