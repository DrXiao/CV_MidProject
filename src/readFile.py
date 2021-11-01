import os
from pathlib import Path
import searcher
import random

# 取得路徑
path_norm = os.path.abspath(os.path.join(
    os.getcwd(), os.path.pardir)) + "//norm.txt"
path_unnorm = os.path.abspath(os.path.join(
    os.getcwd(), os.path.pardir)) + "//unnorm.txt"

#############################
#  data_XX[][0]→檔案名稱     #
#  data_XX[][1]→類別         #
#  data_XX[][2:223]→特徵值   #
##############################
data_norm = []
data_unnorm = []


def readFeature(path):
    data = []
    with open(path) as f:
        cnt = 0
        for line in f.readlines():
            s = line.split(' ')  # 共224項
            data.append(s)
    # print(data_norm[0])
    return data


def main():

    # 隨便選一個編號，顯示所有類別的第pic張圖片，顯示在前端上 (rand_pic+200*k)
    rand_pic = random.randint(0, 199)
    print("rand: ", rand_pic)
    k = random.randint(0, 49)   # 顯示的10張中，被選擇的那一張(從前端接)
    print("idx: ", k*200 + rand_pic)
    caculate = 1  # 計算方式
    flag_norm = True  # 是否正規化
    value = []  # 所有距離
    max_idx = []  # 最大的10個距離的index

    if flag_norm:
        data = readFeature(path_norm)
    else:
        data = readFeature(path_unnorm)

    for i in range(10000):
        if i == (k*200 + rand_pic):
            value.append(0)
            continue
        if caculate == 0:  # 尤拉 公式
            value.append(searcher.euclidean_distance(
                data[(k*200 + rand_pic)][2:223], data[i][2:223]))
        elif caculate == 1:  # cosine 公式
            value.append(searcher.consine_distance(
                data[(k*200 + rand_pic)][2:223], data[i][2:223]))
        elif caculate == 2:  # pcc公式
            value.append(searcher.pcc_distance(
                data[(k*200 + rand_pic)][2:223], data[i][2:223]))
    print(value)
    for i in range(10):
        tmp = max(value)
        max_idx.append(value.index(tmp))
        # print("tmp = ", tmp, ", idx = ", value.index(tmp))
        value[max_idx[i]] = -5  # 已儲存的值就不要ㄌ
    print("original picture: ", data[(k*200 + rand_pic)][0])
    print(max_idx)
    correct = 0
    for i in range(10):
        print(data[max_idx[i]][0])
        if(data[max_idx[i]][1] == data[k*200+rand_pic][1]):
            correct += 1
    print("correct = ", correct*10, "%")
    '''
    data_norm = readFeature(path_norm)
    data_unnorm = readFeature(path_unnorm)
    '''

    '''
    print("file name: ", data_norm[9999][0], "\nfile class: ",
          data_norm[9999][1], "\nfeatures: ", data_norm[9999][2:223])
    '''
    '''
    data = readFeature(path_norm)
    test1 = searcher.euclidean_distance(data[1][2:223], data[2][2:223])
    print(test1)
    test2 = searcher.consine_distance(data[1][2:223], data[2][2:223])
    print(test2)
    test3 = searcher.pcc_distance(data[1][2:223], data[2][2:223])
    print(test3)
    '''


if __name__ == '__main__':
    main()
