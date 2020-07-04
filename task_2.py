"""2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы."""
import random


def merge_sort(lst):

    if len(lst) > 1:
        mid = len(lst) // 2
        lefthalf = lst[:mid]
        righthalf = lst[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                lst[k] = lefthalf[i]
                i = i + 1
            else:
                lst[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            lst[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            lst[k] = righthalf[j]
            j = j + 1
            k = k + 1


n = int(input("Введите число элементов: "))
lst = [random.random()*50 for i in range(n)]

print(f"Исходный - {lst}")
merge_sort(lst)
print(f"Отсортированный - {lst}")
