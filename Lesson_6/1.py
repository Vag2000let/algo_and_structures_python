"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""
from random import randint
from math import inf
from memory_profiler import profile


@profile()
def test_1(number):
    c = 0
    n = 0
    while number != 0:
        if (number % 10) % 2 == 0:
            c += 1
            number = number // 10
        else:
            n += 1
            number = number // 10
    return c, n


test_1(1000)


@profile()
def test_2(numbers):
    m = []
    while len(m) < numbers:
        m.append(randint(-10, 10))
    print(f'Исходный список {m}')

    max_min_num = m[0]
    pos_max_min = 0

    for i in range(len(m)):
        if 0 > m[i] > max_min_num:
            max_min_num = m[i]
            pos_max_min = i

    print(f'Максимально отрицательный элемент: {max_min_num}, позиция {pos_max_min}')


test_2(100)

@profile()
def test_3():
    def get_expand_matrix(matrix):
        """Разворачивает матрицу на 90 градусов"""
        m = []
        for elem in range(0, len(matrix[0])):
            new_list = []
            for num in range(0, len(matrix)):
                new_list.append(matrix[num][elem])
            m.append(new_list)
        return m

    def get_min_col_list(matrix):
        """Возвращает по одному минимальному элементы из каждого столбца матрицы в виде списка"""
        min = []
        for elem in matrix:
            min_num = float(inf)
            for num in range(len(elem)):
                if elem[num] < min_num:
                    min_num = elem[num]
                if num == len(elem) - 1:
                    min.append(min_num)
        return min

    m = []
    ROW = 200
    COL = 200

    for i in range(ROW):
        small_list = []
        for j in range(COL):
            small_list.append(randint(-100, 100))
        m.append(small_list)

    for small in m:
        for i in small:
            print(f'{i:4d}', end=' ')
        print()

    MIN_LIST = get_min_col_list(get_expand_matrix(m))

    MAX_ELEM = -float(inf)
    for i in MIN_LIST:
        if i > MAX_ELEM:
            MAX_ELEM = i

    print(f'Максимальный элемент из минимальных элементов столбцов матрицы - "{MAX_ELEM}"')


test_3()

# Windows 10 x64
# ОЗУ: 12GB
# Python 3.7.4

# test_1
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     14     16.7 MiB     16.7 MiB   @profile()
#     15                             def test_1(number):
#     16     16.7 MiB      0.0 MiB       c = 0
#     17     16.7 MiB      0.0 MiB       n = 0
#     18     16.7 MiB      0.0 MiB       while number != 0:
#     19     16.7 MiB      0.0 MiB           if (number % 10) % 2 == 0:
#     20     16.7 MiB      0.0 MiB               c += 1
#     21     16.7 MiB      0.0 MiB               number = number // 10
#     22                                     else:
#     23     16.7 MiB      0.0 MiB               n += 1
#     24     16.7 MiB      0.0 MiB               number = number // 10
#     25     16.7 MiB      0.0 MiB       return c, n

# test_2
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     33     16.6 MiB     16.6 MiB   @profile()
#     34                             def test_2(numbers):
#     35     16.6 MiB      0.0 MiB       m = []
#     36     16.6 MiB      0.0 MiB       while len(m) < numbers:
#     37     16.6 MiB      0.0 MiB           m.append(randint(-10, 10))
#     38     16.6 MiB      0.0 MiB       print(f'Исходный список {m}')
#     39
#     40     16.6 MiB      0.0 MiB       max_min_num = m[0]
#     41     16.6 MiB      0.0 MiB       pos_max_min = 0
#     42
#     43     16.6 MiB      0.0 MiB       for i in range(len(m)):
#     44     16.6 MiB      0.0 MiB           if 0 > m[i] > max_min_num:
#     45                                         max_min_num = m[i]
#     46                                         pos_max_min = i
#     47
#     48     16.6 MiB      0.0 MiB       print(f'Максимально отрицательный
#     элемент: {max_min_num}, позиция {pos_max_min}')

# test_3 (ROW = 100, COL = 100)
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     52     16.6 MiB     16.6 MiB   @profile()
#     53                             def test_3():
#     54     16.8 MiB      0.0 MiB       def get_expand_matrix(matrix):
#     55                                     """Разворачивает матрицу на 90 градусов"""
#     56     16.8 MiB      0.0 MiB           m = []
#     57     16.9 MiB      0.0 MiB           for elem in range(0, len(matrix[0])):
#     58     16.9 MiB      0.0 MiB               new_list = []
#     59     16.9 MiB      0.0 MiB               for num in range(0, len(matrix)):
#     60     16.9 MiB      0.0 MiB                   new_list.append(matrix[num][elem])
#     61     16.9 MiB      0.0 MiB               m.append(new_list)
#     62     16.9 MiB      0.0 MiB           return m
#     63
#     64     16.9 MiB      0.0 MiB       def get_min_col_list(matrix):
#     65                                     """Возвращает по одному минимальному
#     элементы из каждого столбца матрицы в виде списка"""
#     66     16.9 MiB      0.0 MiB           min = []
#     67     16.9 MiB      0.0 MiB           for elem in matrix:
#     68     16.9 MiB      0.0 MiB               min_num = float(inf)
#     69     16.9 MiB      0.0 MiB               for num in range(len(elem)):
#     70     16.9 MiB      0.0 MiB                   if elem[num] < min_num:
#     71     16.9 MiB      0.0 MiB                       min_num = elem[num]
#     72     16.9 MiB      0.0 MiB                   if num == len(elem) - 1:
#     73     16.9 MiB      0.0 MiB                       min.append(min_num)
#     74     16.9 MiB      0.0 MiB           return min
#     75
#     76     16.6 MiB      0.0 MiB       m = []
#     77     16.6 MiB      0.0 MiB       ROW = 100
#     78     16.6 MiB      0.0 MiB       COL = 100
#     79
#     80     16.8 MiB      0.0 MiB       for i in range(ROW):
#     81     16.8 MiB      0.0 MiB           small_list = []
#     82     16.8 MiB      0.1 MiB           for j in range(COL):
#     83     16.8 MiB      0.0 MiB               small_list.append(randint(-100, 100))
#     84     16.8 MiB      0.0 MiB           m.append(small_list)
#     85
#     86     16.8 MiB      0.0 MiB       for small in m:
#     87     16.8 MiB      0.0 MiB           for i in small:
#     88     16.8 MiB      0.0 MiB               print(f'{i:4d}', end=' ')
#     89     16.8 MiB      0.0 MiB           print()
#     90
#     91     16.9 MiB      0.0 MiB       MIN_LIST = get_min_col_list(get_expand_matrix(m))
#     92
#     93     16.9 MiB      0.0 MiB       MAX_ELEM = -float(inf)
#     94     16.9 MiB      0.0 MiB       for i in MIN_LIST:
#     95     16.9 MiB      0.0 MiB           if i > MAX_ELEM:
#     96     16.9 MiB      0.0 MiB               MAX_ELEM = i
#     97
#     98     16.9 MiB      0.0 MiB       print(f'Максимальный элемент из минимальных
#     элементов столбцов матрицы - "{MAX_ELEM}"')


# test_3 (ROW = 200, COL = 200)
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     52     16.6 MiB     16.6 MiB   @profile()
#     53                             def test_3():
#     54     17.5 MiB      0.0 MiB       def get_expand_matrix(matrix):
#     55                                     """Разворачивает матрицу на 90 градусов"""
#     56     17.5 MiB      0.0 MiB           m = []
#     57     17.8 MiB      0.0 MiB           for elem in range(0, len(matrix[0])):
#     58     17.8 MiB      0.0 MiB               new_list = []
#     59     17.8 MiB      0.0 MiB               for num in range(0, len(matrix)):
#     60     17.8 MiB      0.1 MiB                   new_list.append(matrix[num][elem])
#     61     17.8 MiB      0.0 MiB               m.append(new_list)
#     62     17.8 MiB      0.0 MiB           return m
#     63
#     64     17.8 MiB      0.0 MiB       def get_min_col_list(matrix):
#     65                                     """Возвращает по одному минимальному
#     элементы из каждого столбца матрицы в виде списка"""
#     66     17.8 MiB      0.0 MiB           min = []
#     67     17.8 MiB      0.0 MiB           for elem in matrix:
#     68     17.8 MiB      0.0 MiB               min_num = float(inf)
#     69     17.8 MiB      0.0 MiB               for num in range(len(elem)):
#     70     17.8 MiB      0.0 MiB                   if elem[num] < min_num:
#     71     17.8 MiB      0.0 MiB                       min_num = elem[num]
#     72     17.8 MiB      0.0 MiB                   if num == len(elem) - 1:
#     73     17.8 MiB      0.0 MiB                       min.append(min_num)
#     74     17.8 MiB      0.0 MiB           return min
#     75
#     76     16.6 MiB      0.0 MiB       m = []
#     77     16.6 MiB      0.0 MiB       ROW = 200
#     78     16.6 MiB      0.0 MiB       COL = 200
#     79
#     80     17.5 MiB      0.0 MiB       for i in range(ROW):
#     81     17.5 MiB      0.0 MiB           small_list = []
#     82     17.5 MiB      0.1 MiB           for j in range(COL):
#     83     17.5 MiB      0.1 MiB               small_list.append(randint(-100, 100))
#     84     17.5 MiB      0.0 MiB           m.append(small_list)
#     85
#     86     17.5 MiB      0.0 MiB       for small in m:
#     87     17.5 MiB      0.0 MiB           for i in small:
#     88     17.5 MiB      0.0 MiB               print(f'{i:4d}', end=' ')
#     89     17.5 MiB      0.0 MiB           print()
#     90
#     91     17.8 MiB      0.0 MiB       MIN_LIST = get_min_col_list(get_expand_matrix(m))
#     92
#     93     17.8 MiB      0.0 MiB       MAX_ELEM = -float(inf)
#     94     17.8 MiB      0.0 MiB       for i in MIN_LIST:
#     95     17.8 MiB      0.0 MiB           if i > MAX_ELEM:
#     96     17.8 MiB      0.0 MiB               MAX_ELEM = i
#     97
#     98     17.8 MiB      0.0 MiB       print(f'Максимальный элемент из минимальных
#     элементов столбцов матрицы - "{MAX_ELEM}"')


# test_1 и test_2 не замечены изменения в кол-ве потребления памяти
# при увеличении вводных данных.
# test_3 при увеличении кол-ва строк и столюцов в 2
# раза есть изменения в кол-ве потребления памяти.
