"""Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться."""

from random import randint


def task_7(lst_base):
    print(f'Исходный массив: {lst_base}')
    min_1 = min(lst_base)
    count = 0
    for el in lst_base:
        if el == min_1:
            lst_base.remove(el)
            count += 1
    print(f'Наименьший элемент: {min_1}, встречается в этом массиве {count} раз.')

    if count == 1:
        min_2 = min(lst_base)
        print(f'Второй наименьший элемент: {min_2}')


LST_BASE = [randint(-100, 100) for i in range(10)]
task_7(LST_BASE)
