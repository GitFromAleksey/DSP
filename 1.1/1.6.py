import numpy as np
import matplotlib.pyplot as plt
import SignalGenerate as sg


print('Глава 1.6 - Инвариантные во времени системы')
text = '\n\tИнвариантная во времени система - это система, для которой задержка во времени(или сдвиг) во времени входной последовательности вызывает эквивалентную временную задержку выходной последовательности.\n'
print(text)

f0 = 1 # частота сигнала, Гц
A = 1 # амплитуда сигнала в о.е.
ts = 0.001 # время дискретизации, сек
time = 1 # время генерации, сек
ShiftZero = 0 # сдвиг относительно оси "х" о.е. амплитуды
ShiftPhaseDegree = 0 # сдвиг фазы в градусах

_t, _x_t = sg.getSinus(f0, A, ts, time, ShiftZero, ShiftPhaseDegree)
_y_t = -_x_t/2

ShiftPhaseDegree = 60
_t, _x_t_shift = sg.getSinus(f0, A, ts, time, ShiftZero, ShiftPhaseDegree)
_y_t_shift = -_x_t_shift/2

rows = 2
cols = 1

fig1 = plt.figure()#subplots()

ax1 = fig1.add_subplot(rows, cols, 1)
ax1.set_title('Рис. 1.1 - синусоидальный сигнал во временной области')
ax1.set_xlabel('t, s')
ax1.set_ylabel('x(t)')
ax1.grid(which="major", linewidth=1.2)
ax1.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)
ax1.plot(_t, _x_t)
ax1.plot(_t, _y_t)

ax2 = fig1.add_subplot(rows, cols, 2)
ax2.set_title('Рис. 1.1 - синусоидальный сигнал во временной области')
ax2.set_xlabel('t, s')
ax2.set_ylabel('x(t)')
ax2.grid(which="major", linewidth=1.2)
ax2.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)
ax2.plot(_t, _x_t_shift)
ax2.plot(_t, _y_t_shift)

plt.show()
