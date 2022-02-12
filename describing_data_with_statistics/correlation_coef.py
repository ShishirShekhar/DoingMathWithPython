"""
Find the correlation between the sets
"""
def find_corr_x_y(x, y):
	n = len(x)
	if n == len(y):
		x_sum = sum(x)
		x_sum_squared = x_sum ** 2
		x_squared_sum = sum([i ** 2 for i in x])

		y_sum = sum(y)
		y_sum_squared = y_sum ** 2
		y_squared_sum = sum([i ** 2 for i in y])

		xy_sum = sum([i * j for i, j in zip(x, y)])

		numerator = n * xy_sum - x_sum * y_sum
		denominator_term1 = n * x_squared_sum - x_sum_squared
		denominator_term2 = n * y_squared_sum - y_sum_squared
		denominator = (denominator_term1 * denominator_term2) ** 0.5

		correlation = numerator / denominator
		return correlation
			
	else:
		print("Correaltion can not be found\nx and are of different length.")

if __name__ == '__main__':
	x = [i for i in range(11)]
	y = [i for i in range(11)]
	print(find_corr_x_y(x, y))