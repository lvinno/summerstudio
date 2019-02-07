import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import numpy as np
import os


I = mpimg.imread('./data/Siamese1/12. siamese-cat-food-header.jpg')

print(I.shape)
print(I)
plt.imshow(I)
plt.show()

