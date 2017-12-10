from math import pi
import matplotlib.pyplot as plt
from numpy import linspace

def gdd(x, y, cache = dict()):
	if len(x) == 1:
		return y[0]

	if cache.get((x, y)) != None:
		return cache[x, y]
	ret = (gdd(x[1:], y[1:]) - gdd(x[0:-1], y[0:-1]))/(x[-1] - x[0])
	cache[x, y] = ret
	return ret

def nthMember(x, y, n):
	g = gdd(x[:n + 1], y[:n + 1])
	retStr = ('+' if g >= 0 else '') + str(g)
	for i in range(0, n):
		retStr +=  "*(x - "+ str(x[i]) +")"
	return retStr

def my_interpolate(x, y):
	expr = str()
	for i in range(len(x) + 1):
		expr += nthMember(x, y, i)
	return lambda x : eval(expr)