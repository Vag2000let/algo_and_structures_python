"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

N = int(input("Количество элементов: "))
S_N = 0
NUM_EL = 1
for i in range(N):
    S_N += NUM_EL
    NUM_EL /= -2
print(f'Суммма элементов {S_N}')


def rec_func(n, s_n=0, num_el=1):
    if n == 0:
        return s_n
    else:
        s_n += num_el
        num_el /= 2
        n -= 1
        return rec_func(n, s_n, num_el)


print(rec_func(10))
