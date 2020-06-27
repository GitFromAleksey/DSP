import numpy as np
import matplotlib.pyplot as plt
import SignalGenerate as sg

# _y(t) = sin(2*pi*f0*t) - непрерывный сигнал
# _y(n_array) = sin(2*pi*f0*n_array*ts) - дискретная последовательность

print('Глава 1.1')

##2^(1/12) = 1.059
##2^(2/12) = 1.122
##2^(3/12) = 1.189
##2^(4/12) = 1.260
##2^(5/12) = 1.335
##2^(6/12) = 1.414
##2^(7/12) = 1.498
##2^(8/12) = 1.587
##2^(9/12) = 1.682
##2^(10/12) = 1.782
##2^(11/12) = 1.888
##2^(12/12) = 2

f0 = 1 # частота сигнала, Гц
A = 1 # амплитуда сигнала в о.е.
ts = 0.001 # время дискретизации, сек
time = 10 # время генерации, сек
ShiftZero = 0 # сдвиг относительно оси "х" о.е. амплитуды
ShiftPhaseDegree = 0 # сдвиг фазы в градусах

_t, _y = sg.getSinus(f0, A, ts, time, ShiftZero, ShiftPhaseDegree)

_t1, _y1 = sg.getSinus(f0*(2**(3/12)), A, ts, time, ShiftZero, ShiftPhaseDegree)
_ys = _y + _y1

plt.title('Title')
plt.xlabel('t, s')
plt.ylabel('y(t)')
plt.grid(True)
plt.plot(_t, _ys)
plt.plot(_t, _y)
plt.plot(_t1, _y1)
##plt.scatter(_t, _y)
##plt.scatter(_t1, _y1)
plt.show()
