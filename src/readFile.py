import os
from pathlib import Path
from search import *
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


def readFeature(path):
    data = []
    with open(path) as f:
        cnt = 0
        for line in f.readlines():
            s = line.split(' ')  # 共224項
            data.append(s)
    # print(data_norm[0])
    return data


def distance(num, data, c):
    d = []

    for i in range(10000):
        if i == num:
            if c == 0:
                d.append(1E9)
            else:
                d.append(0)
            continue
        if c == 0:  # 尤拉 公式
            d.append(euclidean_distance(
                data[num][2:223], data[i][2:223]))
        elif c == 1:  # cosine 公式
            d.append(consine_distance(
                data[num][2:223], data[i][2:223]))
        elif c == 2:  # pcc公式
            d.append(pcc_distance(
                data[num][2:223], data[i][2:223]))
    # print(d)
    return d


def searching(caculate, value):
    idx = []
    for i in range(10):
        g = 0
        if caculate == 0:
            tmp = min(value)
            g = 1E9
        else:
            tmp = max(value)
            g = 0
        idx.append(value.index(tmp))
        value[idx[i]] = g  # 已儲存的值就不要ㄌ

    return idx


def main():

    # 隨便選一個編號，顯示所有類別的第pic張圖片，顯示在前端上 (rand_pic+200*k)
    rand_pic = random.randint(0, 199)
    print("rand: ", rand_pic)
    k = random.randint(0, 49)   # 顯示的50張中，被選擇的那一張(從前端接)
    print("idx: ", k*200 + rand_pic)
    caculate = 1  # 計算方式
    flag_norm = True  # 是否正規化
    value = []  # 所有距離
    similar_idx = []  # 最大的10個距離的index

    if flag_norm:
        data = readFeature(path_norm)
    else:
        data = readFeature(path_unnorm)

    value = distance(k*200+rand_pic, data, caculate)

    similar_idx = searching(caculate, value)
    print("original picture: ", data[(k*200 + rand_pic)][0])
    print(similar_idx)
    correct = 0
    for i in range(10):
        print(data[similar_idx[i]][0])
        if(data[similar_idx[i]][1] == data[k*200+rand_pic][1]):
            correct += 1
    print("\ncorrect = ", correct*10, "%")


if __name__ == '__main__':
    main()
