# import the necessary shit
import scipy as sp
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
from PIL import Image
import random as ra

AgeOfCarl = 7
AgeOfRick = 8

if AgeOfCarl == AgeOfRick:
    response = 'Carl and Rick have the same age'
elif AgeOfCarl < AgeOfRick:
    response = 'Rick is older than Carl'
elif AgeOfCarl > AgeOfRick:
    response = 'Carl is older than Rick'
else:
    response = 'Wrong input for if statement'

# print(response)

# eenGetal = 5
#
# if eenGetal < 5:
#     print("yup, groter dan 5")
# else:
#     print("nope, kleiner dan 5")
#

# eenGetalenArray = np.array([1, 2, 3, 4, 5, 6, 7, 8])
#
# if len(eenGetalenArray) < 8:
#     print("yup, kleiner dan 8")
# else:
#     print("nope, groter dan 8")

eenZin = "ja dit is een zin"

if eenZin[0].isupper():
    print("yup, eerste letter is hoofdletter")
else:
    print('nope, geen hoofdletter')


