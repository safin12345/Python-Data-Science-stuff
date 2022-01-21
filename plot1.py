# plot1.py
"""
Our first plot
"""

import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(-2,2,100)
y = x**2
plt.xlabel('x')
plt.ylabel('y')
plt.title('$y=x^2$')
plt.plot(x,y)
plt.show()
