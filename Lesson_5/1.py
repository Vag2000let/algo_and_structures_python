"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import namedtuple


ASC = int(input("Введите кол-во предприятий: "))
COMPANIES = namedtuple("company", "name quarter_1 quarter_2 quarter_3 quarter_4")
PROFIT_AVER = {}

for i in range(ASC):
    Company = COMPANIES(name=input("Введите название предприятия: "),
                        quarter_1=int(input("Введите прибыль за первый квартал: ")),
                        quarter_2=int(input("Введите прибыль за второй квартал: ")),
                        quarter_3=int(input("Введите прибыль за третий квартал: ")),
                        quarter_4=int(input("Введите прибыль за четвертый квартал: ")))
    PROFIT_AVER[Company.name] = (Company.quarter_1 + Company.quarter_2 + Company.quarter_3 + Company.quarter_4)

print(COMPANIES)

TOTAL_AVER = 0
for value in PROFIT_AVER.values():
    TOTAL_AVER += value
TOTAL_AVER = TOTAL_AVER / ASC


for key, value in PROFIT_AVER.items():
    if value > TOTAL_AVER:
        print(key, " - прибыль выше среднего")
    if value < TOTAL_AVER:
        print(key, " - прибыль ниже среднего")
    if value == TOTAL_AVER:
        print(key, " - средняя прибыль")
