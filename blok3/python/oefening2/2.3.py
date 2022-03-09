# for p in range(1, 11):
#     print(2 * p - 1)
# print('I am tired of printing numbers')

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

#
# jojo = np.array(range(0, 10, 1))
#
# for counter in range(1, 5):
#     jojo2 = counter * jojo
#     plt.subplot(2, 2, counter), plt.plot(jojo, jojo2, 'bd-')
#     plt.xlabel('stupid xlabel')
#     plt.ylabel('very stupid ylabel')
# else:
#     plt.show()  # draw plots
#     plt.savefig('niceplot.pdf', format='pdf')  # save plots
#     print('I am tired of drawing plots, I would like to drink')
#     print('Nils Oscar lager from Stockholm')
# here the for-loop stops

# computerbrands = ["apple", "hp", "Acer", "dell"]
#
# for brand in computerbrands:
#     print(brand)

rawdata = np.array([0.5, 1, 2, 3, 5, 7, 13, 16, 20, 16, 13, 7, 5, 3, 2, 1, 0.5])

meanarray = []
currentmean = 0
for i in range(0, len(rawdata) - 1):
    currentmean = np.mean(rawdata[i:i + 2])
    meanarray.append(currentmean)



### 2.3D
mean3array = []
currentMean = 0
for x in range(0, len(rawdata) - 2):
    currentMean = np.mean(rawdata[x:x + 3])
    mean3array.append(currentMean)

### 2.3E
mean5array = []
currentMean = 0
for x in range(0, len(rawdata) - 4):
    currentMean = np.mean(rawdata[x:x + 5])
    mean5array.append(currentMean)

xvalue1 = [0, 0.5, 1, 2, 4, 6, 8, 10, 12, 13, 14, 15, 16, 18, 19, 20]
yvalue1 = meanarray

plt.plot(yvalue1)

xvalue2 = xvalue1
yvalue2 = mean3array

plt.plot(yvalue2)

xvalue3 = xvalue1
yvalue3 = mean5array

plt.plot(yvalue3)
plt.show()
