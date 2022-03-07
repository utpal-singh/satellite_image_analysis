# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 17:18:42 2022

@author: utpal-singh
"""

import rasterio as rio
from osgeo import gdal
import matplotlib.pyplot as plt
import numpy as np

hyperion = rio.open('data/aster/export_to_python/layer_stack.tif')
hyperion_array = hyperion.read()

nRows = hyperion_array.shape[1]
nCols = hyperion_array.shape[2]
Bands = hyperion_array.shape[0]


plt.figure(figsize=(10, 10))
plt.imshow(hyperion_array[5, :, :], cmap='gray')
plt.show()

# Visualizing DSM
plt.figure(figsize=(9, 9))
plt.imshow(hyperion_array[0, :, :], cmap='jet')
plt.xticks([])
plt.yticks([])
plt.show()


hyperion_flatten_null = []
for elements in hyperion_array.flatten():
    if elements == 0:
        continue
    else:
        hyperion_flatten_null.append(elements)

# Let's look at it's histogram!
plt.figure(figsize=(10, 7))
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Hyperion Histogram')
n, bins, patches = plt.hist(x=hyperion_flatten_null, bins=100, color='#0504aa',
                            alpha=0.7, rwidth=0.85)




