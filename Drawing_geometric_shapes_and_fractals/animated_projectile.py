"""
This module show trajectory of objects.
"""

import matplotlib.pyplot as plt
from matplotlib import animation
import math


g = 9.8

def get_interval(u, theta):
	"""This function returns the time intervals"""
	t_flight = 2*u*math.sin(theta)/g
	intervals = []
	start = 0
	interval = 0.005
	while start < t_flight:
		intervals.append(start)
		start += interval
	return intervals


def update_position(i, circle, intervals, u, theta):
	t = intervals[i]
	x = u * t * math.cos(theta)
	y = u * t * math.sin(theta) - 0.5 * g * t ** 2
	circle.center = x, y
	return circle


def create_animation(u, theta):
		intervals = get_interval(u, theta)

		xmin = 0
		xmax = u * math.cos(theta) * intervals[-1]
		ymin = 0
		t_max = u*math.sin(theta)/g
		ymax = u * t_max * math.sin(theta) - 0.5 * g * t_max ** 2
		fig = plt.gcf()
		ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))
		
		circle = plt.Circle((xmin, ymin), 1.0)
		ax.add_patch(circle)
		anim = animation.FuncAnimation(fig, update_position, fargs=(circle, intervals, u, theta), frames=len(intervals), interval=1, repeat=False)

		plt.title("Projectile motion")
		plt.xlabel("X")
		plt.ylabel("Y")
		plt.show()



if __name__ == "__main__":
	try:
		u = float(input("Enter the initial velocity (m/s): "))
		theta = float(input("Enter the angle of projection (degrees): "))
	except ValueError:
		print("You entered an invalid input")
	else:
		theta = math.radians(theta)
		create_animation(u, theta)