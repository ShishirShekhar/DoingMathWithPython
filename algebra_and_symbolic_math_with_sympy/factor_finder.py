import sympy as s

def ffactor(expression):
	try:
		factors = s.solve(expression)
	except ValueError:
		print("Invalid sytanx")
	else:
		print(factors)


if __name__ == "__main__":
	ffactor("x**2 + 2x + 5")