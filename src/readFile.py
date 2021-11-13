import os
from pathlib import Path
from search import *
import random
filesize = 10000
# 取得路徑
path_norm = os.path.abspath(os.path.join(
    os.getcwd(), os.path.pardir)) + "/norm.txt"
path_unnorm = os.path.abspath(os.path.join(
    os.getcwd(), os.path.pardir)) + "/unnorm.txt"

#############################
#  data_XX[][0]→檔案名稱     #
#  data_XX[][1]→類別         #
#  data_XX[][2]→特徵值   #
##############################


def readFeature(path):
    data = []
    with open(path) as f:
        cnt = 0
        for line in f.readlines():
            s = line.split(' ')  # 共224項
            data.append([s[0], s[1], np.array([float(num) for num in s[2:]])])
    # print(data_norm[0])
    return data


def distance(num, data, c):
    d = []

    for i in range(filesize):
        if i == num:
            if c == 0:
                d.append(1E9)
            else:
                d.append(0)
            continue
        if c == 0:  # 尤拉 公式
            d.append(euclidean_distance(
                data[num][2], data[i][2]))
        elif c == 1:  # cosine 公式
            d.append(consine_distance(
                data[num][2], data[i][2]))
        elif c == 2:  # pcc公式
            d.append(pcc_distance(
                data[num][2], data[i][2]))
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


def finding(pic_num, data, flag_dist):
    value = []  # 所有距離
    similar_idx = []  # 最大的10個距離的index

    value = distance(pic_num, data, flag_dist)

    similar_idx = searching(flag_dist, value)
    # print("original picture: ", data[pic_num][0])
    # print(similar_idx)
    accuracy = 0
    for i in range(10):
        # print(data[similar_idx[i]][0])
        if(data[similar_idx[i]][1] == data[pic_num][1]):
            accuracy += 1
    # print("\ncorrect = ", correct*10, "%")
    return accuracy


def main():

    k = random.randint(0, 49)   # 選擇類別)
    rand_pic = random.randint(0, 199)  # 選擇編號
    # print("rand: ", rand_pic)
    # print("idx: ", k*200 + rand_pic)

    caculate = 1  # 計算方式
    flag_norm = True  # 是否正規化
    # accuracy = 0
    # accuracy = finding(k*200 + rand_pic, flag_norm, caculate)

    '''下面是用來測準確率ㄉ！'''
    f = open("accuracy_dist_v2.txt", "w")
    norm_data = readFeature(path_norm)
    unnorm_data = readFeature(path_unnorm)
    data = [unnorm_data, norm_data]
    for k in range(2):      # 是否正規化
        if k:
            f.write("\n***normalize***\n")
        else:
            f.write("\n***unnormalize***\n")
        for i in range(3):              # 不同公式
            accuracy = 0
            for j in range(filesize):      # 跑10000張圖片
                print("pic = ", j, ", caculate = ",
                      i, "accuracy = ", accuracy)
                accuracy += finding(j, data[k], i)
            if i == 0:
                str1 = "Eudience distance: " + str(accuracy/1000) + "\n"
            elif i == 1:
                str1 = "Cosine distance: " + str(accuracy/1000) + "\n"
            else:
                str1 = "PCC distance: " + str(accuracy/1000) + "\n"
            f.write(str1)


if __name__ == '__main__':
    main()
