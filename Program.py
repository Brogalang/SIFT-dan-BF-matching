#INI PROGRAM YANG LASTEST

from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog 
import cv2
import time

def select_image():
    # grab a reference to the image panels
    global panelA, panelB
    # open a file chooser dialog and allow the user to select an input
    # image
    path = filedialog.askopenfilename(initialdir="F:\Percobaan\Data Training")
    path1 = filedialog.askopenfilename(initialdir="F:\Percobaan\Data Testing")
    #sift = cv2.xfeatures2d.SIFT_create()
    # ensure a file path was selected
    if len(path) > 0:
        # load the image from disk, convert it to grayscale, and detect
        # keypoint in it
        #Panel A
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        (thresh, binary) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        sift = cv2.xfeatures2d.SIFT_create()
        kp, des = sift.detectAndCompute(binary, None)
        edged = cv2.drawKeypoints(binary,kp,None)
        
        #Panel B
        image1 = cv2.imread(path1)
        gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        (thresh, binary1) = cv2.threshold(gray1, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        kp1, des1 = sift.detectAndCompute(binary1, None)
        edged1 = cv2.drawKeypoints(binary1,kp1,None)
        
        start_time = time.time()
        #brute force matching
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des,des1, k=2)
        good = []
        for m,n in matches:
            if m.distance < 0.8*n.distance:
                good.append([m])
                
        msg = ' %d ' % (len(good))

        img3 = cv2.drawMatchesKnn(binary,kp,binary1,kp1,good, None, flags=2)

        font = cv2.FONT_HERSHEY_SIMPLEX

        cv2.putText(img3,msg,(70, 250), font, 8,(0,100,0),8,cv2.FONT_HERSHEY_TRIPLEX)           

        # OpenCV represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        #image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
        # convert the images to PIL format...
        binary1 = Image.fromarray(binary1)
        img3 = Image.fromarray(img3)
        # ...and then to ImageTk format
        binary1 = ImageTk.PhotoImage(binary1)
        img3 = ImageTk.PhotoImage(img3)

        # if the panels are None, initialize them
        if panelA is None or panelB is None:
            # the first panel will store our original image
            panelA = Label(image=binary1)
            panelA.image = binary1
            panelA.pack(side="left", padx=10, pady=10)
            # while the second panel will store the edge map
            panelB = Label(image=img3)
            panelB.image = img3
            panelB.pack(side="right", padx=10, pady=10)
            # otherwise, update the image panels
        else:
            # update the pannels
            panelA.configure(image=binary1)
            panelB.configure(image=img3)
            panelA.image = binary1
            panelB.image = img3
            
            print("--- %s seconds ---" % (time.time() - start_time))
            
def select_kawung():
    # grab a reference to the image panels
    global panelA, panelB
    # open a file chooser dialog and allow the user to select an input
    # image
    path = filedialog.askopenfilename(initialdir="F:\Percobaan\Data Testing")
    #sift = cv2.xfeatures2d.SIFT_create()
    # ensure a file path was selected
    
    if len(path) > 0:
            # load the image from disk, convert it to grayscale, and detect
            # keypoint in it
            #Panel A
        top = tk.Toplevel()
        
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        (thresh, binary) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        sift = cv2.xfeatures2d.SIFT_create()
        kp, des = sift.detectAndCompute(binary, None)
            #edged = cv2.drawKeypoints(binary,kp,None) #Buat tampilin gambar SIFT
        for i in range(1, 6):
            #Panel B
            image1 = cv2.imread('F:/Percobaan/Data Training/kawung %d.jpg' % (i),0)
            (thresh, binary1) = cv2.threshold(image1, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            kp1, des1 = sift.detectAndCompute(binary1, None)
            #edged1 = cv2.drawKeypoints(binary1,kp1,None) #Buat tampilin gambar SIFT
            
            #start_time = time.time()
            
            #brute force matching
            bf = cv2.BFMatcher()
            matches = bf.knnMatch(des,des1, k=2)
            good = []
            for m,n in matches:
                if m.distance < 0.8*n.distance:
                    good.append([m])
                    
            msg = ' %d ' % (len(good))
            
    
            img3 = cv2.drawMatchesKnn(binary,kp,binary1,kp1,good, None, flags=2)
    
            font = cv2.FONT_HERSHEY_SIMPLEX
    
            cv2.putText(img3,msg,(70, 250), font, 8,(0,100,0),8,cv2.FONT_HERSHEY_TRIPLEX)           
            #print ("%s" %(msg))
            
        
            label = Label(top, text= "%s" %(msg))
            label.pack()
        
            # OpenCV represents images in BGR order; however PIL represents
            # images in RGB order, so we need to swap the channels
            #image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
            # convert the images to PIL format...
        binary = Image.fromarray(binary)
        img3 = Image.fromarray(img3)
        # ...and then to ImageTk format
        binary = ImageTk.PhotoImage(binary)
        img3 = ImageTk.PhotoImage(img3)
    
        # if the panels are None, initialize them
        if panelA is None or panelB is None:
            # the first panel will store our original image
            panelA = Label(image=binary)
            panelA.image = binary
            panelA.pack(side="left", padx=10, pady=10)
            panelB = None
            panelB.pack(side="left", padx=10, pady=10)
        # otherwise, update the image panels
        else:
            # update the pannels
            panelA.configure(image=binary)
            panelA.image = binary
            panelB = None 
            panelB.pack(side="left", padx=10, pady=10)
            #print ("Testing. %d" %(i))
            #print("--- %s seconds ---" % (time.time() - start_time))
            
# initialize the window toolkit along with the two image panels
root = Tk()

panelA = None
panelB = None
# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
#btn = Button(root, text="Pilih motif Kawung", command=select_kawung)
#btn.pack(side="bottom", fill="both",  padx="10", pady="10")
btn = Button(root, text="Pilih gambar", command=select_image)
btn.pack(side="bottom", fill="both",  padx="10", pady="10")

# kick off the GUI
root.mainloop()