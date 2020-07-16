import numpy as np
import matplotlib.pyplot as plt
import SignalGenerate as sg

print('Глава 2.1 - Наложение: неоднозначность представоения сигнала в частотной области.')

f0 = 1 # частота сигнала, Гц
A = 1 # амплитуда сигнала в о.е.
ts = 0.1 # время дискретизации, сек
time = 1 # время генерации, сек
ShiftZero = 0 # сдвиг относительно оси "х" о.е. амплитуды
ShiftPhaseDegree = 0 # сдвиг фазы в градусах

n = time/ts
n_array = np.arange(0, n, 1)
fs = 1/ts

k = 0
##_x_n0 = np.sin(2*np.pi*(f0+k*fs)*n_array*ts)
_t0, _x_n0 = sg.getSinus(f0, A, ts, time, ShiftZero, ShiftPhaseDegree)

k = 1
f0_1 = f0+k*fs
##_x_n1 = np.sin(2*np.pi*(f0+k*fs)*n_array*ts)
_t1, _x_n1 = sg.getSinus(f0_1, A, ts/f0_1, time, ShiftZero, ShiftPhaseDegree)

k = 2
f0_2 = f0+k*fs
##_x_n2 = np.sin(2*np.pi*(f0+k*fs)*n_array*ts)
_t2, _x_n2 = sg.getSinus(f0_2, A, ts/f0_2, time, ShiftZero, ShiftPhaseDegree)

rows = 1
cols = 1
##fig1, ax1 = plt.subplots()
fig1 = plt.figure()#subplots()

ax1 = fig1.add_subplot(rows, cols, 1)
ax1.set_title('Рис. 1.1 - синусоидальный сигнал во временной области')
ax1.set_xlabel('t, s')
ax1.set_ylabel('x(t)')
ax1.grid(which="major", linewidth=1.2)
ax1.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)
ax1.scatter(_t0, _x_n0, color='red')
ax1.plot(_t0, _x_n0)
ax1.plot(_t1, _x_n1)
ax1.plot(_t2, _x_n2)

plt.show()
