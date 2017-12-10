from sympy import symbols, solve, Eq

x1, x2, x3, x4 = symbols('x_1 x_2 x_3 x_4')

res = solve([Eq(x1 * x4, 1),
			Eq(x1 + 2 * x2 * x3, 0),
			Eq(x2 + 2 * x3 * x4, 0),
			Eq(x4, 0)],
			[x1, x2, x3, x4])

res2 = solve([Eq(x1 * x4, 0),
			Eq(x1 + 2 * x2 * x3, 0),
			Eq(x2 + 2 * x3 * x4, 0),
			Eq(x4, 1)],
			[x1, x2, x3, x4])

print("First system:", "No solution" if res == [] else res)
print("Second system:", "No solution" if res2 == [] else res2)