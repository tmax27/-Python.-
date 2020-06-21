"""Задание_5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве."""

from random import randint


def task_5(lst_base):
    print(f'Базовый список: {lst_base}')
    lst = [el for el in lst_base if el < 0]
    print(f'Максимальный отрицательный элемент в данном массиве = {max(lst)}, '
          f'его индекс {lst_base.index(max(lst))}')


LST_BASE = [randint(-100, 100) for i in range(10)]
task_5(LST_BASE)
