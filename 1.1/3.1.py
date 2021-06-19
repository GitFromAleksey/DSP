import sys
import numpy as np
import matplotlib.pyplot as plt
import SignalGenerate as sg
import cmath

def _complex():
    x_cplx = complex(1,2) #комплексное число
    y_cplx = complex(1,-2) #комплексное число
    x_cplx_module = abs(x_cplx)
    x_cplx_pow = pow(x_cplx, 2)

    print('x_cplx =', x_cplx, ', x_cplx.real =', x_cplx.real, ', x_cplx.imag =', x_cplx.imag)
    
    print('x_cplx_module =', x_cplx_module)
    print('x_cplx_pow =', x_cplx_pow)

    print('y_cplx =', y_cplx)

    print( '(x_cplx + y_cplx) =', (x_cplx + y_cplx) )
    print( '(x_cplx * y_cplx) =', (x_cplx * y_cplx) )
    print( '(x_cplx / y_cplx) =', (x_cplx / y_cplx) )


def GetDpfFreques(N_DPF, fs):
    res = []

    print('\nРассчёт начений частот ДПФ')    
    print('Частота дискретизации fs =', fs, 'Гц')
    print('Кол-во точек ДПФ N =', N_DPF)

    f_com = fs/N_DPF # основная частота синусоид

    print( 'fs/N =', f_com, 'Гц. - основная частота синусоид ДПФ')

    for i in range(N_DPF):
        tmp = (i * f_com)
        res.append(tmp)
        print('X(', i, ') = ', tmp, 'Гц.' )

    return np.array(res)

def main(argv):
    print('Глава 3.1 - Смысл формулы ДПФ')

    fs = 500 # частота дискретизации сигнала
    N = 16 # 16-ти точечное ДПФ
    f_com = fs/N # основная частота синусоид

    GetDpfFreques(N, fs)

    print('\nГлава 3.1.1 - Пример ДПФ №1\n')

# характеристики 1-го компонента сигнала
    f0_1 = 1000 # частота сигнала, Гц
    A_1 = 1 # амплитуда сигнала в о.е.
    ShiftPhaseDegree_1 = 0 # сдвиг фазы в градусах
# характеристики 2-го компонента сигнала
    f0_2 = 2000 # частота сигнала, Гц
    A_2 = 0.5 # амплитуда сигнала в о.е.
    ShiftPhaseDegree_2 = 135 # сдвиг фазы в градусах
# общие харектеристики
    fs = 8000 # Гц, частота дискретизации
    ts = 1/fs # время дискретизации, сек
    N = 8
    time = ts*N # время генерации, сек

    GetDpfFreques(N, fs)

    print('\nЗначения входной последовательности сигнала:')
    t_arr = np.arange(0, N, 1) * ts
    x_1 = A_1 * np.sin( 2*np.pi * f0_1 * t_arr )
    x_2 = A_2 * np.sin( 2*np.pi * f0_2 * t_arr + 3*np.pi/4 )
    x_in = np.round( (x_1 + x_2), 4)

    fig, ax = plt.subplots()
    ax.grid()
##    ax.plot(t_arr, x_1)
##    ax.plot(t_arr, x_2)
##    ax.plot(t_arr, x_in)


    cnt = 0
    for x in x_in:
        print('x(', cnt,') =',x)
        cnt += 1

    print('\nРассчёт значений гармоник:')
    X_list = []
    for m in range(N):
        X = complex()
        for n in range(N):
            r = np.round(x_in[n] * np.cos(2*np.pi*n*m/N), 4)
            im = (-1) * np.round((x_in[n] * np.sin(2*np.pi*n*m/N)), 4)
##            r = x_in[n] * np.cos(2*np.pi*n*m/N)
##            im = -(x_in[n] * np.sin(2*np.pi*n*m/N))
            tmp = complex(r,im)
            X += tmp
        X_list.append(abs(X))
        print('X(',m,') = %2.4f' % X.real,'%2.4f' % X.imag,'j')
        print(np.round(np.arcsin(X.imag/abs(X))*180/np.pi,1))
        print(np.round(np.arccos(X.real/abs(X))*180/np.pi,1))
##        print('  Модуль = %2.4f' % abs(X), 'Угол = %2.1f' % (180*np.arctan(X.imag/X.real)/np.pi) )
        print('  Модуль = %2.4f' % np.round(abs(X)), ', Угол = %2.1f' % (cmath.phase(X)*180/3.1415) )

    
##    ax.hist(X_list, 50, density=False)
##    ax.hist(X_list)
    plt.bar(np.arange(0, len(X_list),1), height=X_list)
    plt.show()
    
        
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
