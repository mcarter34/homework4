#question 3
import matplotlib.pyplot as plt
import numpy as np

xpoints= np.array([0,1,2,3,4,5])
ypoints= np.array([2,4,6,14,10,12])

plt.plot(xpoints, ypoints, '--', color='r', marker='*', ms=10, mfc='g', mec='g')
plt.show()