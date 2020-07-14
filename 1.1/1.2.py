import numpy as np
import matplotlib.pyplot as plt
import SignalGenerate as sg

print('Глава 1.2 - Мгновенные значения, амплитуда и мощность сигнала')


f0 = 1 # частота сигнала, Гц
A = 1 # амплитуда сигнала в о.е.
ts = 0.001 # время дискретизации, сек
time = 1 # время генерации, сек
ShiftZero = 0 # сдвиг относительно оси "х" о.е. амплитуды
ShiftPhaseDegree = 0 # сдвиг фазы в градусах

_t, _x_t = sg.getSinus(f0, A, ts, time, ShiftZero, ShiftPhaseDegree)

_x_t_module = np.absolute(_x_t)
_x_t_power = np.power(_x_t, 2)

fig1 = plt.figure()

rows = 3
cols = 1

ax1 = fig1.add_subplot(rows, cols, 1)
ax1.set_title('Рис. 1.4 - синусоидальный сигнал во временной области')
ax1.set_xlabel('t, s')
ax1.set_ylabel('x(t)')
ax1.grid(which="major", linewidth=1.2)
ax1.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)
ax1.plot(_t, _x_t)

ax2 = fig1.add_subplot(rows, cols, 2)
ax2.set_title('модуль сигнала')
ax2.set_xlabel('t, s')
ax2.set_ylabel('x(t)')
ax2.grid(which="major", linewidth=1.2)
ax2.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)
ax2.plot(_t, _x_t_module)

ax3 = fig1.add_subplot(rows, cols, 3)
ax3.set_title('мощность сигнала')
ax3.set_xlabel('t, s')
ax3.set_ylabel('x(t)')
ax3.grid(which="major", linewidth=1.2)
ax3.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)
ax3.plot(_t, _x_t_power)

plt.show()
