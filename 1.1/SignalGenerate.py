import os
import numpy as np
import matplotlib.pyplot as plt

SelfFileName = os.path.basename(__file__)


# f0 - частота сигнала, Гц
# A - амплитуда сигнала в о.е.
# ts - время дискретизации, сек
# time - время генерации сигнала
# ShiftZero - сдвиг относительно оси "х" о.е. амплитуды
# ShiftPhaseDegree - сдвиг фазы в градусах
def getSinus(f0, A, ts, time, ShiftZero, ShiftPhaseDegree):
    print()
    print(SelfFileName,'-> Sinus generate begin:')
    
    T = 1/f0 # период, сек
    n = time/ts # кол-во отсчетов
    #ts = T/n # промежуток времени кантования, сек/отсчёт
    ShiftPhaseRadian = (ShiftPhaseDegree/180)*np.pi # сдвиг фазы в радианах(для рассчёта)
    n_array = np.arange(0, n, 1) # отсчёты(массив)
    
    print('A = ', A, ', амплитуда сигнала')
    print('ShiftPhaseDegree = ', ShiftPhaseDegree, ', градусы')
    print('ShiftPhaseRadian = ', ShiftPhaseRadian, ', радианы')
    print('f0 = ', f0, ',Гц - частота сигнала')
    print('T = ', T, ',сек - период сигнала')
    print('n = ', n, ', кол-во отсчётов')
    print('ts = ', ts, ',сек - период дискретизации')
    
    _tn = n_array * ts
    _x = 2 * np.pi * f0 * _tn
    _y = A * np.sin(_x + ShiftPhaseRadian) + ShiftZero

    print(SelfFileName,'<- Sinus generate end.\n')
          
    return _tn, _y
