#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.


from random import randint

M = []
NUMBERS = int(input("Введите длину массива: "))

while len(M) < NUMBERS:
    M.append(randint(1, 100))
print(f'Исходный список {M}')

MAX_NUM = M[0]
MIN_NUM = M[0]
POS_MAX, POS_MIN = 0, 0
for i in range(len(M)):
    # находим максимальное значение и его индекс
    if M[i] > MAX_NUM:
        MAX_NUM = M[i]
        POS_MAX = i
    # находим минимальное значение и его индекс
    if M[i] < MIN_NUM:
        MIN_NUM = M[i]
        POS_MIN = i
print(f'Максимальное число: {MAX_NUM}, индекс: {POS_MAX}, Минимальное число: {MIN_NUM}, индекс: {POS_MIN}')
# меняем значения местами
M[POS_MIN] = MAX_NUM
M[POS_MAX] = MIN_NUM
print(f'Список после замены местами максимального и минимально: {M}')



