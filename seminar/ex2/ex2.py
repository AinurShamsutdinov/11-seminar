# Задание No2
# 📌 Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# 📌 При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков- архивов
# 📌 list-архивы также являются свойствами экземпляра


class Archive:
    """Class which save two data integer and string, and archive will all created instances of the class"""
    _old_instance = None
    __number = 0
    __some_string = ''
    __lst_numbers = list()
    __lst_some_strings = list()

    def __new__(cls, *args):
        """Create a new instance with two lists of old instances of the class"""

        instance = super().__new__(cls)
        instance.__number = args[0]
        instance.__some_string = args[1]
        if cls._old_instance is None:
            cls._old_instance = instance
        elif cls._old_instance is not None:
            if cls._old_instance is not None:
                instance.__lst_numbers = list(cls._old_instance.__lst_numbers)
                instance.__lst_numbers.append(cls._old_instance.__number)
            if cls._old_instance is not None:
                instance.__lst_some_strings = list(cls._old_instance.__lst_some_strings)
                instance.__lst_some_strings.append(cls._old_instance.__some_string)
            else:
                instance.__lst_some_strings = list()
        cls._old_instance = instance
        return instance

    def get_lst_numbers(self):
        """Get list of old integers"""

        return self.__lst_numbers

    def get_lst_some_strings(self):
        """Get list of old strings"""

        return self.__lst_some_strings

    def get_number(self):
        """Get current integer number"""

        return self.__number

    def get_some_string(self):
        """Get current string item"""

        return self.__some_string


archive = Archive(10, '11')
archive = Archive(20, '22')
archive = Archive(30, '33')
archive = Archive(40, '44')

print(f'{archive = }', type(archive))
print(f'{archive.get_number() = }')
print(f'{archive.get_some_string() = }')
print(f'{archive.get_lst_numbers() = }')
print(f'{archive.get_lst_some_strings() = }')
