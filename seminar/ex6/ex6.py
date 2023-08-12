# Задание No6
# 📌 Доработайте прошлую задачу.
# 📌 Добавьте сравнение прямоугольников по площади
# 📌 Должны работать все шесть операций сравнения


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

    def __eq__(self, other):
        first = self.area()
        second = other.area()
        return first == second

    def __ne__(self, other):
        first = self.area()
        second = other.area()
        return first != second

    def __gt__(self, other):
        first = self.area()
        second = other.area()
        return first > second

    def __le__(self, other):
        first = self.area()
        second = other.area()
        return first <= second

    def __lt__(self, other):
        first = self.area()
        second = other.area()
        return first < second

    def __ge__(self, other):
        first = self.area()
        second = other.area()
        return first >= second


first_rec = Rectangle(10, 20)
second_rec = Rectangle(20, 10)
third_rec = Rectangle(30, 30)

print('first == second ', (first_rec == second_rec))
print('first != second ', first_rec != second_rec)
print('first != third ', first_rec != third_rec)
print('first > second ', first_rec > second_rec)
print('third > first ', third_rec > first_rec)
print('first <= second ', first_rec <= second_rec)
print('first <= third ', first_rec <= third_rec)
print('first < second ', first_rec < second_rec)
print('first < third ', first_rec < third_rec)
print('first >= second ', first_rec >= second_rec)
print('third >= second ', third_rec >= second_rec)
