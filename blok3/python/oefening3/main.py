# import what you need
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp


# vect1 = np.array([2, 2, 8, 2, 4])
# print(vect1)
#
# hello = vect1 == 8
# print(hello)
#
# hello1 = vect1 == 2
# print(hello1)
#
# hello3 = hello1 & hello
# print(hello3)
#
# hello4 = ~hello
# print(hello4)
#
# hello8 = hello1 | hello
# print(hello8)

# yvalue = np.random.rand(10)
# print(yvalue)
# xvalue = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(xvalue)
#
# plt.subplot(1, 2, 1), plt.plot(xvalue, yvalue, 'bd')
# plt.axis([0, 10, 0, 1])
#
# # select the elements in yvalue that contain
# # values larger than 0.5
#
# # Keep in mind that “my_selection” is just a name for a
# # variable representing a Boolean vector. If you replace
# # “my_selection” in the script with “potato_salad” the script
# # still runs properly.
#
# my_selection = yvalue > 0.5
# newxvalue = xvalue[my_selection]
# newyvalue = yvalue[my_selection]
#
# plt.subplot(1, 2, 2), plt.plot(newxvalue, newyvalue, 'rd')
# plt.axis([0, 10, 0, 1])
# plt.show()

vect1 = np.array([3, 1, 1, 5, 5, 1, 18])
ddrie = vect1 < 4
print(ddrie)

print(vect1[ddrie])