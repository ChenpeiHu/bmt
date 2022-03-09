import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

jojo = np.array(range(0, 10, 1))

for counter in range(1, 5):
    jojo2 = counter * jojo
    plt.subplot(2, 2, counter), plt.plot(jojo, jojo2, 'bd-')
    plt.xlabel('stupid xlabel')
    plt.ylabel('very stupid ylabel')
else:
    plt.show()  # draw plots
    plt.savefig('niceplot.pdf', format='pdf')  # save plots
    print('I am tired of drawing plots, I would like to drink')
    print('Nils Oscar lager from Stockholm')
# here the for-loop stops
