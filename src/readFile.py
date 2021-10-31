import os
from pathlib import Path
import searcher

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
    data_norm = readFeature(path_norm)
    data_unnorm = readFeature(path_unnorm)
    '''
    print("file name: ", data_norm[9999][0], "\nfile class: ",
          data_norm[9999][1], "\nfeatures: ", data_norm[9999][2:223])
    '''
    data = readFeature(path_norm)
    test1 = searcher.euclidean_distance(data[1][2:223],data[2][2:223])
    print(test1)
    test2 = searcher.consine_distance(data[1][2:223],data[2][2:223])
    print(test2)
    test3 = searcher.pcc_distance(data[1][2:223],data[2][2:223])
    print(test3)

if __name__ == '__main__':
    main()
    
