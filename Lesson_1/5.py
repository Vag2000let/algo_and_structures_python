#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

import sys


try:
    A = ord(input('Введите 1-ую букву: '))
    B = ord(input('Введите 2-ую букву: '))
except:
    print('Введите буквы')
    sys.exit(1)

if A == B:
    print('Введены одинаковые буквы')
    sys.exit(1)

A = A - ord('a') + 1
B = B - ord('a') + 1

print(f'Номер позиции: {A} и {B}')
print(f'Символов между буквами: {abs(A - B) - 1}')
