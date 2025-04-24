import random


def int_input():
    while True:
        try:
            number = int(input('Введите целое число : '))
            return number
        except ValueError:
            print('Вы ошиблись! Попробуйте ещё раз!')


m = int_input()
print('Число строк :', m)

print('')

n = int_input()
print('Число столбцов :', n)

print('')


def float_input():
    while True:
        try:
            number = float(input('Введите вещественное число : '))
            return number
        except ValueError:
            print('Вы ошиблись! Попробуйте ещё раз!')


d = float_input()
print(d)

print('')


def new_list(a, m, n):
    for i in range(m):
        for j in range(n):
            a[i][j] = i * j
    return a


a = [0] * m
for i in range(m):
    a[i] = [0] * n
w = new_list(a, m, n)
for record in w:
    print(record)
print('')
i = random.randint(0, m - 1)
j = random.randint(0, n - 1)
element = w[i][j]
print(element, ': i =', i, ', j =', j)
print('')
w[i][j] = d
for record in w:
    print(record)