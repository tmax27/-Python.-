"""Задание_3.	В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы."""

# mass = [88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
# # min(mass), max(mass) = max(mass), min(mass)
# print(mass)

from random import randint


def task_3(lst):
    max_val = max(lst)
    min_val = min(lst)
    ind_max = lst.index(max_val)
    ind_min = lst.index(min_val)

    print(
        f'В данном массиве чисел максимальное число {max_val} стоит на {ind_max} позиции,'
        f'а минимальное число {min_val} стоит на {ind_min} позиции.')

    print('Заменяем их.')
    print(lst)

    lst[ind_max], lst[ind_min] = min_val, max_val
    ind_max = lst.index(max_val)
    ind_min = lst.index(min_val)
    print(
        f'В данном массиве чисел максимальное число {max_val} стоит на {ind_max} позиции,'
        f'а минимальное число {min_val} стоит на {ind_min} позиции.')

    print(lst)


LST = [randint(-100, 100) for i in range(10)]
task_3(LST)
