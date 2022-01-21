# plot2.py
"""
A Parametric plot
"""

import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, np.pi, 1000)
x = 0.7*np.sin(t+1)*np.sin(3*t)
y = 0.7*np.cos(t+1)*np.sin(3*t)
plt.xlabel('x(t)')
plt.ylabel('y(t)')
plt.title('Parametric Plot')
plt.plot(x,y,color = 'blue')
plt.show()