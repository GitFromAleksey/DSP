import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines
import SignalGenerate as sg

print('Глава 2.3 - Дискретизация полосовых сигналов')

#fs' = 2 * fc + B или fs' = (2 * fc + B)/m
# fs' - частота дискретизации, Гц
# fc - центральная частота полосового сигнала, Гц
# B - ширина спектра полосового сигнала, Гц
# m - любое положительное целое число

# Условие для предотвращения наложений спектров:
# (2*fc - B)/m >= fs >= (2*fc + B)/(m + 1) 

fc = 20 * 10**6
B = 5 * 10**6
print('fc =', fc, ',Гц - центральная частота полосового сигнала')
print('B =', fc, ',Гц - ширина спектра полосового сигнала')

m = np.arange(1, 10, 1)
R = (fc + B/2)/B
fs_ = (2*fc - B)/m
fs__ = (2*fc - B)/(m + 1)

##i = 0
##while i < fs_.size:
##    print('m:',m[i], '\tfs_: %.1f'%fs_[i], '\tfs__: %.1f'%fs__[i])
##    i = i + 1

rows = 1
cols = 1

fig1 = plt.figure()

ax1 = fig1.add_subplot(rows, cols, 1)

i = 0
while i < fs_.size:
    line = matplotlib.lines.Line2D([i, fs_[i]], [i, fs__[i]])#, color="k")
    ax1.add_line(line)
    i = i + 1

plt.show()




