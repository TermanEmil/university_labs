from RootFinders import newton
import numpy as np

def find_time_to_pay(a, r, p):
	f = lambda n: a * (1 + r)**n - p * ((1 + r)**n - 1) / r
	(x, xVals) = newton(1, 10**-6, f, verbose=False)
	return int(np.ceil(x))

def find_yearly_payments(a, r, n):
	f = lambda p: a * (1 + r)**n - p * ((1 + r)**n - 1) / r
	(x, xVals) = newton(1, 10**-6, f, verbose=False)
	return x

def find_interest(a, p, n):
	f = lambda r: a * (1 + r)**n - p * ((1 + r)**n - 1) / r
	(x, xVals) = newton(1, 10**-6, f, verbose=False)
	return x

print("Years to pay off the loan:", find_time_to_pay(100000, 0.06, 10000))
print("You must pay %.2f per year to pay off the loan in 20 year" % \
	find_yearly_payments(100000, 0.06, 20))
print("Yearly rate must be %.2f%% to pay off the loan in 20 years" % \
	(find_interest(100000, 10000, 20) * 100))