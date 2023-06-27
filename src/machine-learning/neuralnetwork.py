
class NeuralNetwork:
    """ класс простой нейронной сети """
    def __init__(self, input, weights):
        self.input = input
        self.weights = weights

    def neuralnetwork(self):
        """ метод возвращает предикцию"""
        def vect_mat_mut(vect, matrix):
            assert(len(vect) == len(matrix))
            output = [0, 0, 0]
            for i in range(len(vect)):
                output[i] = w_sum(vect, matrix[i])
            return output
        def w_sum(a, b):
            assert(len(a) == len(b))
            output = 0
            for i in range(len(a)):
                output += (a[i] * b[i])
            return output
        
        pred = vect_mat_mut(self.input, self.weights)
        return pred
        
