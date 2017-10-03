import matplotlib.pyplot as plt

def	fib1(n):
	global iterations
	iterations += 1

	if n < 2:
		return n
	else:
		return fib1(n - 1) + fib1(n - 2)

xPltData = []
yPltData = []

for n in xrange(30):
	iterations = 0
	fib1(n)
	xPltData += [n]
	yPltData += [iterations]

plt.title("Recursive fibonaci")
plt.xlabel("n")
plt.ylabel("Iterations")

plt.plot(xPltData, yPltData)
plt.show()