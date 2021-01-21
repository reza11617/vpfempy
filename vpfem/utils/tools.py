def dimension_checker(inputList, correctSize):
    if len(inputList) != correctSize:
        raise Exception("Wrong dimention for this node")
    return len(inputList)

def int_type_checker(x):
    if not type(x) is int:
        raise TypeError("Only integers are allowed")
    return x

def check_size(x, limit):
    if len(x) == limit:
        return x
    else:
        raise Exception("Wrong number of inputs")
