import numpy as np

def magnitude(vector):
    sum_squares = sum([np.power(vector[x],2) for x in range(0,len(vector))])
    return np.sqrt(sum_squares)

def angle_between(vector1,vector2):
    dot_product = np.dot(vector1,vector2)
    return np.arccos(dot_product/(magnitude(vector1)*magnitude(vector2)))

def euclidean_distance(point1,point2):
    assert len(point1) == len(point2)
    summation = sum([np.power(point1[i]-point2[i],2) for i in range(0,len(point1))])
    return np.sqrt(summation)