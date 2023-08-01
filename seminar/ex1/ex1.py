# Задание No1
# 📌 Создайте класс Моя Строка, где:
# 📌 будут доступны все возможности str
# 📌 дополнительно хранятся имя автора строки и время создания (time.time)
import time


class MyStr(str):
    __author: str

    def __init__(self, author):
        self.__time = time.time()
        self.__author = author

    def get_author(self):
        return self.__author

my_str = MyStr('Testovich')

print(my_str.get_author())
