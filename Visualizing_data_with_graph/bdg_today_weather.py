"""
This modules give the graph to today's bodhgaya weather.
"""
import matplotlib.pyplot as plt

y = [31, 31.5, 31, 28, 28, 27, 27, 28]
x = ['11 am', '2 pm', '5 pm', '8 pm', '11 pm', '2 am', '5 am', '8 am']
y_ = [i for i in range(20, 41)]

plt.figure(figsize=(12,5))
plt.plot(x,y)
plt.title("Today's weather of bodhgaya")
plt.xlabel('Temp')
plt.ylabel('Time')
plt.yticks(ticks=y_)
plt.show()
