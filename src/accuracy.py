import os
from pathlib import Path
from search import *
import readFile

filesize = 10000
accuracy = 0

# 取得路徑
path_norm = os.path.abspath(os.path.join(
    os.getcwd(), os.path.pardir)) + "/norm.txt"
path_unnorm = os.path.abspath(os.path.join(
    os.getcwd(), os.path.pardir)) + "/unnorm.txt"

f = open("accuracy_class.txt", "w")
norm_data = readFile.readFeature(path_norm)
unnorm_data = readFile.readFeature(path_unnorm)
data = [unnorm_data, norm_data]
for i in range(3):      # 不同公式
    if i == 0:
        f.write("\nEudience distance: \n")
    elif i == 1:
        f.write("\nCosine distance:\n")
    else:
        f.write("\nPCC distance:\n")

    for k in range(2):    # 是否正規化
        if k:
            f.write("***normalize***\n")
        else:
            f.write("***unnormalize***\n")
        for j in range(filesize + 1):      # 跑10000張圖片
            if j % 200 == 0 and j != 0:
                str1 = data[k][j - 1][1] + " " + str(accuracy/20) + "\n"
                f.write(str1)
                accuracy = 0
            if(filesize == j):
                break
            print("pic = ", j, ", caculate = ",
                  i, "accuracy = ", accuracy)

            accuracy += readFile.finding(j, data[k], i)


f.close
