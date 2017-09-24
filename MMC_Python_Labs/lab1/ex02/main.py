import fractions as fr
import decimal as dc

# Using fractions instead of floats helps us avoid the float difference error.
# Floating point isn't the best way to calculate scientific stuff, that's why
# we use fractions of fixed point floats

# Fixed floating points are more reliable but sometimes less precise since the
# float is saved in a int, generating a consistent result.

def	float_method():
	print("\nFloating point method")
	t = 0.1

	for n in range (1, 10):
		e = n / 10.0 - n * t
		print (e)

def	fractional_method():
	print("\nFractional method")
	t = fr.Fraction(1, 10)

	for n in range (1, 10):
		e = fr.Fraction(n, 10) - (n * t)
		print (e)

def	fixed_point():
	print("\nFixed point method")
	dc.getcontext().prec = 20
	t = dc.Decimal(1) / dc.Decimal(10)

	for n in range (1, 10):
		e = dc.Decimal(n) / 10 - n * t
		print (e)

float_method()
fractional_method()
fixed_point()
