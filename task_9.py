"""Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы."""
from random import randint


def task_9(row_numb, col_numb):
    matrix = []
    for i in range(row_numb):
        string = []
        for j in range(col_numb):
            string.append(randint(0, 50))
            print(f'{string[j]:3}', end=' ')
        matrix.append(string)
        print()

    min_lst = []
    for i in range(col_numb):
        min_l = []
        for j in range(row_numb):
            min_l.append(matrix[j][i])
        min_lst.append(min(min_l))

    print(f'{min_lst} минимальные значения по столбцам')
    print(f'Максимальное среди них = {max(min_lst)}')


try:
    ROW_NUMB = int(input("Задайте количество строк в матрице: "))
    COL_NUMB = int(input("Задайте количество столбцов в матрице: "))
    task_9(ROW_NUMB, COL_NUMB)
except ValueError:
    print('Вы вместо числа ввели строку. Исправьтесь')
