import pylab as pl
import numpy as np
import matplotlib.cm as cm
from PIL import Image  # do not ask me why


def putimageonscreen(mypicture):
    pl.imshow(mypicture, cmap=cm.gray)
    pl.show()


# End of function

# open picture1.jpg
img1 = Image.open('pictures/picture1.jpg')
img2 = Image.open('pictures/picture2.jpg')
img3 = Image.open('pictures/picture3.jpg')
img4 = Image.open('pictures/picture4.jpg')
mypicture1 = np.flipud(np.asarray(img1))
mypicture2 = np.transpose(np.flipud(np.asarray(img2)))
mypicture3 = np.fliplr(np.asarray(img3))
mypicture4 = np.asarray(img4)

deel1en2 = np.vstack((mypicture1, mypicture2))
print(deel1en2)

deel3en4 = np.vstack((mypicture4, mypicture3))
print(deel3en4)

helefoto = np.hstack((deel1en2, deel3en4))
putimageonscreen(helefoto)
