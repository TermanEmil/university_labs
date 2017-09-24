import fractions as fr
import numpy as np
import sys

# We can't use np.sinh or np.cosh or np.e ** n, for huge numbers, because
# the result becomes bigger than the float limit. That's why, we're using
# a continued fraction to determine the result, even though it's not perfectly
# precisive
# Sometimes we don't need such big precision

# why?: because there is a big number of operations with floats, which
# decreases the precision

# I noted that the sinh / cosh and the exponential methods don't generate that
# little error for big numbers, that's because there are less operations than
# lambert's method.

# Using fractions, is slower, but more precise. Using floats is faster but a bit
# less precise, which sometimes is fine

def		lambert_tanh_fractions(x, i):
	if i >= 1000:
		return 0
	if i == 1:
		return fr.Fraction(x / (i + lambert_tanh_fractions(x, i + 2)))
	return fr.Fraction((x ** 2) / (i + lambert_tanh_fractions(x, i + 2)))

def		lambert_tanh_floats(x, i):	
	if i >= 1000:
		return 0
	if i == 1:
		return x / (i + lambert_tanh_floats(x, i + 2))
	return (x ** 2) / (i + lambert_tanh_floats(x, i + 2))

def		evaluate_hyperbolic_tan(x):
	print("x = %d" % (x))
	print("lambert_fracs:\t\t %.20f" % (lambert_tanh_fractions(x, 1)))
	print("lambert_floats:\t\t %.20f" % (lambert_tanh_floats(np.float64(x), 1)))
	print("np.tanh:\t\t\t %.20f" % (np.tanh(x)))

	if (x <= 700):
		print("sinh / cosh:\t\t %.20f" % (np.sinh(x) / np.cosh(x)))
		print("exponential:\t\t %.20f" % ((np.e ** x - np.e ** (-x)) / (np.e ** x + np.e ** (-x))))

	print("")
	pass

sys.setrecursionlimit(1000)
evaluate_hyperbolic_tan(10)
evaluate_hyperbolic_tan(100)
evaluate_hyperbolic_tan(700)
evaluate_hyperbolic_tan(1000)