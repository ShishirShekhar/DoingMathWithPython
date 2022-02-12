"""
This module show trajectory of objects.
"""

import matplotlib.pyplot as plt
import math

def t_calculation(u, theta, g=9.8):
	"""This function calculates all the important variables"""
	theta = math.radians(theta)
	
	t_flight = 2 * u * math.sin(theta) / g
	t_list = time_interval(0, t_flight, 0.001)

	x = [u * t * math.cos(theta) for t in t_list]
	y = [u * t * math.sin(theta) - 0.5 * g * t ** 2 for t in t_list]

	return x, y, t_flight

def time_interval(start, final, interval):
	"""This function returns the time intervals"""
	t_list = []
	
	while start <= final:
		t_list.append(start)
		start += interval
	
	return t_list

if __name__ == "__main__":
	plt.figure(figsize=(12, 5))
	plt.title('Projectile motion')
	x, y, t_flight = t_calculation(25, 60)
	plt.plot(x, y)
	plt.xlabel('Distance')
	plt.ylabel('Height')
	plt.show()
