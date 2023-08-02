# Задание No2
# 📌 Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# 📌 При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков- архивов
# 📌 list-архивы также являются свойствами экземпляра


class Archive:
    __number = 0
    __some_string = ''
    lst_numbers = list()
    lst_some_strings = list()

    def __new__(cls, number, some_str):
        cls.lst_numbers.append(number)
        cls.lst_some_strings.append(some_str)
        cls.__number = number
        cls.__some_string = some_str

    def __init__(self, number, some_str):
        self.__number = number
        self.__some_string = some_str

    def get_archive(self):
        return self.lst_numbers, self.lst_some_strings


archive = Archive(10, '10')
archive = Archive(20, '20')

print(archive.lst_numbers)
