# Домашнее задание по теме "Создание исключений".

class Car:

    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model
        self.__vin = vin if self.__is_valid_vin(vin) is True else None
        self.__numbers = numbers if self.__is_valid_numbers(numbers) is True else None

    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int) and 9999999 >= vin_number >= 1000000:
            return True
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not 9999999 >= vin_number >= 1000000:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str) and len(numbers) == 6:
            return True
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')

class IncorrectVinNumber(Exception):

    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


# Пример выполняемого кода:

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
