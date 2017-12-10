import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

x = [0, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95, 1]
y = [0, 1, 5, 15, 33.5, 33, 16.50, 16, 16, 16, 16, 16, 6, 2, 0]

# Canvas
canvas = plt.figure()
rect = canvas.patch
rect.set_facecolor('white')

x_sm = np.array(x)
y_sm = np.array(y)

x_smooth = np.linspace(x_sm.min(), x_sm.max(), 2000)
y_smooth = spline(x, y, x_smooth)

sp1 = canvas.add_subplot(1,1,1, facecolor='w')
sp1.plot(x_smooth, y_smooth, 'red', linewidth=1)
sp1.plot(x, y, 'purple', linewidth = 1)

sp1.set_xlabel('time', color='dimgray')
sp1.set_ylabel('Thrust', color='dimgray')

plt.grid(alpha=0.8)
plt.show()