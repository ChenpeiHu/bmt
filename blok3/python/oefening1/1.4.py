import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

#
# kyckling = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
# print(kyckling)
# print('1')
#
# kip = np.transpose(kyckling)
# print(kip)
# print('2')
#
# huhn = np.rot90(kyckling)
# print(huhn)
# print('3')
#
# poule = np.flipud(kyckling)
# print(poule)
# print('4')
#
# chicken = np.fliplr(kyckling)
# print(chicken)
# print('5')

twodimarray = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
sumthirdrow = np.sum(twodimarray[2,])
sumfirstcolumn = np.sum(twodimarray[:, 0])

sumthirdrow = np.sum(twodimarray[:, 2])

X = twodimarray[1, 1] + twodimarray[2, 0]
Y = np.sum(twodimarray[1, -2:])
print('X = ', X, 'Y = ', Y)
