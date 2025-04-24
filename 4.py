import math
import sys
import matplotlib.pyplot as plt


def float_input():
    while True:
        try:
            number = float(input('Введите вещественное число : '))
            return number
        except ValueError:
            print('Вы ошиблись! Попробуйте ещё раз!')


x0 = float_input()
print('x0 =', x0)

print('')

dx = float_input()
print('dx =', dx)

print('')


def int_input():
    while True:
        try:
            number = int(input('Введите целое число : '))
            return number
        except ValueError:
            print('Вы ошиблись! Попробуйте ещё раз!')


N = int_input()
print('N =', N)

print('')


class matrix2:

    def __init__(self, x0, dx, N):
        self.x0 = x0
        self.dx = dx
        self.N = N
        self.x = [0] * N
        self.y = [0] * N

    def setx(self):
        self.x = [self.x0 + i * self.dx for i in range(self.N)]

    def sety(self, function):
        self.y = [function(self.x0 + i * self.dx) for i in range(self.N)]

    def out(self):
        for i in range(self.N):
            print(f"{self.x[i]} {self.y[i]}")

    def outfile(self, file=sys.stdout):
        for i in range(self.N):
            file.write(f"{self.x[i]} {self.y[i]}\n")  # f-строки
            # выражения в фигурных скобках заменяются их значениями

    def grafik(self, ax, **kwargs):
        ax.plot(self.x, self.y, **kwargs)
        return ax


a = matrix2(x0, dx, N)
b = matrix2(x0, dx, N)
c = matrix2(x0, dx, N)

a.setx()
b.setx()
c.setx()

a.sety(math.sin)
b.sety(math.cos)
c.sety(math.fabs)

fig1, ax1 = plt.subplots(figsize=(7.2, 3.6))

plt.suptitle('Графики №1')

a.grafik(ax1, label='sin', color='red', linestyle=':')
b.grafik(ax1, label='cos', color='black', linestyle='--')
c.grafik(ax1, label='fabs', color='orange', linestyle='-')

ax1.legend()
plt.show()

fig2, ax2 = plt.subplots(1, 3, figsize=(7.2, 3.6))

plt.suptitle('Графики №2')

ax2[0].set_title('first')
ax2[1].set_title('second')
ax2[2].set_title('third')

a.grafik(ax2[0], label='sin', color='red', linestyle=':')
b.grafik(ax2[1], label='cos', color='black', linestyle='--')
c.grafik(ax2[2], label='fabs', color='orange', linestyle='-')

ax2[0].legend()
ax2[1].legend()
ax2[2].legend()

plt.show()

print('Points of the first graph: ')
a.out()
print('')

print('Points of the second graph: ')
b.out()
print('')

print('Points of the third graph: ')
c.out()

f = open('matrix2_a.txt', 'w')
a.outfile(f)
f = open('matrix2_b.txt', 'w')
b.outfile(f)
f = open('matrix2_c.txt', 'w')
c.outfile(f)

# "красивый" график:
# x0 = -10
# dx = 0.05
# N = 400