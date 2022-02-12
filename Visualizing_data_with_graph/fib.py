import matplotlib.pyplot as plt

def fibo(n):
	if n == 1:
		return [1]
	elif n == 2:
		return [1, 1]
	elif n > 2:
		a = 1
		b = 1
		series = [a, b]
		for i in range(n):
			c = a + b
			series.append(c)
			a = b
			b = c
		return series


if __name__ == '__main__':
	n = 10
	series = fibo(n)
	ratio = [series[i] / series[i-1] for i in range(n+2)]
	plt.plot(series, ratio)
	plt.show()
