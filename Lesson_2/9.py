"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


def func_delete(num):
    if len(str(num)) > 1:
        return (num - (num % 10)) // 10
    return num


def func_sum(num, my_sum):
    my_sum += num % 10
    if len(str(num)) <= 1:
        return my_sum
    return func_sum(func_delete(num), my_sum)


NUMBER_COUNT = int(input('Введите кол-во цифр для ввода: '))
SUM_NUM = 0

for i in range(NUMBER_COUNT):
    SUM_NUMBERS= int(input(f'Введите число номер {i + 1}: '))
    print(f'Сумма цифр числа {SUM_NUMBERS} = {func_sum(SUM_NUMBERS, SUM_NUM)}')