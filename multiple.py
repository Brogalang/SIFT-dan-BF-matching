import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import time
#for h in range (1, 3):

for h in range(1, 13):
    for i in range(1, 22):
        #img1 = cv.imread('/media/gasai/Nguli/Percobaan/Data Training/parang %d.jpg' % (h),0)  # queryImage
        #img2 = cv.imread('/media/gasai/Nguli/Percobaan/Data Testing/grompol %d.jpg' % (i),0) 

        img1 = cv.imread('F:/Percobaan/Data Rotate 5/kawung %d.jpg' % (h),0)  # queryImage
        img2 = cv.imread('F:/Percobaan/Data Testing/parang %d.jpg' % (i),0)
            
        #gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
        #gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
        (thresh, imb1) = cv.threshold(img1, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
        (thresh, imb2) = cv.threshold(img2, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
        
        start_time = time.time()
        
        method = 'SIFT' #ORB
        lower_ratio = 0.8
        
        if method   == 'ORB':
            finder = cv.ORB_create()
        elif method == 'SIFT':
            finder = cv.xfeatures2d.SIFT_create()
        
        # find the keypoints and descriptors with SIFT
        kp1, des1 = finder.detectAndCompute(imb1,None)
        kp2, des2 = finder.detectAndCompute(imb2,None)
        
        # BFMatcher with default params
        bf = cv.BFMatcher()
        matches = bf.knnMatch(des1,des2, k=2)
        
        # Apply ratio test
        good = []
        
        for m,n in matches:
            if m.distance < lower_ratio*n.distance:
                good.append([m])
        #dist = 1 - len(good) / (max(len(img1.distance), len(img2.distance)))
        
        msg2 = ' %d ' % (len(good))
        
        img3 = cv.drawMatchesKnn(imb1,kp1,imb2,kp2,good, None, flags=2)
        
        font = cv.FONT_HERSHEY_SIMPLEX
        #cv.putText(img3,msg1,(25, 500), font, 1,(0,100,0),1,cv.FONT_HERSHEY_TRIPLEX)
        #cv.putText(img3,msg2,(25, 530), font, 1,(0,100,0),1,cv.FONT_HERSHEY_TRIPLEX)
        cv.putText(img3,msg2,(70, 250), font, 8,(0,100,0),8,cv.FONT_HERSHEY_TRIPLEX)
        #print ("kawung Training. %d" %(i))
        #print ("Testing. %d" %(i))
        print ("%s" %(msg2))
    
    #print("%f" % (time.time() - start_time))


#plt.imshow(img3),plt.show()
#cv.imshow('Foto Normal', img3)
#cv.waitKey(0)
#cv.destroyAllWindows()