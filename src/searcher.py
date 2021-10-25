import typing

def euclidean_distance(vec1, vec2):
    pass

def consine_distance(vec1, vec2):
    pass

def pcc_distance(vec1, vec2):
    pass

class searcher:
    similarity_funcs = {
        "euclidean": euclidean_distance,
        "consine": consine_distance,
        "pcc": pcc_distance
    }
    def __init__(self):
        self.__norm_data = {}
        self.__unnorm_data = {}
        
        with open("norm.txt", "r") as file:
            for line in file:
                line = line.split(" ")
                img_list = [line[1]] + [float(feature) for feature in line[2:]]
                self.__norm_data[line[1]] = img_list

        with open("unnorm.txt", "r") as file:
            for line in file:
                line = line.split(" ")
                img_list = [line[1]] + [float(feature) for feature in line[2:]]
                self.__unnorm_data[line[1]] = img_list

    def calcSimilarity(self, img1_name: str, img2_name: str, func: typing.Callable) -> float:
        pass

    def returnSimilarImgs(self, img_name: str, similarity_func_name: str, norm: bool) -> list:
        pass

if __name__ == "__main__":
    obj = searcher()