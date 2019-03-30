#!/usr/bin/env python

import numpy as np

import cv2

image_name = "akar"

print 'baca gambar dari file'
img = cv2.imread("Gambar/" + image_name + ".jpg")

print 'buat window holder untuk gambarnya'
cv2.namedWindow("Gambar", cv2.WINDOW_NORMAL)

print 'tampilkan gambar'
cv2.imshow("Gambar", img)

print 'press a key inside the image to make a copy'
cv2.waitKey(0)

print 'gambar di copy in ke folder Gambar/copy'
cv2.imwrite("Gambar/copy/" + image_name + "-copy.jpg", img)
