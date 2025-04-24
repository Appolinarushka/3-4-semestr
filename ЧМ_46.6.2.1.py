import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def v(x, p, q, r, t):
    return p*x**3 + q*x**2 + r*x + t

x = np.linspace(-1/np.sqrt(3), 1/np.sqrt(3), 50)
y = np.arctan(x)

popt, pcov = curve_fit(v, x, y)

print("p =", popt[0])
print("q =", popt[1])
print("r =", popt[2])
print("t =", popt[3])

plt.plot(x, y, 'bo', label='data')
plt.plot(x, v(x, *popt), 'r-', label='fit')
plt.legend(loc='best')
plt.show()