# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

import sys


try:
    A = int(input('Число 1: '))
    B = int(input('Число 2: '))
    C = int(input('Число 3: '))

    if A == B == C:
        print('Числа одинаковые')
        sys.exit(1)

    if B < A < C or C < A < B:
        print(f'Среднее цисло {A}')
    elif A < B < C or C < B < A:
        print(f'Среднее цисло {B}')
    else:
        print(f'Среднее цисло {C}')
except:
    print('Введите корректные данные')


