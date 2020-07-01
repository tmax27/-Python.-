"""1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС."""
from memory_profiler import profile

length = 900


@profile
def recursion(length):
    def sum_series_numbers(n, elem=1):
        if n <= 0:
            return 0
        return elem + sum_series_numbers(n - 1, -elem / 2)

    print(
        f'Сумма последовательности из {length} элементов равна {sum_series_numbers(length)}')


@profile
def for_in(length):
    elem = 1
    amount = 0
    for i in range(length):
        amount += elem
        elem = -elem / 2
    print(f'Сумма последовательности из {length} элементов равна {amount}')


recursion(length)
for_in(length)

"""
Line #    Mem usage    Increment   Line Contents
================================================
    14     15.7 MiB     15.7 MiB   @profile
    15                             def recursion(length):
    16     17.0 MiB      0.1 MiB       def sum_series_numbers(n, elem=1):
    17     17.0 MiB      0.1 MiB           if n <= 0:
    18     17.0 MiB      0.0 MiB               return 0
    19     17.0 MiB      0.0 MiB           return elem + sum_series_numbers(n - 1, -elem / 2)
    20                             
    21     15.8 MiB      0.0 MiB       print(
    22     17.0 MiB      0.0 MiB           f'Сумма последовательности из {length} элементов равна {sum_series_numbers(length)}')

Рекурсия требует больше памяти , т.к. при ее работе хранится стек вызываемых функций.


Line #    Mem usage    Increment   Line Contents
================================================
    25     16.8 MiB     16.8 MiB   @profile
    26                             def for_in(length):
    27     16.8 MiB      0.0 MiB       elem = 1
    28     16.8 MiB      0.0 MiB       amount = 0
    29     16.8 MiB      0.0 MiB       for i in range(length):
    30     16.8 MiB      0.0 MiB           amount += elem
    31     16.8 MiB      0.0 MiB           elem = -elem / 2
    32     16.8 MiB      0.0 MiB       print(f'Сумма последовательности из {length} элементов равна {amount}')

Версия Python: 3.7
64-разрядная операционная система
"""