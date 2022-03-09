# import what you need
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

x = np.random.uniform(-1, 1, 200)
y = np.random.uniform(-1, 1, 200)

plt.subplot(1, 3, 1), plt.plot(x, y, 'bd')
plt.axis([-1, 1, -1, 1])


mySelection = (x > 0) & (y > 0)


def pos(array):
    return [a for a in array if a > 0] or None


def neg(array):
    return [a for a in array if a < 0] or None


positiveX = pos(x)[:90]
positiveY = pos(y)[:90]

negativeX = neg(x)[:90]
negativeY = neg(y)[:90]

plt.subplot(1, 3, 2), plt.plot(positiveX, positiveY, 'rd')
plt.axis([0, 1, 0, 1])
plt.title("positive")


plt.subplot(1, 3, 3), plt.plot(negativeX, negativeY, 'gd')
plt.axis([-1, 0, -1, 0])
plt.title("negative")
plt.show()
