def matrix_pruduct(a, b):
    if (check_matrix(a)):
        if (check_matrix(b)):
            return [[sum(a[i][k] * b[k][j] for k in range(len(a[0]))) for j in range(len(b[0]))] for i in range(len(a))]
        else:
            return "b is not a matrix"
    else:
        return "a is not a matrix"


def tensor_product(a, b):

        else:
            return "b is not a matrix"
    else:
        return "a is not a matrix"


def check_matrix(a):
    if (type(a) == list):
        for i in a:
            for j in i:
                if (type(j) != int and type(j) != float):
                    return False

                if (len(a[0]) != len(i)):
                    return False
        return True
    else:
        return False


a = [[1, 2, 3]]
b = [[1, 2], [3, 4]]
print(tensor_product(a, b))
