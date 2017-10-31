import matplotlib.pyplot as plt
import numpy as np

x = [0,
		0.5, 1, 2, 4, 8,
		0.5625, 1.125, 2.25, 4.5, 9,
		.625, 1.25, 2.5, 5, 10,
		.6875, 1.375, 2.75, 5.5, 11,
		.75, 1.5, 3, 6, 12,
		.8125, 1.625, 3.25, 6.5, 13,
		.875, 1.75, 3.5, 7, 14,
		.9375, 1.875, 3.75, 7.5, 14,
		.9375, 1.875, 3.75, 7.5, 15]
y = [0] * len(x)
x.append(0)
y.append(10)
s = [1] * len(x)
plt.plot(x, y, 'r|', ms=30)
plt.axhline(y=0, linestyle='-')

plt.show()