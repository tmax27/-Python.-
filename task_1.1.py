"""1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС."""
import sys
from memory_profiler import profile


@profile
def func():

    a = list(range(500000))

    min_num = a[0]
    min_num2 = a[1]

    if min_num > min_num2:
        min_num, min_num2 = min_num2, min_num

    for i in range(len(a)):
        if a[i] < min_num:
            min_num2 = min_num
            min_num = a[i]
        elif a[i] < min_num2:
            min_num2 = a[i]

    print("Два наименьших элемента:", min_num, min_num2)
    print(f"Два наименьших элемента: {min_num}, {min_num2}")
    del a


func()

"""
Для запуска программы было выделено 15.7 MiB.
При создании списка "a" было выделено еще 19.3 MiB.
После выполнения программы удалил список "a" , тем самым
освободил память (19.3 MiB).
Line #    Mem usage    Increment   Line Contents
================================================
    13     15.7 MiB     15.7 MiB   @profile
    14                             def func():
    15                             
    16     35.0 MiB     19.3 MiB       a = list(range(500000))
    17                             
    18     35.0 MiB      0.0 MiB       min_num = a[0]
    19     35.0 MiB      0.0 MiB       min_num2 = a[1]
    20                             
    21     35.0 MiB      0.0 MiB       if min_num > min_num2:
    22                                     min_num, min_num2 = min_num2, min_num
    23                             
    24     35.0 MiB      0.0 MiB       for i in range(len(a)):
    25     35.0 MiB      0.0 MiB           if a[i] < min_num:
    26                                         min_num2 = min_num
    27                                         min_num = a[i]
    28     35.0 MiB      0.0 MiB           elif a[i] < min_num2:
    29     35.0 MiB      0.0 MiB               min_num2 = a[i]
    30                             
    31     35.0 MiB      0.0 MiB       print("Два наименьших элемента:", min_num, min_num2)
    32     35.0 MiB      0.0 MiB       print(f"Два наименьших элемента: {min_num}, {min_num2}")
    33     15.7 MiB      0.0 MiB       del a
    
Версия Python: 3.7
64-разрядная операционная система
"""