import math


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


class matrix:

    def set(self, m, n):
        self.m = m
        self.n = n
        self.a = [[(i + 1) * (j + 1) for j in range(n)] for i in range(m)]

    def out(self):
        s = [[str(e) for e in row] for row in self.a]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print('\n'.join(table))

    def outfile(self, file):
        s = [[str(e) for e in row] for row in self.a]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        file.write('\n'.join(table))

    #    def alternative_out(self, file=None):
    #        if file is None:
    #            for record in self.a:
    #                print(record)
    #        else:
    #            for record in self.a:
    #                file.write(str(record) + '\n')

    def convert(self, function):
        self.b = [[function((i + 1) * (j + 1)) for j in range(len(self.a[i]))] for i in range(len(self.a))]
        s = [[str(e) for e in row] for row in self.b]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print('\n'.join(table))


u = matrix()
u.set(m, n)
u.out()
f = open('matrix.txt', 'w')
u.outfile(f)
# u.alternative_out()
print('')
u.convert(math.sqrt)