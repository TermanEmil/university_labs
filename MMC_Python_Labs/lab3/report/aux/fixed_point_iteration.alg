x = x0;

while |x - f(x)| > tolerance:
	x = f(x);

return x;