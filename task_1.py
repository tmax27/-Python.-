"""Задание_1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9."""


# for i in range(2, 100):
#     d = 0
#     for j in range(2, 10):
#         if i % j == 0:
#             d += 1
#             i += 1
#     print(f'В диапазоне 2-99: {d} чисел кратны {j}')

def task_1():
    lst_1 = list(range(2, 100))
    lst_2 = list(range(2, 10))
    for i in lst_2:
        numb = 0
        for j in lst_1:
            if j % i == 0:
                numb += 1
        print(f'В диапазоне 2-99: {numb} чисел кратны {i}.')


task_1()
