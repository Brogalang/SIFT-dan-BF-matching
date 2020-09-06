from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("kawung 1.jpg", cv2.IMREAD_GRAYSCALE)

#sift = cv2.xfeatures2d.SIFT_create()
#kp = sift.detect(img, None)

# keypoints_sift, descriptors = sift.detectAndCompute(img, None)
#img = cv2.drawKeypoints(img, kp, None)

cv2.imwrite('1.kawung 1 grayscale.png', img)
plt.imshow(img),plt.title('image')
plt.xticks([]),plt.yticks([])
plt.show()