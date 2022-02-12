"""
Perform Fractional operations
"""
from fractions import Fraction

def main():
	f1 = Fraction(input('Enter the value of first fraction: '))
	op = input('Enter the operator(+, -, /, *): ')
	f2 = Fraction(input('Enter the value of second fraction: '))
	if op == '+':
		result = f1 + f2
	elif op == '-':
		result = f1 - f2
	elif op == '*':
		result = f1 * f2
	elif op == '/':
		result = f1 / f2
	else:
		print("We can't perform this operation")
	return result


if __name__ == '__main__':
	while True:
		print(main())
		a = input('Do you want to exit?(y/n)')
		if a == 'y':
			break
