import matplotlib.pyplot as plt
import numpy as np

rootPath = '../report/imgs/'

R3 = [0, 100, 200, 300, 467]
U1 = [14.93, 9.06, 7.57, 6.9, 6.35]
U2 = [0.06, 5.88, 7.42, 8.0, 8.64]
I1 = [144.3, 88.4, 74, 67.2, 62]
I2 = [0.2, 29.4, 37.1, 40.5, 43.3]
I3 = [143.5, 59.2, 36.7, 26.7, 18.6]

fig1 = plt.figure(figsize=(14.0, 7.0))

ax1 = plt.subplot(1, 2, 1)
ax1.set_title('U1, U2 = f(R3)')
plt.plot(R3, U1, 'o-', label = "U1", solid_joinstyle = 'round')
plt.plot(R3, U2, 'o--', label = "U2", solid_joinstyle = 'round')
plt.legend()
plt.xlabel('R3')
plt.ylabel('U (V)')
plt.grid()

ax2 = plt.subplot(1, 2, 2)
ax2.set_title('I1, I2, I3 = f(R3)')
plt.plot(R3, I1, 'o-', label = "I1", solid_joinstyle = 'round')
plt.plot(R3, I2, 'o--', label = "I2", solid_joinstyle = 'round')
plt.plot(R3, I3, 'bs-', color = 'red', label = "I3", solid_joinstyle = 'round')
plt.legend()
plt.xlabel('R3')
plt.ylabel('I (mA)')
plt.grid()

savePath = rootPath + 'U1U2_I1I2I3_R3_plot.jpg'
plt.savefig(savePath)

plt.show()