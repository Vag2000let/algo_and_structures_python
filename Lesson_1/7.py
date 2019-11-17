"""
7.	По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой
треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""

A = int(input('Введите длину отрезка a: '))
B = int(input('Введите длину отрезка b: '))
C = int(input('Введите длину отрезка c: '))

# треугольник существует тогда и только тогда,
# когда сумма любых двух его сторон больше третьей стороны.
if A + B <= C or A + C <= B or B + C <= A:
    print('Треугольник не существует!')
if A != B and A != C and B != C:
    print('Треугольник разносторонний')
elif A == B == C:
    print('Треугольник равносторонний')
elif A == B or B == C or A == C:
    print('Треугольник равнобедренный')




