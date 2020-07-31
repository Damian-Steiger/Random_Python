#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import math

plt.axis([0, 100, -5, 5])

array = np.linspace(0,100,1000)

for i in range(100):
    sin_y = np.sin(array[i])
    cos_y = np.cos(array[i])
    tan_y = np.tan(array[i])
    plt.scatter(i, sin_y, c = 'r')
    plt.scatter(i, cos_y, c = 'b')
    plt.scatter(i, tan_y, c = 'g')
    plt.legend(["SIN", "COS", "TAN"])
    plt.pause(0.00001)

plt.show()
