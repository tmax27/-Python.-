"""1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций"""
import random
import timeit


def bubble_sort(orig_list):
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
        n += 1
    return orig_list


def bubble_sort_upd(orig_list):
    n = 1
    k = 0
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
                k = 1
        if k == 0:
            break
        n +=1
    return orig_list


orig_list = [random.randint(-100, 100) for i in range(10)]
print(orig_list) # Исходный список
# Последующие 2 сортированные, но обновлённый работает быстрее
print(bubble_sort(orig_list))
print(bubble_sort_upd(orig_list))

print(timeit.timeit("bubble_sort(orig_list)", setup="from __main__ import bubble_sort, orig_list"))
print(timeit.timeit("bubble_sort_upd(orig_list)", setup="from __main__ import bubble_sort_upd, orig_list"))

'''
[-41, 40, 59, -65, 69, 100, 15, -95, 24, -79]   print(orig_list)
[100, 69, 59, 40, 24, 15, -41, -65, -79, -95]   print(bubble_sort(orig_list))
[100, 69, 59, 40, 24, 15, -41, -65, -79, -95]   print(bubble_sort_upd(orig_list))
6.346599    timeit.timeit("bubble_sort(orig_list)"
1.0681281   timeit.timeit("bubble_sort_upd(orig_list)"
'''