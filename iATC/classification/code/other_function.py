# 计算矩阵中预测值为1的个数大于等于2的索引
def CountM(y_predict):
    m = []
    for i in range(len(y_predict)):
        count = 0
        for j in y_predict[i]:
            if j == 1:
                count += 1
                if count >= 2:
                    if i not in m:
                        m.append(i)
    return m


# 求真实数据集和预测数据集中为真的数据下标
def index_true(y_true, y_predict):
    y_true_p = []
    y_predict_p = []
    for i in range(len(y_true)):
        y_true_q = []
        y_predict_q = []
        for j in range(len(y_true[i])):
            if y_true[i, j] == 1.0:
                y_true_q.append(j + 1)
            if y_predict[i, j] == 1:
                y_predict_q.append(j + 1)
        y_true_p.append(y_true_q)
        y_predict_p.append(y_predict_q)
    return y_true_p, y_predict_p
