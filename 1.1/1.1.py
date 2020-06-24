import numpy as np
import matplotlib.pyplot as plt

# x(t) = sin(2*pi*f0*t) - непрерывный сигнал
# x(n_array) = sin(2*pi*f0*n_array*ts) - дискретная последовательность

print('Глава 1.1')

# пример массива с разбиением диапазона
##ls_from = 0
##ls_to = 9
##ls_count = 10
##linspace = np.linspace(ls_from, ls_to, ls_count) # 10 чисел от 0 до 9
##print(linspace)
##print(type(linspace))

# пример массива с шагом
##arg_from = 0
##arg_to = 10
##arg_step = 1
##arange = np.arange(arg_from, arg_to, arg_step)
##print(arange)
##print(type(arange))

A = 1 # амплитуда сигнала
f0 = 1 # частота сигнала, Гц
T = 1/f0 # период, сек
n = 100 # количество отсчётов на период
n_T = 20 # кол-во периодов
n_array = np.arange(0, n * n_T, 1) # отсчёты(массив)
ts = T/n # промежуток времени кантования, сек/отсчёт

print('A = ', A, ', амплитуда сигнала')
print('f0 = ', f0, ',Гц - частота сигнала')
print('T = ', T, ',сек - период сигнала')
print('n = ', n, ', кол-во отсчётов')
print('ts = ', ts, ',сек время квантирования')

y = 2 * np.pi * f0 * n_array * ts
x = A * np.sin(y)

##print('n_array = ', n_array)
##print('x(n_array)', x)

plt.title('Title')
plt.xlabel('n_array')
plt.ylabel('x(n_array)')
plt.grid(True)
plt.plot(y, x)
plt.scatter(y, x)
plt.show()
