"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

NUMBER = int(input("Введите число: "))
REVERSE_ = 0

while NUMBER != 0:
    REVERSE_ = int((REVERSE_ + (NUMBER % 10) * 0.1) * 10)
    NUMBER = NUMBER // 10
print(f'{REVERSE_}')


def func_rec(number, reverse=0):
    if number == 0:
        return reverse
    else:
        reverse = int((reverse + (number % 10) * 0.1) * 10)
        number = number // 10
        return func_rec(number, reverse)


print(f'{func_rec(int(input("Введите число: ")))}')
