"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""
from random import randint

M = []
NUMBERS = int(input("Введите длину массива: "))

while len(M) < NUMBERS:
    M.append(randint(-10, 10))
print(f'Исходный список {M}')

MAX_MIN_NUM = M[0]
MAX_MIN_NUM_1 = M[0]

for i in range(len(M)):
    if M[i] < MAX_MIN_NUM:
        MIN_NUM_2 = MAX_MIN_NUM
        MIN_NUM_1 = M[i]
    elif M[i] < MAX_MIN_NUM_1:
        MIN_NUM_2 = M[i]
print(f'Два минимальных элемента массива {MAX_MIN_NUM} и {MAX_MIN_NUM_1}')