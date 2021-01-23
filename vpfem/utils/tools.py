from numpy import sqrt

def dimension_checker(input_list, correct_size):
    if len(input_list) != correct_size:
        raise Exception("Wrong dimention for this node")
    return len(input_list)

def int_type_checker(input_arg):
    if not isinstance(input_arg, int):
        raise Exception("Please enter integer")
    return input_arg

def check_size(input_list, limit):
    if not len(input_list) == limit:
        raise Exception("Wrong number of inputs")
    return input_list

def distance_nodes(node_i, node_j):
    sqrt_value = 0
    for i in range(node_i.get_dim()):
        sqrt_value += (node_i.coordinate[i] - node_j.coordinate[i])**2
    return sqrt(sqrt_value)
