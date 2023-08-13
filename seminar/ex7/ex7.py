#   Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц
import np as np


# class Matrix(object):
class Matrix:
    """Class for matrix and mathematics operations on matrix"""
    __matrix = []

    def __init__(self, tuple_matrix):
        """Initiate matrix"""
        self.matrix = tuple_matrix

    def __str__(self):
        """Get the string representation of the matrix"""
        matrix_copy = self.get_matrix()
        str_matrix = ''
        for i in range(len(matrix_copy)):
            str_matrix = str_matrix + str(matrix_copy[i]) + '\n'
        return str_matrix

    def __repr__(self):
        """Get the formatted string representation of the matrix"""
        return f'Rectangle({self.depth}, {self.length})'

    def __eq__(self, other):
        """Compare two matrices"""
        this_matrix = self.get_matrix()
        other_matrix = other.get_matrix()
        """Check if two matrices are equal"""
        if len(this_matrix) == len(other_matrix):
            for i in range(len(this_matrix)):
                new_row = []
                for j in range(len(this_matrix[i])):
                    if this_matrix[i][j] != other_matrix[i][j]:
                        return False
        return True

    def __add__(self, other):
        """Summ two matrices"""
        this_matrix = self.get_matrix()
        other_matrix = other.get_matrix()
        matrix = []
        for i in range(len(this_matrix)):
            new_row = []
            for j in range(len(this_matrix[i])):
                new_row.append(this_matrix[i][j] + other_matrix[i][j])
            matrix.append(new_row)
        return Matrix(matrix)

    def __mul__(self, other):
        """Multiply two matrices"""
        mul_matrix = np.matmul(self.get_matrix(), other.get_matrix())
        return Matrix(mul_matrix)

    def get_matrix(self):
        return self.matrix


first = [1, 2, -2]
second = [3, 2, 0]
third = [-4, 0, 2]

fourth = [3, 4, 2]
fifth = [0, 1, 0]
sixth = [-2, 0, 1]


collect_one = [first, second, third]
collect_two = [fourth, fifth, sixth]
matrix_one = Matrix(collect_one)
matrix_two = Matrix(collect_two)
matrix_sum = matrix_one + matrix_two
matrix_mul = matrix_one * matrix_two
print('matrix_one == matrix_two is ', matrix_one == matrix_two)
print('matrix_one == matrix_fourth is ', matrix_one == matrix_sum)
print(f'{matrix_one}')
print(f'{matrix_two}')
print(f'{matrix_sum}')
print(f'{matrix_mul}')
