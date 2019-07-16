# 批量预测功能

# from iATC.classification.code.atc import iatc
# from iATC.classification.code.test import read_data
# from iATC.classification.code.test import get_drugs_code
# from iATC.classification.code.test import get_drug_json
from .atc import iatc
from .data_process import read_data
from .data_process import get_drugs_code
from .data_process import get_drug_json
from numpy.random import RandomState
from sklearn.model_selection import train_test_split


# 获取需要批量预测的文件
def read_batch_file(file):
    with open(file, 'r', encoding='UTF-8') as f:
        example = f.read()
        f.close()
    return example


# 将文本数据转换成数据字典
def batch_dict(data):
    drugs = data.split('>')
    data_dict = dict()
    for i in range(1, len(drugs)):
        drug = drugs[i].split('\n')
        print(len(drug))
        name, smiles = drug[0], drug[1]
        data_dict[name] = smiles

    return data_dict


def get_data_index2(data):
    # 获取所有的药物列表
    drug_code_list = get_drugs_code()

    # 获取药物及SMILES
    drug_smiles_dict = get_drug_json()

    data_dict = batch_dict(data)

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


# 批量预测(测试)
def batch_drug_predict(data):
    # 获取并处理数据集
    X, y = read_data()

    # 切分训练测试数据集
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)

    # 创建模型并进行训练
    atc = iatc()
    atc.fit(X_train, y_train)

    drug_dict = get_data_index2(data)
    print(drug_dict)

    predict_dict = dict()

    # 预测结果
    for name, drug_index in drug_dict.items():
        predict = atc.predict(X[drug_index])
        predict_dict[name] = predict

    return predict_dict


def write_to_txt(predict_dict, out_path):
    with open(out_path, 'w', encoding='utf-8') as txt:
        for name, kind in predict_dict.items():
            print(name, kind)
            txt.write(name + ' ' + str(kind) + '\n')
        txt.close()


# file = '../static/in_txt/example.txt'
# data = read_batch_file(file)
# result = batch_drug_predict(data)
# out_path = '../static/out_txt/result.txt'
# write_to_txt(result, out_path)
