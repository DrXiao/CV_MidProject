import numpy as np

def euclidean_distance(vec1, vec2):
    # 歐幾里得距離: 越小越相近
    _sum = sum(((vec1 - vec2) ** 2))

    """
    for feature_index in range(feature_num):
        x = (vec1[feature_index])
        y = (vec2[feature_index])
        sum = sum + (x - y)**2
    """
    Eucl_similarity = _sum**0.5  # 最後的歐幾里得距離

    return Eucl_similarity


def consine_distance(vec1, vec2):
    # Cosine Similarity: 餘弦值越接近於1代表夾角越接近於0，向量上就越相似
    numerator = 0  # 分子
    denominator = 0  # 分母
    numerator = sum(vec1 * vec2)
    denominator = (sum(vec1 ** 2) ** 0.5) * (sum(vec2 ** 2) ** 0.5)

    """
    for feature_index in range(feature_num):
        numerator = (vec1[feature_index]) * \
            (vec2[feature_index]) + numerator
        A = (vec1[feature_index])**2 + A  # sigma (vec1)**2
        B = (vec2[feature_index])**2 + B  # sigma (vec2)**2
    denominator = (A**0.5) * (B**0.5)
    """
    consine_similarity = (numerator/denominator)  # 最後cosine距離

    return consine_similarity


def pcc_distance(vec1, vec2):
    # Pearson Correlation Coefficient:相關係數越高代表兩項目之間的關係越密切，反之則越不相關
    average1 = 0
    average2 = 0
    """
    for i in range(feature_num):
        average1 = average1 + (vec1[i])
        average2 = average2 + (vec2[i])
    average1 = average1/feature_num  # vec1的平均
    average2 = average2/feature_num  # vec2的平均
    """
    average1 = np.average(vec1)
    average2 = np.average(vec2)

    numerator = 0  # 分子
    denominator = 0  # 分母
    part1 = 0  # sigma (vec1 - average1)^2
    part2 = 0  # sigma (vec2 - average2)^2

    """
    for feature_index in range(feature_num):
        numerator = numerator + \
            ((vec1[feature_index]) - average1) * \
            ((vec2[feature_index])-average2)
        part1 = ((vec1[feature_index]) - average1)**2 + part1
        part2 = ((vec2[feature_index])-average2)**2 + part2
    denominator = (part1 ** 0.5)*(part2 ** 0.5)
    """
    numerator = sum((vec1 - average1) * (vec2 - average2))
    denominator = (sum((vec1-average1) ** 2) ** 0.5) * \
        (sum((vec2-average2) ** 2) ** 0.5)

    pcc_similarity = (numerator / denominator)  # 最後求得的PCC距離

    return pcc_similarity
