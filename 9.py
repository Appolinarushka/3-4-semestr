import sys
import math
import tkinter as tk
import numpy as np
import matplotlib.pyplot
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
from tkinter import filedialog
from tkinter import font


matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


class pendulum:
    def __init__(self, damping, amplitude, frequency):
        self.d = damping
        self.a = amplitude
        self.omega = frequency

    def __call__(self, y, t):
        velocity = y[1]  # первое дифференциальное уравнение
        acceleration = -self.d * y[1] - np.sin(y[0]) + self.a * np.cos(self.omega * t)  # второе дифференциальное уравнение
        return np.array([velocity, acceleration])


class rk:
    def __init__(self, f):
        self.f = f

    def setfunc(self, f):
        self.f = f

    def setparams(self, u0, t0, tmax, h):
        self.u0 = u0
        self.t0 = t0
        self.tmax = tmax
        self.h = h

    def rk4(self, u, t):
        k1 = self.f(u, t)
        k2 = self.f(u + self.h * k1 / 2, t + self.h / 2)
        k3 = self.f(u + self.h * k2 / 2, t + self.h / 2)
        k4 = self.f(u + self.h * k3, t + self.h)
        return u + (k1 + 2 * (k2 + k3) + k4) * self.h / 6

    def solve(self):
        y = self.u0
        solution = np.empty((0, 2))
        time = np.arange(self.t0, self.tmax, self.h)
        for t in time:
            y = self.rk4(y, t)
            solution = np.append(solution, [y], axis=0)
        return solution, time


def input_int(x):
    while True:
        try:
            x = int(x.get())
            return 0
        except ValueError:
            return 1


def input_float(x):
    while True:
        try:
            x = float(x.get())
            return 0
        except ValueError:
            return 1


class Graphing:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Маятник')
        self.window.geometry('1500x750+20+20')

        font_1 = font.Font(family="Arial", size=15)

        frame1 = tk.Frame()
        frame2 = tk.Frame()
        frame3 = tk.Frame()
        frame4 = tk.Frame()
        frame5 = tk.Frame()

        self.x0 = tk.StringVar()
        self.dx = tk.StringVar()
        self.xmax = tk.StringVar()
        self.d = tk.StringVar()
        self.a = tk.StringVar()
        self.omega = tk.StringVar()
        self.coord0 = tk.StringVar()
        self.speed0 = tk.StringVar()
        self.xaxis = tk.IntVar()
        self.yaxis = tk.IntVar()

        def create_label_entry(text, frame, row, variable, default):
            tk.Label(frame, text=text, font=font_1).grid(row=row, column=0)
            entry = tk.Entry(frame, width=10, textvariable=variable,font=font_1)
            entry.insert(0, default)
            entry.grid(row=row, column=1)

        create_label_entry('x0: ', frame1, 0, self.x0, '0')
        create_label_entry('dx: ', frame1, 1, self.dx, '0.1')
        create_label_entry('x_max: ', frame1, 2, self.xmax, '100')
        create_label_entry('Damping: ', frame1, 3, self.d, '0.05')
        create_label_entry('Amplitude: ', frame1, 4, self.a, '0.01')
        create_label_entry('Frequency: ', frame1, 5, self.omega, '1')
        create_label_entry('Coordinate: ', frame1, 6, self.coord0, '3')
        create_label_entry('Velocity: ', frame1, 7, self.speed0, '0')

        ttk.Label(frame5, text='X axis: ', font=font_1).grid(row=0, column=0)
        ttk.Radiobutton(frame5, text='t', variable=self.xaxis, value=0).grid(row=0, column=1) # option button
        ttk.Radiobutton(frame5, text='x', variable=self.xaxis, value=1).grid(row=0, column=2)
        ttk.Radiobutton(frame5, text='v', variable=self.xaxis, value=2).grid(row=0, column=3)
        ttk.Label(frame5, text='Y axis: ', font=font_1).grid(row=1, column=0)
        ttk.Radiobutton(frame5, text='t', variable=self.yaxis, value=0).grid(row=1, column=1)
        ttk.Radiobutton(frame5, text='x', variable=self.yaxis, value=1).grid(row=1, column=2)
        ttk.Radiobutton(frame5, text='v', variable=self.yaxis, value=2).grid(row=1, column=3)

        tk.Button(frame2, text='Задать параметры', command=self.set_options, font=font_1).pack(anchor=tk.W, fill=tk.BOTH)
        tk.Button(frame2, text='Рассчитать таблицу значений', command=self.calculate_values, font=font_1).pack(anchor=tk.W, fill=tk.BOTH)
        tk.Button(frame2, text='Записать таблицу значений в файл', command=self.write_to_file, font=font_1).pack(anchor=tk.W, fill=tk.BOTH)
        tk.Button(frame2, text='Считать таблицу значений из файла', command=self.read_file, font=font_1).pack(anchor=tk.W, fill=tk.BOTH)
        tk.Button(frame2, text='Нарисовать график', command=self.draw_graph, font=font_1).pack(anchor=tk.W, fill=tk.BOTH)
        tk.Button(frame2, text='Очистить график', command=self.clear_graph, font=font_1).pack(anchor=tk.W, fill=tk.BOTH)
        tk.Button(frame2, text='Закрыть приложение', command=self.close_app, font=font_1).pack(anchor=tk.W, fill=tk.BOTH)

        self.fig, self.ax = matplotlib.pyplot.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=frame4)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

        self.text = tk.Text(frame3, width=30)
        self.text.pack()

        frame1.place(x=110, y=25)
        frame2.place(x=50, y=325)
        frame3.place(x=475, y=25)
        frame4.place(x=800, y=25)
        frame5.place(x=1050, y=550)

        self.window.mainloop()

    def set_options(self):
        if (input_float(self.x0) + input_float(self.dx) + input_float(self.xmax) + input_float(self.d) + + input_float(
                self.a) + input_float(self.omega) + input_float(self.coord0) + input_float(self.speed0)) == 0:
            self.x0v = float(self.x0.get())
            self.dxv = float(self.dx.get())
            self.xmaxv = float(self.xmax.get())
            self.coord0v = float(self.coord0.get())
            self.speed0v = float(self.speed0.get())
            self.initial = np.array([self.coord0v, self.speed0v])
            self.f = pendulum(damping=float(self.d.get()), amplitude=float(self.a.get()),
                                frequency=float(self.omega.get()))
            self.solver = rk(self.f)
            self.solver.setparams(self.initial, self.x0v, self.xmaxv, self.dxv)
        else:
            showerror('Error', 'Wrong format')

    def calculate_values(self):
        self.text.delete('1.0', 'end')
        self.y, self.t = self.solver.solve()
        for i in reversed(range(self.t.size)):
            self.text.insert('1.0', ("{:.2f}".format(self.y[i][0]) + ' ' + "{:.2f}".format(self.y[i][1]) + ' ' + "{:.2f}".format(self.t[i]) + '\n'))

    def read_file(self):
        filepath = filedialog.askopenfilename()
        self.text.delete('1.0', 'end')
        arr1 = []
        arr2 = []
        with open(filepath, 'r') as file:
            i = 0
            for line in file:
                values = line.strip().split()
                arr1.append([float(values[0]), float(values[1])])
                arr2.append([float(values[2])])
                self.text.insert('1.0', ("{:.2f}".format(float(values[0])) + ' ' + "{:.2f}".format(
                    float(values[1])) + ' ' + "{:.2f}".format(float(values[2])) + '\n'))
                i += 1
        self.y = np.array(arr1)
        self.t = np.array(arr2)

    def write_to_file(self):
        filepath = filedialog.asksaveasfilename()
        with open(filepath, 'w') as file:
            for i in range(self.t.size):
                file.write("{:.2f}".format(self.y[i][0]) + ' ' + "{:.2f}".format(self.y[i][1]) + ' ' + "{:.2f}".format(self.t[i]) + '\n')

    def draw_graph(self):
        g = (self.t, self.y[:, 0], self.y[:, 1])
        self.ax.plot(g[self.xaxis.get()], g[self.yaxis.get()])
        self.canvas.draw()

    def clear_graph(self):
        self.ax.clear()
        self.canvas.draw()

    def close_app(self):
        self.canvas.get_tk_widget().destroy()
        matplotlib.pyplot.close(self.fig)
        self.window.destroy()


graph = Graphing()
# x v t