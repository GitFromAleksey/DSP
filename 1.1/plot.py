import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
import numpy as np

# генерация данных для построения графика
x = np.linspace(0, 10, 10)
y1 = 4*x
y2 = [i**2 for i in x]

# получение экземпляра чего-то там...
fig, ax = plt.subplots(figsize=(8, 6))

ax.set_title("Графики зависимостей: y1=4*x, y2=x^2", fontsize=16)

# название горизонтальной оси
ax.set_xlabel("x", fontsize=14)
# название вертикальной оси
ax.set_ylabel("y1, y2", fontsize=14)

# описание толстых линий сетки
ax.grid(which="major", linewidth=1.2)
# описание тонких(промежуточных) линий сетки
ax.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)

# рисование графика точками
ax.scatter(x, y1, c="red", label="y1 = 4*x")
# рисование графика линией
ax.plot(x, y2, label="y2 = x^2")
# отображение легенды(label в предыдущих двух действиях)
ax.legend()

# мелкая сектка
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())

# штрихи на осях
ax.tick_params(which='major', length=10, width=2)
ax.tick_params(which='minor', length=5, width=1)

plt.show()
