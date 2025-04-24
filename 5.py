import tkinter as tk


window = tk.Tk()
window.title('Построение графиков')
window.geometry('400x550+20+20')


def create_label_entry(parent, row, label_text):
    label = tk.Label(parent, text=label_text)
    entry = tk.Entry(parent)
    label.grid(row=row, column=0)
    entry.grid(row=row, column=1)


frame_1 = tk.Frame(window)
frame_1.pack(pady=20)


label_entry_1 = create_label_entry(frame_1, 0, 'x0: ')
label_entry_2 = create_label_entry(frame_1, 1, 'dx: ')
label_entry_3 = create_label_entry(frame_1, 2, 'N: ')
label_entry_4 = create_label_entry(frame_1, 3, 'Function: ')


def create_button(parent, row, button_text):
    button = tk.Button(parent, text=button_text, width=35)
    button.grid(row=row)
    return button


frame_2 = tk.Frame(window)
frame_2.pack()


button_1 = create_button(frame_2, 0, 'Задать и проверить параметры')
button_2 = create_button(frame_2, 1, 'Рассчитать таблицу значений')
button_3 = create_button(frame_2, 2, 'Записать таблицу значений в файл')
button_4 = create_button(frame_2, 3, 'Считать таблицу значений из файла')
button_5 = create_button(frame_2, 4, 'Нарисовать график')
button_6 = create_button(frame_2, 6, 'Очистить график')
button_7 = create_button(frame_2, 7, 'Закрыть приложение')


canvas = tk.Canvas(window, width=200, height=200)
canvas.pack(pady=20)
python_image = tk.PhotoImage(file="sign.png")
canvas.create_image(100, 100, image=python_image)


window.mainloop()