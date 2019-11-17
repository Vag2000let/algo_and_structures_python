# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

NUMBER = int(input('Введите трехзначное число: '))
NUMBER_A = NUMBER // 100
NUMBER_B = (NUMBER // 10) % 10
NUMBER_C = NUMBER % 10
print(f'Сумма чисел: {NUMBER_A + NUMBER_B + NUMBER_C}, Произведение чисел: {NUMBER_A * NUMBER_B * NUMBER_C}')

