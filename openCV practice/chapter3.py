from cv2 import cv2
import numpy as np

img = cv2.imread("Resources/lambo.png")
print(img.shape)

imgResize = cv2.resize(img, (1000, 500))
print(imgResize.shape)

imgCropped = img[0:200, 200:500]

cv2.imshow("image", img)
cv2.imshow("image Resize", imgResize)
cv2.imshow("cropped", imgCropped)

cv2.waitKey(0)