import numpy as np
import matplotlib.pyplot as plt
import SignalGenerate as sg

# _x_t(t) = sin(2*pi*f0*t) - непрерывный сигнал
# _x_t(n_array) = sin(2*pi*f0*n_array*ts) - дискретная последовательность

print('Глава 1.1')

##2**(1/12) = 1.059
##2**(2/12) = 1.122
##2**(3/12) = 1.189
##2**(4/12) = 1.260
##2**(5/12) = 1.335
##2**(6/12) = 1.414
##2**(7/12) = 1.498
##2**(8/12) = 1.587
##2**(9/12) = 1.682
##2**(10/12) = 1.782
##2**(11/12) = 1.888
##2**(12/12) = 2

f0 = 1 # частота сигнала, Гц
A = 1 # амплитуда сигнала в о.е.
ts = 0.001 # время дискретизации, сек
time = 1 # время генерации, сек
ShiftZero = 0 # сдвиг относительно оси "х" о.е. амплитуды
ShiftPhaseDegree = 0 # сдвиг фазы в градусах

_t, _x_t = sg.getSinus(f0, A, ts, time, ShiftZero, ShiftPhaseDegree)

_t1, _x1_t = sg.getSinus(f0*2, A/2, ts, time, ShiftZero, ShiftPhaseDegree)
_x_t_summ = _x_t + _x1_t

##plt.title('Рис. 1.1 - синусоидальный сигнал во временной области')
##plt.xlabel('t, s')
##plt.ylabel('x(t)')
##plt.grid(True)
####plt.plot(_t, _x_t_summ)
##plt.plot(_t, _x_t)
##plt.plot(_t1, _x1_t)
####plt.scatter(_t, _x_t)
####plt.scatter(_t1, _x1_t)

rows = 3
cols = 1
##fig1, ax1 = plt.subplots()
fig1 = plt.figure()#subplots()

ax1 = fig1.add_subplot(rows, cols, 1)
ax1.set_title('Рис. 1.1 - синусоидальный сигнал во временной области')
ax1.set_xlabel('t, s')
ax1.set_ylabel('x(t)')
ax1.grid(which="major", linewidth=1.2)
ax1.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)
ax1.plot(_t, _x_t)

ax2 = fig1.add_subplot(rows, cols, 2)
ax2.set_title('сигнал двойной частоты и половинной амплитуды')
ax2.set_xlabel('t, s')
ax2.set_ylabel('x(t)')
ax2.grid(which="major", linewidth=1.2)
ax2.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)
ax2.plot(_t, _x1_t)

ax3 = fig1.add_subplot(rows, cols, 3)
ax3.set_title('сумма двух сигналов')
ax3.set_xlabel('t, s')
ax3.set_ylabel('x(t)')
ax3.grid(which="major", linewidth=1.2)
ax3.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)
ax3.plot(_t, _x_t_summ)

plt.show()


