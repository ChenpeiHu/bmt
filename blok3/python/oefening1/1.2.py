import scipy as sp  # this is commenting
import numpy as np  # Python is blind for this
import matplotlib.pyplot as plt  # commenting is good

nicearray = np.arange(0, 105, 5)
carrot = np.sqrt(nicearray)
malicious = np.mean(nicearray)

# print(nicearray)
# print(malicious)

plt.plot(nicearray, carrot, 'r:')
plt.axis([0, 100, 0, 20])
plt.show()
