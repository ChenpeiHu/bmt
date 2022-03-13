# import what you need
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

x = np.random.uniform(-1, 1, 200)
y = np.random.uniform(-1, 1, 200)

plt.subplot(3, 2, 1), plt.plot(x, y, 'bd')
plt.axis([-1, 1, -1, 1])

x_groter_dan_0 = x > 0
y_groter_dan_0 = y > 0
x_kleiner_dan_0 = x < 0
y_kleiner_dan_0 = y < 0
zelfde_tekens = ((x > 0) & (y > 0)) | ((x < 0) & (y < 0))

plt.subplot(3, 2, 2), plt.plot(x[x_groter_dan_0][:80], y[y_groter_dan_0][:80], "md")
plt.subplot(3, 2, 3), plt.plot(x[x_kleiner_dan_0][:80], y[y_kleiner_dan_0][:80], "rd")
plt.subplot(3, 2, 4), plt.plot(x[x_kleiner_dan_0][:80], y[y_kleiner_dan_0][:80], "gd")
plt.subplot(3, 2, 5), plt.plot(x[zelfde_tekens][:80], y[zelfde_tekens][:80], "yd")
plt.tight_layout()
plt.show()