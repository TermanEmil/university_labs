x1, x2, x3 = x0, x0, x0

do
{
	x0 = x1;
	x1 = f(x0);
	x2 = f(x1);
	$\lambda$ = (x2 - x1) / (x1 - x0);
	x3 = x2 + $\frac{\lambda}{1 - \lambda} (x2 - x1)$;
	x1 = x3;
} while |x3 - x2| < tolerance;

return x1;