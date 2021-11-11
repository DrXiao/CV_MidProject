from flask import Flask, render_template, request
import sys
sys.path.append("src")
from readFile import *
from search import *
from pathlib import Path
from base64 import b64encode

app = Flask(__name__, template_folder="templates")

pic_path = Path("pic/")
norm_features = readFeature("norm.txt")
unnorm_features = readFeature("unnorm.txt")
files = [ info[0:2] for info in norm_features]

# Decorator 裝飾器 -> 給函式附加功能
@app.route("/")
def home():
    rand_pic = random.randint(0, 199)
    imgs = []
    for class_idx in range(50):
        img_idx = rand_pic + class_idx * 200
        with open(pic_path / files[img_idx][1] / files[img_idx][0], "rb") as file:
            imgs.append([files[img_idx][0], files[img_idx][1], b64encode(file.read()).decode("utf-8")])
    # [圖片名稱, 圖片類別, 圖片的二進位資料]
    return render_template("home.html", imgs=imgs)

@app.route("/search")
def search():
    img_info = request.values
    methods = {
        "Euclidean Distance": 0,
        "Cosine Similarity": 1,
        "PCC": 2
    }
    """
        "norm":     Normalize / Unnormalize
        "method":   Euclidean Distance / Consine Similarity / PCC
        "img_filename": (filename of the img)
        "img_class": (the class of the img)
    """
    for selected_img_idx in range(10000):
        if files[selected_img_idx][0] == img_info["img_filename"]:
            break
    if img_info["norm"] == "Normalize":
        all_distance = distance(selected_img_idx, norm_features, methods[img_info["method"]])
    else:
        all_distance = distance(selected_img_idx, unnorm_features, methods[img_info["method"]])
    similar_imgs_idx = searching(methods[img_info["method"]], all_distance)
    similar_imgs = []
    accuracy = 0.0
    for img_idx in similar_imgs_idx:
        with open(pic_path / files[img_idx][1] / files[img_idx][0], "rb") as file:
            similar_imgs.append([files[img_idx][0], b64encode(file.read()).decode("utf-8")])
        if files[img_idx][1] == img_info["img_class"]:
            accuracy += 1
    selected_img = None
    with open(pic_path / files[selected_img_idx][1] / files[selected_img_idx][0], "rb") as file:
        selected_img = [files[selected_img_idx][0], b64encode(file.read()).decode("utf-8")]
    return render_template("imgSearch.html", selected_img=selected_img, similar_imgs=similar_imgs, accuracy=accuracy)


if __name__ == "__main__":
    app.debug = True
    app.run()