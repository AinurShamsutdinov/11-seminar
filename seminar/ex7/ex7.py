#   Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать, ○ сравнения,
# ○ сложения,
# ○ *умножения матриц


class Matrix(object):
    """Class for matrix and mathematics operations on matrix"""
    __matrix = tuple()

    def __init__(self, tuple_matrix):
        self.matrix = tuple_matrix

    def __str__(self):
        """Get the string representation of the matrix"""
        str_matrix: str
        for item in self.__matrix:
            str_matrix += item
            str_matrix += '\n'
        return str_matrix

    def __repr__(self):
        """Get the formatted string representation of the matrix"""
        return f'Rectangle({self.depth}, {self.length})'

    def __eq__(self, other):
        """Check if two matrices are equal"""
        if len(self.__matrix) == len(self.__matrix):
            for item_one, item_two in self.__matrix, other.__matrix:
                if item_one != item_two:
                    return False
        return True


first = (1, 2, 3)
second = (1, 3, 4)
third = (10, 20, 49)
fourth = (32, 32, 42)
matrix_one = (first, second, third)
matrix_two = (first, second, fourth)
matrix_three = (first, second, third)
print('matrix_one == matrix_two is ', matrix_one == matrix_two)
print('matrix_one == matrix_three is ', matrix_one == matrix_three)
print(f'{matrix_one = }')
