import os
from pathlib import Path

features_path = Path("raw features")
img_path = Path("pic")

all_imgs_features = {}

for feature_file in os.listdir(features_path):
    with open(features_path / feature_file, "r") as file:
        file.readline()
        for _ in range(201):
            img_info = file.readline().split(" ")
            #print(img_info[0:32])
            #print(img_info[32:44])
            #print(img_info[44:80])
            #print(img_info[336:398])
            #print(img_info[398:478])
            #print(img_info[479])
            if img_info[479].find(".db") != -1:
                continue
            img_features = [float(feature) for feature in img_info[0:80] + img_info[336:478]]
            all_imgs_features[img_info[479]] = [feature_file.split(".")[0], img_features]

with open("unnorm.txt", "w") as file:
    for img in all_imgs_features:
        print("%s %s"%(img, all_imgs_features[img][0]), end='', file=file)
        for feature_idx in range(len(all_imgs_features[img][1])):
            print(" %d"%(all_imgs_features[img][1][feature_idx]), end='', file=file)
        print(file=file)

with open("norm.txt", "w") as file:
    for img in all_imgs_features:
        print("%s %s"%(img, all_imgs_features[img][0]), end='', file=file)
        for all_range in [[0, 32], [32, 44], [44, 80], [80, 142], [142, 222]]:
            max_feature = max(all_imgs_features[img][1][all_range[0]:all_range[1]])
            min_feature = min(all_imgs_features[img][1][all_range[0]:all_range[1]])
            for feature in all_imgs_features[img][1][all_range[0]:all_range[1]]:
                if max_feature != 0:
                    feature /= max_feature
                print(" %f"%(feature), end='', file=file)
        print(file=file)