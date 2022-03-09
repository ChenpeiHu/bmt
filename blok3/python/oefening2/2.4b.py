import pylab as pl
import numpy as np
import matplotlib.cm as cm
from PIL import Image  # do not ask me why

# This is a function that visualizes matrices
# Each 8-bit number is a gray value
def putimageonscreen(mypicture):
    pl.imshow(mypicture, cmap=cm.gray)
    pl.show()

# End of function

kros = np.array([[0, 255, 0], [255, 128, 255], [0, 255, 0]])
print(kros)
putimageonscreen(kros)
print('')

superkros = np.vstack((kros, kros))
print(superkros)
putimageonscreen(superkros)
print('')

megakros = np.hstack((superkros, superkros))
print(megakros)
putimageonscreen(megakros)