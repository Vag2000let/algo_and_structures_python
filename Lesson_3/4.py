# 4.	Определить, какое число в массиве встречается чаще всего.


M = [1, 1, 3, 3, 3, 2]
POS = 0
NUMBER = M[0]
for i in range(len(M)):
    if M.count(i) > NUMBER:
        NUMBER = M.count(i)
        POS = i
print(f'Чаще всего встречается число {NUMBER}, {POS} раз(а)')
