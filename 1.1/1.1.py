import numpy as np
import matplotlib.pyplot as plt
import SignalGenerate as sg

# _y(t) = sin(2*pi*f0*t) - непрерывный сигнал
# _y(n_array) = sin(2*pi*f0*n_array*ts) - дискретная последовательность

print('Глава 1.1')



f0 = 2 # частота сигнала, Гц
A = 1 # амплитуда сигнала в о.е.
n = 15 # количество отсчётов на период
n_T = 1 # кол-во периодов
ShiftZero = 0 # сдвиг относительно оси "х" о.е. амплитуды
ShiftPhaseDegree = 180 # сдвиг фазы в градусах

_x, _y = sg.getSinus(f0, A, n, n_T, ShiftZero, ShiftPhaseDegree)

_x1, _y1 = sg.getSinus(f0*2, A, n, n_T, ShiftZero, ShiftPhaseDegree)

plt.title('Title')
plt.xlabel('n_array')
plt.ylabel('_y(n_array)')
plt.grid(True)
plt.plot(_x, _y)
plt.plot(_x1, _y1)
plt.scatter(_x, _y)
plt.show()
