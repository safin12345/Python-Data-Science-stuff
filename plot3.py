# plot3.py
"""
Two curves on one plot
"""

import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0, 2, 0.01)
c = 1+np.cos(2*np.pi*t)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t,s,'b--',t,c,'c.-')
plt.xlabel('Time(s)')
plt.ylabel('Voltage (mV)')
plt.title('Voltage-Time Plot')
plt.grid(True)
plt.savefig('Voltage-Time Plot.jpg')
plt.show()