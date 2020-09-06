from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("parang 2.jpg", cv2.IMREAD_GRAYSCALE)

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(img, None)

# keypoints_sift, descriptors = sift.detectAndCompute(img, None)
img = cv2.drawKeypoints(img, kp, None)

cv2.imwrite('parang 2 sift.png', img)
plt.imshow(img),plt.title('image')
plt.xticks([]),plt.yticks([])
plt.show()