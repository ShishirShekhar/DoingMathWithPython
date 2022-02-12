"""
This modules give the graph to visulze quadratic equation.
"""
import matplotlib.pyplot as plt

x = [i for i in range(11)]
y = [i**2 + i*2 + 1 for i in x]

plt.figure(figsize=(12,5))
plt.plot(x,y)
plt.title("Quadratic equation")
plt.xlabel('x')
plt.ylabel('y')
plt.show()