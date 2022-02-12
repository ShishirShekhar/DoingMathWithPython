from sympy.plotting import plot
from sympy import Symbol, solve

def equation_graph():
	solutions = []
	for i in range(2):
		exp = input("Enter the equation in terms of x and y: ")
		y = Symbol('y')
		solution = solve(exp, y)
		solution = solution[0]
		solutions.append(solution)
	p = plot(solutions[0], solutions[1], legend=True, show=False)
	p[0].line_color = 'r'
	p[1].line_color = 'g'
	p.show()

if __name__ == '__main__':
	equation_graph()