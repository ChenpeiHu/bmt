import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

a = sp.pi
b = a * 0.02
c = a * 2
xvalue = np.arange(0, c, b)
print(xvalue)

yvalue = np.sin(xvalue)
plt.plot(xvalue, yvalue, ':')

yvalue2 = yvalue + 0.5
plt.plot(xvalue, yvalue2)

yvalue3 = yvalue - 0.5
plt.plot(xvalue, yvalue3)

plt.show()

plt.suptitle("Mijn plot")

plt.subplot(3, 2, 1), plt.plot(xvalue, yvalue)
plt.subplot(3, 2, 2), plt.plot(xvalue, yvalue2)
plt.subplot(3, 2, 4), plt.plot(xvalue, yvalue2)
plt.subplot(3, 2, 6), plt.plot(xvalue, yvalue3)
plt.subplot(3, 4, 10), plt.plot(xvalue, yvalue)

plt.savefig('niceplot.pdf', format='pdf')
plt.show()
