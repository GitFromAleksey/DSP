import numpy as np
import matplotlib.pyplot as plt
import SignalGenerate as sg


print('Глава 1.5.2 - Пример нелинейной системы')

f0_1Hz = 1 # частота сигнала, Гц
f0_3Hz = 3 # частота сигнала, Гц
A = 1 # амплитуда сигнала в о.е.
ts = 0.02 # время дискретизации, сек
time = 1 # время генерации, сек
ShiftZero = 0 # сдвиг относительно оси "х" о.е. амплитуды
ShiftPhaseDegree = 0 # сдвиг фазы в градусах

_t_1Hz, _x_n_1Hz = sg.getSinus(f0_1Hz, A, ts, time, ShiftZero, ShiftPhaseDegree)
_y_n_1Hz_pow_2 = np.power(_x_n_1Hz, 2)
n = np.arange(0, time/ts, 1)
_y_n_1Hz_formula = 1/2 - np.cos(2*np.pi*2*f0_1Hz*n*ts)/2

_t_3Hz, _x_n_3Hz = sg.getSinus(f0_3Hz, A, ts, time, ShiftZero, ShiftPhaseDegree)
_y_n_3Hz_pow_2 = np.power(_x_n_3Hz, 2)
n = np.arange(0, time/ts, 1)
_y_n_3Hz_formula = 1/2 - np.cos(2*np.pi*2*f0_3Hz*n*ts)/2

_x_n_summ = _x_n_1Hz + _x_n_3Hz
_y_n_summ = np.power(_x_n_summ, 2)


fig1 = plt.figure()

rows = 3
cols = 1

ax1 = fig1.add_subplot(rows, cols, 1)
ax1.set_title('Синусоидальный сигнал и его квадрат 1Гц')
ax1.set_xlabel('t, s')
ax1.set_ylabel('x(n), y(n)=-x(n)/2')
ax1.grid(which="major", linewidth=1.2)
ax1.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)
ax1.plot(_t_1Hz, _x_n_1Hz)
ax1.plot(_t_1Hz, _y_n_1Hz_formula)
ax1.scatter(_t_1Hz, _y_n_1Hz_pow_2)

ax2 = fig1.add_subplot(rows, cols, 2)
ax2.set_title('Синусоидальный сигнал и его квадрат 3Гц')
ax2.set_xlabel('t, s')
ax2.set_ylabel('x(n), y(n)=-x(n)/2')
ax2.grid(which="major", linewidth=1.2)
ax2.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)
ax2.plot(_t_3Hz, _x_n_3Hz)
ax2.plot(_t_3Hz, _y_n_3Hz_formula)
ax2.scatter(_t_3Hz, _y_n_3Hz_pow_2)

ax3 = fig1.add_subplot(rows, cols, 3)
ax3.set_title('Сумма сигналов и квадратов сигналов (1Гц и 3Гц) ')
ax3.set_xlabel('t, s')
ax3.set_ylabel('x(n), y(n)=-x(n)/2')
ax3.grid(which="major", linewidth=1.2)
ax3.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)
ax3.plot(_t_1Hz, _x_n_summ)
ax3.plot(_t_1Hz, _y_n_summ)

plt.show()
