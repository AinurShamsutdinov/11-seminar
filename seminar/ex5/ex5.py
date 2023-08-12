# Задание No5
# 📌 Дорабатываем класс прямоугольник из прошлого семинара.
# 📌 Добавьте возможность сложения и вычитания.
# 📌 При этом должен создаваться новый экземпляр прямоугольника.
# 📌 Складываем и вычитаем периметры, а не длинну и ширину.
# 📌 При вычитании не допускайте отрицательных значений.


class Rectangle(object):
    """Class to represent a rectangle"""
    length: int
    depth: int

    def __init__(self, length, depth):
        """Initiate a rectangle"""
        if (length is None) or (depth is None):
            if length is not None:
                self.length = length
                self.depth = length
            elif depth is not None:
                self.length = depth
                self.depth = depth
        elif (length is not None) and (depth is not None):
            self.length = length
            self.depth = depth

    def perimeter(self):
        """Calculate the perimeter of a rectangle"""
        return (self.length + self.depth) * 2

    def area(self):
        """Calculate the area of a rectangle"""
        return self.length * self.depth

    def __add__(self, other):
        """Sum perimeters of two rectangles and get a new rectangle"""
        sum_perimeters = self.perimeter() + other.perimeter()
        sum_sides = sum_perimeters / 2
        return Rectangle(int(sum_sides / 2), int(sum_sides / 2))

    def __sub__(self, other):
        """Substuct perimeters if the result is bigger than 0 and return new Rectangle, else return None"""
        sub_perimeters: int
        sub_sides: int
        if self.perimeter() > other.perimeter():
            sub_perimeters = self.perimeter() - other.perimeter()
            sub_sides = sub_perimeters / 2
            return Rectangle(int(sub_sides / 2), int(sub_sides / 2))
        return None

    def __str__(self):
        """Get the string representation of the object"""
        return f'depth = {self.depth} length = {self.length}'

    def __repr__(self):
        """Get the formatted string representation of the object"""
        return f'Rectangle({self.depth}, {self.length})'


first = Rectangle(10, 20)
second = Rectangle(30, 50)

summ = first + second
sub = second - first

print(summ.depth, summ.length)
print(sub.depth, sub.length)
print(summ)
print(sub)
print(f'{summ = }')
print(f'{sub = }')

