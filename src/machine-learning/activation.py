
class Activation:
    def __init__():
        pass
    def ele_mul(pred, true, input, matrix, alpha):
        assert(len(pred) == len(true))
        for x, i in enumerate(matrix):
            for y, j in enumerate(i):
                matrix[x][y] = j - (((pred[y] - true[y]) * input[y]) * alpha)
        return matrix
