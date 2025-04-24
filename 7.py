import math
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
from tkinter import messagebox
from tkinter import font
from math import sin, cos, tan, fabs, exp, log, sqrt, asin, acos, atan, sinh, cosh, tanh, asinh, acosh, atanh


window = tk.Tk()
window.title('Приложение для построения графиков')
window.geometry('1475x575+20+20')


font_1 = font.Font(family= "Arial", size=15)


frame_1 = tk.Frame(window)
frame_1.place(x=65, y=25)


label_1 = tk.Label(frame_1, text='x0: ', font=font_1)
label_1.grid(row=0, column=0)
label_2 = tk.Label(frame_1, text='dx: ', font=font_1)
label_2.grid(row=1, column=0)
label_3 = tk.Label(frame_1, text='N: ', font=font_1)
label_3.grid(row=2, column=0)
label_4 = tk.Label(frame_1, text='Function: ', font=font_1)
label_4.grid(row=3, column=0)


value_1 = tk.StringVar()
value_1.set(-150)
entry_1 = tk.Entry(frame_1, textvariable = value_1, font=font_1)
entry_1.grid(row=0, column=1)


value_2 = tk.StringVar()
value_2.set(0.1)
entry_2 = tk.Entry(frame_1, textvariable = value_2, font=font_1)
entry_2.grid(row=1, column=1)


value_3 = tk.StringVar()
value_3.set(300)
entry_3 = tk.Entry(frame_1, textvariable = value_3, font=font_1)
entry_3.grid(row=2, column=1)


value_4 = tk.StringVar()
value_4.set('sin')
entry_4 = tk.Entry(frame_1, textvariable = value_4, font=font_1)
entry_4.grid(row=3, column=1)


frame_2 = tk.Frame(window)
frame_2.place(x=25, y=175)


frame_3 = tk.Frame(window)
frame_3.place(x=475, y=25)


text = tk.Text(frame_3, width=30)
text.grid(row=0, column=0)


fig, ax = plt.subplots()
ax.set_title('График')


frame_4 = tk.Frame(window)
frame_4.place(x=775, y=25)


canvas = FigureCanvasTkAgg(fig, master=frame_4)


def set_and_check_parameters():
    global x0, dx, N
    try:
        x0 = float(entry_1.get())
        dx = float(entry_2.get())
        N = int(entry_3.get())
        messagebox.showinfo("Информация", "Параметры успешно установлены!")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректные значения!")
    print('Кнопка "Задать и проверить параметры" нажата!')


def calculate_values():
    text.delete(1.0, tk.END)  # очищаем виджет Text перед добавлением новых значений
    text.insert(tk.END, "x\tf(x)\n")  # добавляем заголовок таблицы
    x0 = float(entry_1.get())
    dx = float(entry_2.get())
    N = int(entry_3.get())
    s = entry_4.get()  # получаем строку с математической функцией из виджета Entry

    def math_f(str):
        result = eval(str)
        return result

    for i in range(N):
        x = x0 + i * dx
        fx = (math_f(s)(x))
        text.insert(tk.END, f"{(x)}\t{(fx)}\n")  # добавляем значения x и f(x) в таблицу
    print('Кнопка "Рассчитать таблицу значений" нажата!')


def write_to_file():
    file = open("6.txt",'w')
    file.write("x\tf(x)\n")  # записываем заголовок таблицы
    s = entry_4.get()  # получаем строку с математической функцией из виджета Entry

    def math_f(str):
        result = eval(str)
        return result

    x0 = float(entry_1.get())
    dx = float(entry_2.get())
    N = int(entry_3.get())

    for i in range(N):
        x = x0 + i * dx
        fx = (math_f(s)(x))
        file.write(f"{x}\t{fx}\n")  # записываем значения x и f(x) в файл
    print('Кнопка "Записать таблицу значений в файл" нажата!')


def read_from_file():
    file = open("6.txt",'r')
    table = file.read()  # читаем таблицу из файла
    text.delete(1.0, tk.END)  # очищаем виджет Text
    text.insert(tk.END, table)  # вставляем таблицу в виджет Text
    print('Кнопка "Считать таблицу значений из файла" нажата!')


def draw_graph():
    global ax, canvas
    s = entry_4.get()

    def math_f(str):
        result = eval(str)
        return result

    x0 = float(entry_1.get())
    dx = float(entry_2.get())
    N = int(entry_3.get())

    X=[]
    Y=[]

    for i in range(N):
        x = x0 + i * dx
        X.append(x)
        fx = (math_f(s)(x))
        Y.append(fx)

    ax.plot(X, Y)
    canvas.draw()
    canvas.get_tk_widget().pack()

    print('Кнопка "Нарисовать график" нажата!')


def clear_graph():
    global ax, canvas
    ax.clear()
    canvas.draw()
    print('Кнопка "Очистить график" нажата!')


def close_app():
    global canvas, fig, window
    if canvas:
        canvas.get_tk_widget().destroy()
    plt.close(fig)
    window.destroy()
    print('Кнопка "Закрыть приложение" нажата!')


button_1 = tk.Button(frame_2, text= 'Задать и проверить параметры',width=35, command=set_and_check_parameters, font=font_1)
button_1.grid(row=0)
button_2 = tk.Button(frame_2, text= 'Рассчитать таблицу значений', width=35, command=calculate_values, font=font_1)
button_2.grid(row=1)
button_3 = tk.Button(frame_2, text= 'Записать таблицу значений в файл', width=35, command=write_to_file, font=font_1)
button_3.grid(row=2)
button_4 = tk.Button(frame_2, text= 'Считать таблицу значений из файла', width=35, command=read_from_file, font=font_1)
button_4.grid(row=3)
button_5 = tk.Button(frame_2, text= 'Нарисовать график', width=35, command=draw_graph, font=font_1)
button_5.grid(row=4)
button_6 = tk.Button(frame_2, text= 'Очистить график', width=35, command=clear_graph, font=font_1)
button_6.grid(row=5)
button_7 = tk.Button(frame_2, text= 'Закрыть приложение', width=35, command=close_app, font=font_1)
button_7.grid(row=6)


window.mainloop()