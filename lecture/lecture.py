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
