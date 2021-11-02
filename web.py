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


@app.route("/")
def home():
    rand_pic = random.randint(0, 199)
    imgs = []
    for class_idx in range(50):
        img_idx = rand_pic + class_idx * 200
        with open(pic_path / files[img_idx][1] / files[img_idx][0], "rb") as file:
            imgs.append([files[img_idx][0], files[img_idx][1], b64encode(file.read()).decode("utf-8")])

    return render_template("home.html", imgs=imgs)

@app.route("/search")
def search():
    img = request.values
    print(img)
    print(img["img_filename"], img["img_class"])
    return render_template("imgSearch.html")


if __name__ == "__main__":
    app.debug = True
    app.run()