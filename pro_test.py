class Matrix(object):
    def __init__(self, n_r, n_c):
        self.matrix = [[0 for i in range(n_c)] for j in range(n_r)]

    def my_at(self, i, j):
        return self.matrix[i][ j]

    def set(self, i, j, val):
        self.matrix[i][j] = val


m = Matrix(10, 8)
m.set(1, 2, 10)
print m.my_at(1, 2)