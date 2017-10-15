import matplotlib.pyplot as plt
import numpy as np

def markRegion(x1, x2, color, text):
	plt.axvspan(x1, x2, color = color, alpha = 0.2)
	plt.text((x1 + x2) / 2.0, 0, text)	

rootPath = '../report/imgs/'

x = [0, 1, 1, 3, 6, 7.8, 7.8]
y = [0, -1, 4.9, 1, -1.5, -2.5, 0]

fig, ax = plt.subplots(1)

ax.plot(x, y, 'o-')
plt.xlabel('R')
plt.ylabel('I')
ax.grid()

markRegion(x[0], x[1], 'red', 'r0')
markRegion(x[2], x[3], 'blue', 'R1')
markRegion(x[3], x[4], 'green', 'R2')
markRegion(x[4], x[5], 'purple', 'R3')

ax.set_yticklabels(['', '', '', 0])
ax.set_xticklabels([])

savePath = rootPath + 'PotentialChart.jpg'
plt.savefig(savePath)
plt.show()