import matplotlib.pyplot as plt
import csv
from datetime import datetime
import numpy as np


x, y ,z= np.loadtxt('speed.csv', delimiter=',', unpack=True)
plt.plot(x,y, label='Speed')
plt.xlabel('Time')
plt.ylabel('Speed')
plt.title('Speed V/S Time')
plt.legend()
plt.show()