# 5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.
from random import randint

M = []
NUMBERS = int(input("Введите длину массива: "))

while len(M) < NUMBERS:
    M.append(randint(-100, 100))
print(f'Исходный список {M}')

MAX_MIN_NUM = M[0]
POS_MAX_MIN = 0

for i in range(len(M)):
    if 0 > M[i] > MAX_MIN_NUM:
        MAX_MIN_NUM = M[i]
        POS_MAX_MIN = i

print(f'Максимально отрицательный элемент: {MAX_MIN_NUM}, позиция {POS_MAX_MIN}')
