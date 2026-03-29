import math

def euclidean_distance(point1, point2):
    # Check if input is tuple or list
    if not isinstance(point1, (tuple, list)) or not isinstance(point2, (tuple, list)):
        return "Error: Inputs must be tuples or lists"
    # Check if both inputs have the same dimension
    if len(point1) != len(point2):
        return "Error: Both inputs should have the same dimension"
    
    # Compute the Euclidean distance    
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    
    return math.sqrt(distance)