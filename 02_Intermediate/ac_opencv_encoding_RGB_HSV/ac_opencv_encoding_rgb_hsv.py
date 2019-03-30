#!/usr/bin/env python

import numpy as np

import cv2

image_name = "nature2"

print 'baca gambar dari file'
img = cv2.imread("Gambar/" + image_name + ".jpg")

print 'display image in native color'
cv2.imshow("Gambar Asli", img)
cv2.moveWindow("Gambar Asli",0,0)
print(img.shape)

height,width,channels =img.shape

print '============ slipt the image into three channels, RGB ============'
blue,green,red = cv2.split(img)

cv2.imshow("Blue Channel", blue)
cv2.moveWindow("Blue Channel", 0, height)

cv2.imshow("Red Channel", red)
cv2.moveWindow("Red Channel", 0, height)

cv2.imshow("Green Channel", green)
cv2.moveWindow("Green Channel", 0, height)

# Hue : menyatakan warna sebenarnya, seperti merah, violet, dan kuning dan digunakan menentukan kemerahan (redness), kehijauan (greeness), dsb.
# Saturation : kadang disebut chroma, adalah kemurnian atau kekuatan warna.
# Value : kecerahan dari warna. Nilainya berkisar antara 0-100 %. Apabila nilainya 0 maka warnanya akan menjadi hitam, semakin besar nilai maka semakin cerah dan  muncul variasi-variasi baru dari warna tersebut.

print '============ slipt the image into HSV, Hue, Saturatin, Value ============'
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
hsv_image = np.concatenate((h,s,v), axis = 1)
cv2.imshow("Hue, Saturation, Value Image", hsv_image)
cv2.imshow("HSV Image", hsv)


print '============ converts an image to a greyscale ============'
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray_image)

print gray_image

cv2.waitKey(0)
cv2.destroyAllWindows()
