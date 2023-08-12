# Задание No5
# 📌 Дорабатываем класс прямоугольник из прошлого семинара.
# 📌 Добавьте возможность сложения и вычитания.
# 📌 При этом должен создаваться новый экземпляр прямоугольника.
# 📌 Складываем и вычитаем периметры, а не длинну и ширину.
# 📌 При вычитании не допускайте отрицательных значений.


class Rectangle(object):
    length: int
    depth: int

    def __init__(self, length, depth):
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
        return (self.length + self.depth) * 2

    def area(self):
        return self.length * self.depth

    def __add__(self, other):
        sum_perimeters = self.perimeter() + other.perimeter()
        sum_sides = sum_perimeters / 2
        return Rectangle(int(sum_sides / 2), int(sum_sides / 2))

    def __sub__(self, other):
        sub_perimeters: int
        sub_sides: int
        if self.perimeter() > other.perimeter():
            sub_perimeters = self.perimeter() - other.perimeter()
            sub_sides = sub_perimeters / 2
            return Rectangle(int(sub_sides / 2), int(sub_sides / 2))
        return None


first = Rectangle(10, 20)
second = Rectangle(30, 50)

summ = first + second
sub = second - first

print(summ.depth, summ.length)
print(sub.depth, sub.length)

