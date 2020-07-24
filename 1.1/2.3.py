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

fc = 20# * 10**6
B = 5# * 10**6
print('fc =', fc, ',Гц - центральная частота полосового сигнала')
print('B =', fc, ',Гц - ширина спектра полосового сигнала')

m = np.arange(1, 10, 1)
##R = (fc + B/2)/B
fs_ = ((2*fc - B)/m)/B
fs__ = ((2*fc - B)/(m + 1))/B
Rfs_ = (fs_ + B/2)/B
Rfs__ = (fs__ + B/2)/B

B_ = 30
m_ = 1
fs_max_1 = (2*fc + B_)/m_
print('fs_max_1 -', fs_max_1)
print('fs_max_1/B_ -', fs_max_1/B_)



##i = 0
##while i < fs_.size:
##    print('m:',m[i], '\tfs_: %.1f'%fs_[i], '\tfs__: %.1f'%fs__[i])
##    i = i + 1

rows = 1
cols = 1

fig1 = plt.figure()

ax1 = fig1.add_subplot(rows, cols, 1)

ax1.set_xlim([2, 11])
ax1.set_ylim([0, 4])

Bmin = 2*fc/(2*m + 1)
Bmax = 10
i = 0
for _m in m:
    fs_1 = (2*fc + Bmin[i])/(_m+1)
    fs_2 = (2*fc + Bmax)/(_m+1)
    R_1 = (fc + 2*Bmin[i])/Bmin[i]
    R_2 = (fc + 2*Bmax)/Bmax

    line = matplotlib.lines.Line2D([R_1, fs_1/Bmin[i]], [R_2, fs_2/Bmax])#, color="k")
    ax1.add_line(line)
    
    i = i + 1

plt.show()




