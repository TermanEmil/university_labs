from scipy.integrate import quad
import numpy
from sympy import *

e = Symbol('e')

def	_integralF(x, k):
	return (numpy.e ** (-x)) * (x ** k)

def	integrateMyFunction(k):
	return quad(_integralF, 0, 1, args = (k))[0]

def	recursiveIntegrate(k):
	if k == 0:
		return 1 - 1 / e
	else:
		return k * recursiveIntegrate(k - 1) - 1 / e

for k in range(0, 25 + 25):
	expr = recursiveIntegrate(k)
	recursiveResult = expr.subs(e, numpy.e)

	printValues = (k, integrateMyFunction(k), recursiveResult, expr)
	print("%d)\t %lf : %lf (%s)" % printValues)

#Folosirea lui e duce la erori mici. Iar cand e * 42163840398198058854693626 e si mai mare
#Atunci cand aduni un numar mare cu un numar foarte mic, tot apar erori
#se poate de dat exemplu la nivel de mantisa - cum se stocheaza

#float pote stoca foarte bine numere foarte mici, dar are mari probleme cand stocheaza numere mari.

#atunci cand adun un numar foarte mare cu un numar foarte mic, exponentul la numarul
#mic trebuie sa fie egal cu exponentul la cel mare, astfel, bitii in mantisa se shifteaza
#creand acea erorae

#sa aflu eroare: o formula care depinde de acel u