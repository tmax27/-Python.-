"""Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого)."""
numb_a = int(input('Введите число a: '))
numb_b = int(input('Введите число b: '))
numb_c = int(input('Введите число c: '))
if numb_b < numb_a < numb_c or numb_c < numb_a < numb_b:
    print(f'Средним числом является {numb_a}')
elif numb_a < numb_b < numb_c or numb_c < numb_b < numb_a:
    print(f'Средним числом является {numb_b}')
else:
    print(f'Средним числом является {numb_c}')