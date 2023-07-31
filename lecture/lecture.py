# class User:
#     def __init__(self, name: str, equipment: list = None):
#         self.name = name
#         self.equipment = equipment if equipment is not None else []
#         self.life = 3
#         # принтим только в учебных целях, а не для реальных задач
#         print(f'Создал {self} со свойствами:\n {self.name = },\t{self.equipment = },\t{self.life = }')
#
#
# print('Создаём первый раз')
# u_1 = User('Спенглер')
# print('Создаём второй раз')
# u_2 = User('Венкман', ['протонный ускоритель', 'ловушка'])
# print('Создаём третий раз')
# u_3 = User(equipment=['ловушка', 'прибор ночного видения'], name='Стэнц')
########################################################################################################
# class User:
#     def __init__(self, name: str):
#         self.name = name
#         print(f'Создал {self.name = }')
#
#     def __new__(cls, *args, **kwargs):
#         instance = super().__new__(cls)
#         print(f'Создал класс {cls}')
#         return instance
#
#
# print('Создаём первый раз')
# u_1 = User('Спенглер')
# print('Создаём второй раз')
# u_2 = User('Венкман')
# print('Создаём третий раз')
# u_3 = User(name='Стэнц')
########################################################################################################
# class NamedInt(int):
#     def __new__(cls, value, name, test):
#         instance = super().__new__(cls, value)
#         instance.name = name
#         instance.test = 'Test fuck it'
#         print(f'Создал класс {cls}')
#         return instance
#
#
# print('Создаём первый раз')
# a = NamedInt(42, 'Главный ответ жизни, Вселенной и вообще', 'test a')
# print('Создаём второй раз')
# b = NamedInt(73, 'Лучшее просто число', 'test b')
# print(f'{a = }\t{a.name = }\t{type(a) = }\t{a.test}')
# print(f'{b = }\t{b.name = }\t{type(b) = }\t{b.test}')
# c = a + b   # name and test do nothing when you add the numbers
# print(f'{c = }\t{type(c) = }')
########################################################################################################
# class Singleton:
#     _instance = None
#     count = 0
#
#     def __new__(cls, *args, **kwargs):
#         cls.count += 1
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
#     def __init__(self, name: str):
#         self.name = name
#
#
# a = Singleton('Первый')
# print(f'{a.name = }\t{a.count = }')
# b = Singleton('Второй')
# d = Singleton('Third')
# print(f'{a is b = }\t{b.count = }')
# print(f'{a.name = }\n{b.name = }')
# print(f'{d.name = }\t{d.count = }')
########################################################################################################
# class User:
#     def __init__(self, name: str):
#         self.name = name
#         print(f'Создал {self.name = }')
#
#     def __del__(self):
#         print(f'Удаление экземпляра {self.name}')
#
#
# u_1 = User('Спенглер')
# input('Enter num ')
# u_2 = User('Венкман')
########################################################################################################
# import sys
#
#
# class User:
#
#     def __init__(self, name: str):
#         self.name = name
#         print(f'Создал {self.name = }')
#
#     def __del__(self):
#         print(f'Удаление экземпляра {self.name}')
#
#
# u_1 = User('Спенглер')
# print(sys.getrefcount(u_1))
# u_2 = u_1
# print(sys.getrefcount(u_1), sys.getrefcount(u_2))
# del u_1
# print(sys.getrefcount(u_2))     #   get the number of references
# print('Завершение работы')
########################################################################################################
# class User:
#     """A User training class for demonstrating class documentation.
#         Shows the operation of the help(cls) and the dander method __doc__"""
#
#     def __init__(self, name: str):
#         """Added the name parameter."""
#         self.name = name
#
#     def simple_method(self):
#         """Example of a simple method."""
#         self.name.capitalize()
#
#
# u_1 = User('Спенглер')
# print('Справка класса User ниже', '*' * 50)
# help(User)
# print('Справка экземпляра u_1 ниже', '*' * 50)
# help(u_1)
########################################################################################################
# class User:
#     """A User training class for demonstrating classvdocumentation.
#     Shows the operation of the help(cls) and the dander method __doc__"""
#
#     def __init__(self, name: str):
#         """Added the name parameter."""
#         self.name = name
#         print(f'Создал {self.name = }')
#
#     def simple_method(self):
#         """Example of a simple method."""
#         self.name.capitalize()
#
#
# u_1 = User('Спенглер')
# print(f'Документация класса: {User.__doc__ = }')
# print(f'Документация экземпляра: {u_1.__doc__ = }')
# print(f'Документация метода: {u_1.simple_method.__doc__}')
########################################################################################################
# class User:
#
#     def __init__(self, name: str):
#         """Added the name parameter."""
#         self.name = name
#
#     def simple_method(self):
#         """Example of a simple method."""
#         self.name = self.name.capitalize()
#
#
# user = User('Спенглер')
# user.simple_method()
# print(user)
# print(f'{user.name = }')
########################################################################################################
# class User:
#
#     def __init__(self, name: str):
#         """Added the name parameter."""
#         self.name = name
#
#     def simple_method(self):
#         """Example of a simple method."""
#         self.name.capitalize()
#
#     def __str__(self):
#         return f'Экземпляр класса User с именем "{self.name}"'
#
#
# user = User('Спенглер')
# print(user)
########################################################################################################
# class User:
#
#     def __init__(self, name: str):
#         """Added the name parameter."""
#         self.name = name
#
#     def simple_method(self):
#         """Example of a simple method."""
#         self.name.capitalize()
#
#     def __repr__(self):
#         return f'User({self.name}) test'
#
#
# user = User('Спенглер')
# print(user)
########################################################################################################
# class User:
#
#     def __init__(self, name: str, equipment: list = None):
#         self.name = name
#         self.equipment = equipment if equipment is not None else []
#         self.life = 3
#
#     def __repr__(self):
#         return f'User({self.name}, {self.equipment})'
#
#
# user = User('Венкман', ['протонный ускоритель', 'ловушка'])
# print(user)
########################################################################################################
# class User:
#
#     def __init__(self, name: str, equipment: list = None):
#         self.name = name
#         self.equipment = equipment if equipment is not None else []
#         self.life = 3
#
#     def __str__(self):
#         eq = 'оборудованием: ' + ', '.join(self.equipment) if self.equipment else 'пустыми руками'
#         return f'Перед нами {self.name} с {eq}. Количество жизней - {self.life}'
#
#     def __repr__(self):
#         return f'User({self.name}, {self.equipment})'
#
#
# user = User('Венкман', ['протонный ускоритель', 'ловушка'])
# print(user)
# print(f'{user}')
#
# print(repr(user))
# print(f'{user = }')
########################################################################################################
# class User:
#
#     def __init__(self, name: str, equipment: list = None):
#         self.name = name
#         self.equipment = equipment if equipment is not None else []
#         self.life = 3
#
#     def __str__(self):
#         eq = 'оборудованием: ' + ', '.join(self.equipment) if self.equipment else 'пустыми руками'
#         return f'Перед нами {self.name} с {eq}. Количество жизней - {self.life}'
#
#     def __repr__(self):
#         return f'User({self.name}, {self.equipment})'
#
#
# u_1 = User('Спенглер')
# u_2 = User('Венкман', ['протонный ускоритель', 'ловушка'])
# u_3 = User(equipment=['ловушка', 'прибор ночного видения'], name='Стэнц')
# ghostbusters = [u_1, u_2, u_3]
#
# print(ghostbusters)
# print(f'{ghostbusters}')
# print(repr(ghostbusters))
# print(f'{ghostbusters = }')
#
# print(*ghostbusters, sep='\n')
########################################################################################################
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return f'Vector({self.x}, {self.y})'
#
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector(x, y)
#
#
# a = Vector(2, 4)
# b = Vector(3, 7)
# c = a + b
# print(f'{a = }\t{b = }\t{c = }')
########################################################################################################
# from random import choices
#
#
# class Closet:
#     CLOTHES = ('брюки', 'рубашка', 'костюм', 'футболка', 'перчатки', 'носки', 'туфли')
#
#     def __init__(self, count: int, storeroom=None):
#         self.count = count
#         if storeroom is None:
#             self.storeroom = choices(self.CLOTHES, k=count)
#         else:
#             self.storeroom = storeroom
#
#     def __str__(self):
#         names = ', '.join(self.storeroom)
#         return f'Осталось вещей в шкафу {self.count}:\n{names}'
#
#     def __rshift__(self, other):
#         shift = self.count if other > self.count else other
#         self.count -= shift
#         return Closet(self.count, choices(self.storeroom, k=self.count))
#
#
# storeroom = Closet(10)
# print(storeroom)
# for _ in range(4):
#     storeroom = storeroom >> 3
#     print(storeroom)
########################################################################################################
class StrPro(str):

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        return instance

    def __rmul__(self, other: str):
        words = other.split()
        result = self.join(words) + ' test '
        return StrPro(result)


text = 'Каждый охотник желает знать где сидит фазан'
s = StrPro(' (=^.^=) ')
print(f'{text = }\n{s = }')
print(text * s)
# print(s * text)     # TypeError: 'str' object cannot be interpreted as an integer
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
