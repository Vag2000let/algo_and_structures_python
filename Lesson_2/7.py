"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""


# abs(x) - Возвращает абсолютную величину (модуль числа).
NUMBER = abs(int(input("Введите число n: ")))
SUM = 0

for i in range(1, NUMBER + 1):
    SUM += i
if SUM == int(NUMBER * (NUMBER + 1) / 2):
    print(f"{SUM} == {int(NUMBER * (NUMBER + 1) / 2)}, равенство выполняется!")


def func_rec_sum(user_n, sum_n=0):
    if user_n == 0:
        return sum_n
    else:
        sum_n += user_n
        user_n -= 1
        return func_rec_sum(user_n, sum_n)


def comparison(n):
    if func_rec_sum(n) == int(n * (n + 1) / 2):
        print(f"{func_rec_sum(n)} == {int(n * (n + 1) / 2)}, равенство выполняется!")


user_n = abs(int(input("Введите число n: ")))
comparison(user_n)
