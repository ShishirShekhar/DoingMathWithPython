"""This module visulize your expense"""

import matplotlib.pyplot as plt

def expens_v():
	i = int(input("Enter total number of categories you spent in: "))
	x = []
	y = []
	for expens in range(i):
		print("\n")
		cat = input("Enter the category: ")
		ex = int(input("Enter your expense: "))
		x.append(cat)
		y.append(ex)
	return x, y

if __name__ == '__main__':
	x, y = expens_v()
	plt.figure(figsize=(12, 5))
	plt.barh(x, y)
	plt.show()
