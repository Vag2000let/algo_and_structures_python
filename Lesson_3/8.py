"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
from random import randint

M = []

for i in range(4):
    small_list = []
    for j in range(5):
        small_list.append(randint(1, 100))
    M.append(small_list)

for small in M:
    sum = 0
    for i in small:
        sum += i
        print(f'{i:3d}', end=' ')
    print(f'| {sum}')