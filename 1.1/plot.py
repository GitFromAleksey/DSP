import numpy as np
import matplotlib.pyplot as plt


fig, _ = plt.subplots()
print(type(fig))
print(type(_))

one_tick = fig.axes[0].yaxis#.get_major_ticks()[0]
print(type(one_tick))
print(one_tick)
