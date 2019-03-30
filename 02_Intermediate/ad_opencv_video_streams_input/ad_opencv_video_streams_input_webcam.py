#!/usr/bin/env python

import numpy as np
import cv2

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('k'):    # cv2.waitKey(1000) untuk update motion
        break

video_capture.release()

cv2.destroyAllWindows()
