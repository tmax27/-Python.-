"""Задание_8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки
и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу."""


def task_8():
    row_n = 5
    col_n = 4
    matrix = []
    for i in range(row_n):
        string = []
        s = 0
        print(f'{i + 1}-я строка: ')
        for j in range(col_n):
            n = int(input())
            s += n
            string.append(s)
            matrix.append(string)

    for i in matrix:
        print(i)


task_8()
