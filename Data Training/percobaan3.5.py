import numpy as np
import cv2 as cv
import time
from matplotlib import pyplot as plt

start = time.time()

img1 = cv.imread('grompol 1.jpg',0)          # queryImage
img2 = cv.imread('grompol 2.jpg',0) # trainImage

method = 'SIFT' #ORB
lower_ratio = 0.80

if method   == 'ORB':
    finder = cv.ORB_create()
elif method == 'SIFT':
    finder = cv.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = finder.detectAndCompute(img1,None)
kp2, des2 = finder.detectAndCompute(img2,None)

# BFMatcher with default params
bf = cv.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

# Apply ratio test
good = []

for m,n in matches:
    if m.distance < lower_ratio*n.distance:
        good.append([m])
#dist = 1 - len(good) / (max(len(img1.distance), len(img2.distance)))

msg1 = 'using %s with lowe_ratio %.2f' % (method, lower_ratio)
msg2 = 'there are %d good matches' % (len(good))

img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,good, None, flags=2)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img3,msg1,(25, 240), font, 1,(0,100,0),1,cv.FONT_HERSHEY_TRIPLEX
)
cv.putText(img3,msg2,(25, 270), font, 1,(0,100,0),1,cv.FONT_HERSHEY_TRIPLEX
)
fname = 'hahahaha_%s_%.2f.png' % (method, lower_ratio)

print('It took', time.time()-start, 'seconds.')

#cv.imwrite(fname, img3)

plt.imshow(img3),plt.show()
#cv.imshow('Foto Normal', img3)
#cv.waitKey(0)
#cv.destroyAllWindows()