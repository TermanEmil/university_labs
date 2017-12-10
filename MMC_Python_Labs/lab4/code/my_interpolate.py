from math import pi
import matplotlib.pyplot as plt
from numpy import linspace


def general_divided_dif(x, y, cache = dict()):
	if len(x) == 1:
		return y[0]

	if cache.get((x, y)) != None:
		return cache[x, y]

	f_from_1_to_n = general_divided_dif(x[1:], y[1:])
	f_from_0_to_n_minus_1 = general_divided_dif(x[0:-1], y[0:-1])

	ret = (f_from_1_to_n - f_from_0_to_n_minus_1) / (x[-1] - x[0])
	cache[x, y] = ret
	return ret

# Find the string equation of the n-th order divided difference.
def nth_member(x, y, n):
	g = general_divided_dif(x[:n + 1], y[:n + 1])
	equation_str = ('+' if g >= 0 else '') + str(g)

	for i in range(0, n):
		equation_str +=  "*(x - "+ str(x[i]) +")"
	return equation_str

# General divided differences.
def my_interpolate(x, y):
	expr = str()
	for i in range(len(x) + 1):
		expr += nth_member(x, y, i)
	return lambda x : eval(expr)