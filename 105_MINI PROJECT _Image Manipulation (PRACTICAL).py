# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 20:21:12 2024

@author: prash
"""

import numpy as np

from skimage import io

import matplotlib.pyplot as plt

camaro = io.imread("camaro.jpg")
print(camaro)

camaro.shape

plt.imshow(camaro)
plt.show()

#Cropping the image

cropped = camaro[0:500,:,:]
plt.imshow(cropped)
plt.show()

cropped = camaro[:,400:1000,:]
plt.imshow(cropped)
plt.show()

cropped = camaro[350:1050,200:1350,:]
plt.imshow(cropped)
plt.show()


#Save the image

io.imsave("camaro_cropped.jpg",cropped)

#Flip the image

verticle_flip = cropped = camaro[::-1,:,:]
plt.imshow(verticle_flip)
plt.show()

io.imsave("camaro_cropped_vertical_flip.jpg",verticle_flip)


horizontal_flip = cropped = camaro[:,::-1,:]
plt.imshow(horizontal_flip)
plt.show()

io.imsave("camaro_cropped_horizontal_flip.jpg",horizontal_flip)





#colour channels


red =np.zeros(camaro.shape, dtype = "uint8")

red[:,:,0] = camaro[:,:,0]

plt.imshow(red)
plt.show()



green =np.zeros(camaro.shape, dtype = "uint8")

green[:,:,1] = camaro[:,:,1]

plt.imshow(green)
plt.show()


blue =np.zeros(camaro.shape, dtype = "uint8")

blue[:,:,2] = camaro[:,:,2]

plt.imshow(blue)
plt.show()



camaro_rainbow = np.vstack((red,green,blue))

plt.imshow(camaro_rainbow)
plt.show()

io.imsave("camaro_rainbow.jpg",camaro_rainbow)





