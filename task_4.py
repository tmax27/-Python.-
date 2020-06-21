"""Задание_4. Определить, какое число в массиве встречается чаще всего"""

import random


def task_4(lst):
    print(f'Исходный массив {lst}')
    numb = max(lst, key=lst.count)
    print(f'Число {numb} встречается {lst.count(numb)} раза.')


LST = [random.randint(-100, 100) for i in range(50)]
task_4(LST)
