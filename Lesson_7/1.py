"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random
import timeit


# Стандартный подход
def bubble_sort(LIST):
    w = 1

    while w < len(LIST):
        for i in range(len(LIST) - w):
            if LIST[i] < LIST[i + 1]:
                LIST[i], LIST[i + 1] = LIST[i + 1], LIST[i]
        w += 1
    return LIST

# Дорабртанный
# Если за проход не совершается ни одной сортировки то прекращение

def bubble_sort_upgrade(LIST):
    q = 1
    no_sort = 0

    while q < len(LIST):
        for i in range(len(LIST) - q):
            if LIST[i] < LIST[i + 1]:
                LIST[i], LIST[i + 1] = LIST[i + 1], LIST[i]
                no_sort = 1
        if no_sort == 0:
            break
        q += 1
    return LIST


LIST = [random.randint(-100, 100) for i in range(10)]
print(bubble_sort(LIST))
print(bubble_sort_upgrade(LIST))

print(timeit.timeit("bubble_sort(LIST)", setup="from __main__ import bubble_sort, LIST"))
print(timeit.timeit("bubble_sort_upgrade(LIST)", setup="from __main__ import bubble_sort_upgrade, LIST"))
