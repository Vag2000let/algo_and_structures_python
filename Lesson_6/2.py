"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""
from pympler import asizeof
from sys import getsizeof


class Toy:
    def __init__(self, type, name, name_1):
        self.type = type
        self.name = name
        self.name_1 = name_1


class Car(Toy):
    def form(self):
        print('Закупка сырья')

    def bodywork(self):
        print('Изготовление кузова')

    def color(self):
        print('Кузов машины окрашен')


my_car = Car('car', 'Skoda', 'Czech')



class ToyFactory:
    def __init__(self):
        super().__init__(Toy)
        self.my_car = my_car

    def create_toy(self):
        print('Cоздан экземпляр: ', self.type, self.name, self.name_1)


ToyFactory.create_toy(my_car)

my_car = Car('car', 'Skoda', 'Czech')
print(my_car.__dict__)
print(f'asizeof - {asizeof.asizeof(my_car)}')
print(f'getsizeof - {getsizeof(my_car)}')
my_car.name_2 = 'Felicia'
print(my_car.__dict__)
print(f'asizeof - {asizeof.asizeof(my_car)}')
print(f'getsizeof - {getsizeof(my_car)}')


class Toy:
    __slots__ = ['type', 'name', 'name_1']

    def __init__(self, type, name, name_1):
        self.type = type
        self.name = name
        self.name_1 = name_1


class Car(Toy):
    def form(self):
        print('Закупка сырья')

    def bodywork(self):
        print('Изготовление кузова')

    def color(self):
        print('Кузов машины окрашен')


my_car_2 = Car('car', 'Skoda', 'Czech')



class ToyFactory:
    def __init__(self):
        super().__init__(Toy)
        self.my_car_2 = my_car_2

    def create_toy(self):
        print('Cоздан экземпляр: ', self.type, self.name, self.name_1)


ToyFactory.create_toy(my_car_2)

my_car_2 = Car('car', 'Skoda', 'Czech')
print(my_car_2.__slots__)
print(f'asizeof - {asizeof.asizeof(my_car_2)}')
print(f'getsizeof - {getsizeof(my_car_2)}')

# СЛОВАРЬ:
# Cоздан экземпляр:  car Skoda Czech
# {'type': 'car', 'name': 'Skoda', 'name_1': 'Czech'}
# asizeof - 504
# getsizeof - 56
# {'type': 'car', 'name': 'Skoda', 'name_1': 'Czech', 'name_2': 'Felicia'}
# asizeof - 616
# getsizeof - 56

# КОРТЕЖ:
# Cоздан экземпляр:  car Skoda Czech
# ['type', 'name', 'name_1']
# asizeof - 360
# getsizeof - 80
