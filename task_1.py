"""1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего."""

import collections


def calc():
    n = int(input("Введите количество предприятий для расчета прибыли: "))
    d = dict()
    a = 1

    for i in range(n):
        name = input("Введите название предприятия: ")
        pr = input(
            "через пробел введите прибыль данного предприятия\n"
            "за каждый квартал(Всего 4 квартала): ")
        profit = pr.split(" ")
        d[name] = profit
        a += 1
        print()

    fab = collections.Counter(d)

    b = 0
    t = 0
    for i in fab:
        summ = 0
        for j in fab[i]:
            summ += int(j)
        fab[i] = summ
        t += summ
        b += 1
    sec = t / b

    print("Средняя годовая прибыль всех предприятий: " + str(sec))
    bigger = []
    smaller = []
    for i in fab:
        if int(fab[i]) >= sec:
            bigger.append(i)
        else:
            smaller.append(i)

    print("Предприятия, с прибылью выше среднего значения: ", end="")
    for i in bigger:
        print(i, end=" ")
    print()
    print()
    print("Предприятия, с прибылью ниже среднего значения: ", end="")
    for i in smaller:
        print(i, end=" ")
    print()


calc()