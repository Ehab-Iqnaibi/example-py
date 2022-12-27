import numpy as np
import matplotlib.pyplot as plt
'''
#1 plot and show
plt.plot([-1, -2.0, 6, 10, 21.5])
plt.show()

#2 points
days = list(range(1, 8))
temperature = [10, 14, 16, 20, 20, 14, 17]
plt.plot(days, temperature, "or")
plt.show()

#3 X and Y Labels, Title
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.title('Temperature of the Week')
plt.plot(days, temperature,
          days, temperature, "or")
plt.show()

# figure and axes
import matplotlib.pyplot as plt
days = list(range(1, 8))
temperature = [10, 14, 16, 20, 20, 14, 17]
fig, ax = plt.subplots() # one axis

ax.set(xlabel='Days', ylabel='Temperature',
         title='Temperature of the Week')
ax.plot(days, temperature,
          days, temperature, "or")
plt.show()

#4 np with matplot
# 100 point start from -2pi to 2pi
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
f_sin = 3*np.sin(x)
f_2 = np.sin(2*x) - np.cos(x)
fig, ax = plt.subplots()
# x and y lim axis
startx, endx = -2 * np.pi - 0.1, 2*np.pi + 0.1
starty, endy = -4.0, 4.0
ax.axis([startx, endx, starty, endy])

ax.set(xlabel='x-axis',ylabel='y-axis',title='Some periodic functions')
ax.plot(x, f_sin, x, f_2)
plt.show()
'''
#4 spines,ticks,
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
f_sin = 3 * np.sin(x)
f_2 = np.sin(2 * x) - np.cos(x)
fig, ax = plt.subplots()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
ax.set_xticks([-2.0 * np.pi, -1.5 * np.pi, -1.0 * np.pi, -0.5 * np.pi,
                0.5 * np.pi, 1.0 * np.pi, 1.5 * np.pi, 2.0 * np.pi])
ax.set_yticks([-3, -1, +1, 3])
ax.set_title('Some periodic functions')
ax.plot(x, f_sin, '--', x, f_2, 'r')
plt.show()