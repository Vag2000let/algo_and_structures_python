"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint

M = []
NUMBERS = int(input("Введите длину массива: "))

while len(M) < NUMBERS:
    M.append(randint(1, 100))
print(f'Исходный список {M}')

MAX_NUM = M[0]
MIN_NUM = M[0]
POS_MAX, POS_MIN = 0, 0
SUM = 0
for i in range(len(M)):
    # находим максимальное значение и его индекс
    if M[i] > MAX_NUM:
        MAX_NUM = M[i]
        POS_MAX = i
    # находим минимальное значение и его индекс
    if M[i] < MIN_NUM:
        MIN_NUM = M[i]
        POS_MIN = i
if POS_MAX > POS_MIN:
    for j in range(POS_MIN + 1, POS_MAX):
        SUM += M[j]
else:
    for j in range(POS_MAX + 1, POS_MIN):
        SUM += M[j]
print(f'Максимальное число: {MAX_NUM}, индекс: {POS_MAX}, Минимальное число: {MIN_NUM}, индекс: {POS_MIN}')
print(f'Сумма чисел между максимальным и минимальным элементами = {SUM}')
