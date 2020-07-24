import sys
import numpy as np
import matplotlib.pyplot as plt
import SignalGenerate as sg

print('Глава 3.1 - Смысл формулы ДПФ')

##def X(x_n, N):


def main(argv):
    f1 = 1000 # частота сигнала, Гц
    f2 = 2000 # частота сигнала, Гц

    A1 = 1 # амплитуда сигнала в о.е.
    A2 = 0.5 # амплитуда сигнала в о.е.
    
    ShiftZero1 = 0 # сдвиг относительно оси "х" о.е. амплитуды
    ShiftPhaseDegree1 = 0 # сдвиг фазы в градусах

    ShiftZero2 = 0 # сдвиг относительно оси "х" о.е. амплитуды
    ShiftPhaseDegree2 = 135 # сдвиг фазы в градусах

    ts = 1/(8000) # время дискретизации, сек
    time = 1/f1 # время генерации, сек

    _t, _x1_t = sg.getSinus(f1, A1, ts, time, ShiftZero1, ShiftPhaseDegree1)
    _t, _x2_t = sg.getSinus(f2, A2, ts, time, ShiftZero2, ShiftPhaseDegree2)
    _x_sum = _x1_t + _x2_t

    i = 0
    for x in _x_sum:
        print('x(',i,')=%.4f'%x)
        i = i + 1

    rows = 1
    cols = 1
    fig1 = plt.figure()

    ax1 = fig1.add_subplot(rows, cols, 1)
    ax1.set_title('Рис. 1.1 - синусоидальный сигнал во временной области')
    ax1.set_xlabel('t, s')
    ax1.set_ylabel('x(t)')
    ax1.grid(which="major", linewidth=1.2)
    ax1.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)
    ax1.plot(_t, _x1_t)
    ax1.plot(_t, _x2_t)
    ax1.plot(_t, _x_sum)

    plt.show()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
