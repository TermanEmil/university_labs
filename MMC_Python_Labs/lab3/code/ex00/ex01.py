from RootFinders import newton
import numpy as np

def findTimeToPay(a, r, p):
	f = lambda n: a * (1 + r)**n - p * ((1 + r)**n - 1) / r
	(x, xVals) = newton(1, 10**-6, f, verbose=False)
	return int(np.ceil(x))

def findYearlyPayments(a, r, n):
	f = lambda p: a * (1 + r)**n - p * ((1 + r)**n - 1) / r
	(x, xVals) = newton(1, 10**-6, f, verbose=False)
	return x

def findInterest(a, p, n):
	f = lambda r: a * (1 + r)**n - p * ((1 + r)**n - 1) / r
	(x, xVals) = newton(1, 10**-6, f, verbose=False)
	return x


print(findTimeToPay(100000, 0.06, 10000))
print(findYearlyPayments(100000, 0.06, 20))
print(findInterest(100000, 10000, 20))