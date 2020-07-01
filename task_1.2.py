"""1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС."""
from memory_profiler import profile


@profile
def simple(i):
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


@profile
def eratosfen(i):
    n = 2
    l = 10000
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n*2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
    return [p for p in sieve if p != 0][i-1]


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(eratosfen(i))

"""
Line #    Mem usage    Increment   Line Contents
================================================
    12     15.7 MiB     15.7 MiB   @profile
    13                             def simple(i):
    14     15.7 MiB      0.0 MiB       count = 1
    15     15.7 MiB      0.0 MiB       n = 2
    16     15.7 MiB      0.0 MiB       while count <= i:
    17     15.7 MiB      0.0 MiB           t = 1
    18     15.7 MiB      0.0 MiB           is_simple = True
    19     15.7 MiB      0.0 MiB           while t <= n:
    20     15.7 MiB      0.0 MiB               if n % t == 0 and t != 1 and t != n:
    21     15.7 MiB      0.0 MiB                   is_simple = False
    22     15.7 MiB      0.0 MiB                   break
    23     15.7 MiB      0.0 MiB               t += 1
    24     15.7 MiB      0.0 MiB           if is_simple:
    25     15.7 MiB      0.0 MiB               if count == i:
    26     15.7 MiB      0.0 MiB                   break
    27     15.7 MiB      0.0 MiB               count += 1
    28     15.7 MiB      0.0 MiB           n += 1
    29     15.7 MiB      0.0 MiB       return n
    
Line #    Mem usage    Increment   Line Contents
================================================
    32     15.7 MiB     15.7 MiB   @profile
    33                             def eratosfen(i):
    34     15.7 MiB      0.0 MiB       n = 2
    35     15.7 MiB      0.0 MiB       l = 10000
    36     16.1 MiB      0.1 MiB       sieve = [x for x in range(l)]
    37     16.1 MiB      0.0 MiB       sieve[1] = 0
    38     16.1 MiB      0.0 MiB       while n < l:
    39     16.1 MiB      0.0 MiB           if sieve[n] != 0:
    40     16.1 MiB      0.0 MiB               m = n*2
    41     16.1 MiB      0.0 MiB               while m < l:
    42     16.1 MiB      0.0 MiB                   sieve[m] = 0
    43     16.1 MiB      0.0 MiB                   m += n
    44     16.1 MiB      0.0 MiB           n += 1
    45     16.1 MiB      0.0 MiB       return [p for p in sieve if p != 0][i-1]

Незначительный инкремент обусловлен необходимостью генерации списка
Величина инкремента может изменяться, в зависимости от объема списка
При этом в целом инкремент находится в рамках нормы
Оптимизация не требуется

Версия Python: 3.7
64-разрядная операционная система
"""