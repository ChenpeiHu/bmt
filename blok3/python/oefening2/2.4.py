import numpy as np

kyckling = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(kyckling)
print('1')

kip = np.transpose(kyckling)
print(kip)
print('2')

huhn = np.rot90(kyckling)
print(huhn)
print('3')

poule = np.flipud(kyckling)
print(poule)
print('4')

chicken = np.fliplr(kyckling)
print(chicken)
print('5')