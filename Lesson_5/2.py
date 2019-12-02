"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque

num_a = deque(input("Введите первое число: "))
num_b = deque(input("Введите второе число: "))


def hex_sum(num_a, num_b):
    num_a = "".join([i for i in num_a])
    num_b = "".join([i for i in num_b])
    sum = hex((int(float.fromhex(num_a) + float.fromhex(num_b))))
    sum = deque(sum[2::].upper())
    print("Сумма: ", sum)


def hex_mul(num_a, num_b):
    num_a = "".join([i for i in num_a])
    num_b = "".join([i for i in num_b])
    sum = hex((int(float.fromhex(num_a) * float.fromhex(num_b))))
    sum = deque(sum[2::].upper())
    print("Произведение: ", sum)


hex_sum(num_a, num_b)
# hex_mul(num_a, num_b)