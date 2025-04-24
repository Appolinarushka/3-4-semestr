import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.linalg as sla

# генерация данных для спектра с несколькими пиками
x = np.linspace(1000, 1200, 175)
y = np.zeros_like(x)

# добавление пиков
peaks = [(1050, 100), (1100, 60), (1150, 40)]
for i in peaks:
    y += i[1] * np.exp(-0.5 * ((x - i[0]) / 1) ** 2)
# регистрируемый сигнал

print('y')
print(y)

# построение графика изначального спектра
plt.figure()
plt.plot(x, y)
plt.title('Регистрируемый сигнал')
plt.grid(True)
plt.show()

# m = int(input("Введите значение m: "))
m = 3

# создание матрицы A
A = np.zeros((175, 175))

for i in range(175):
    for j in range(175):
        if abs(i - j) <= m:
            A[i, j] = 1 / (2 * m + 1)
        if abs(i - j) > m:
            A[i, j] = 0

print('A')
print(A)
# print('A_float')
# A_float = A.astype(float)
# print(A_float)

res_A = np.linalg.det(A)
print('res_A', res_A)

product = np.dot(A, y)
print('product')
print(product)

max_element = max(product)
print('Максимальный элемент', max_element)

# def max_index(product):
#    max_value = product[0]
#    max_index = 0
#    for i in range(len(product)):
#        if product[i] > max_value:
#            max_value = product[i]
#            max_index = i
#    return max_index
# max_index_value = max_index(product)
# print("Индекс максимального элемента:", max_index_value)

max_noise = 0.025 * max_element
print('Максимальный шум', max_noise)

noise_distribution = [random.uniform(-max_noise, max_noise) for _ in range(175)]
print('Распределение шума')
print(noise_distribution)
average_noise_value = sum(noise_distribution) / len(noise_distribution)
print('average_noise_value', average_noise_value)

result = product + noise_distribution
print('result')
print(result)

# построение графика результата регистрации
plt.figure()
plt.plot(x, result)
plt.title('Результат регистрации')
plt.grid(True)
plt.show()

U = np.eye(175)  # единичная матрица 175 на 175
# print('U')
# print(U)
# print('U_float')
# U_float = U.astype(float)
# print(U_float)

A_T = A.T  # матрица, транспонированная к матрице A
print('Матрица, транспонированная к матрице A')
print(A_T)

res_A_T = np.linalg.det(A_T)
print('res_A_T', res_A_T)

# определение линейного преобразования R
w = 0.0001
R = np.dot(np.linalg.inv(np.dot(A_T, A) + w * U), A_T)
print('R')
print(R)

R_result = np.dot(R, result)
print('R_result')
print(R_result)

# построение графика результата интерпретации
plt.figure()
plt.plot(x, R_result)
plt.title('Результат интерпретации')
plt.grid(True)
plt.show()

#pogr = R_result - y  # погрешность интерпретации
#print('pogr')
#print(pogr)
#print('max_pogr', max(pogr))

B = np.linalg.pinv(A)
print('B')
print(B)

R_иск= np.dot(U, B)
print('R_иск')
print(R_иск)

R_иск_result = np.dot(R_иск, result )
print('R_иск_result')
print(R_иск_result)

# синтез идеального сигнала
plt.figure()
plt.plot(x, R_иск_result)
plt.title('Сигнал идеального прибора')
plt.grid(True)
plt.show()

#Q = np.linalg.inv(np.dot(A_T, A))
#Sigma = np.dot(np.linalg.inv(np.dot(A_T, A)), np.dot(U,A_T))
#print('Sigma')
#print(Sigma)


#RR = np.dot(np.linalg.inv(np.dot(A_T, A) + w * Sigma), A_T)
#RR_result = np.dot(RR, result)
#plt.figure()
#plt.plot(x, RR_result)
#plt.title('Работает?')
#plt.grid(True)
#plt.show()