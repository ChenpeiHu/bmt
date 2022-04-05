# import what you need
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

x = np.random.uniform(-1, 1, 200)
y = np.random.uniform(-1, 1, 200)

plt.subplot(2, 2, 1), plt.plot(x, y, 'bd')
plt.axis([-1, 1, -1, 1])

groter_dan_0 = (x > 0) & (y > 0)
kleiner_dan_0 = (x < 0) & (y < 0)
zelfde_tekens = ((x > 0) & (y > 0)) | ((x < 0) & (y < 0))

plt.subplot(2, 2, 2), plt.plot(x[groter_dan_0], y[groter_dan_0], "md")
plt.subplot(2, 2, 3), plt.plot(x[kleiner_dan_0], y[kleiner_dan_0], "gd")
plt.subplot(2, 2, 4), plt.plot(x[zelfde_tekens], y[zelfde_tekens], "yd")
plt.tight_layout()
plt.show()
