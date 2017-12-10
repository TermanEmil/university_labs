from my_interpolate import my_interpolate

from math import pi
import matplotlib.pyplot as plt
from numpy import linspace

x_range = linspace(-pi/2, pi, 200)

# Ex1
x = (0, pi/2, pi)
y = (0, 1, 0)
f = my_interpolate(x, y)
plt.plot(x_range, f(x_range), label = "quadratic")
plt.plot(x, y, 'ro')

# Ex2
x = (-pi/2, 0, pi/2, pi)
y = (-1, 0, 1, 0)
f = my_interpolate(x, y)
plt.plot(x_range, f(x_range), label = "cubic")

# Points
plt.plot(x, y, 'ro')
plt.legend()
plt.show()