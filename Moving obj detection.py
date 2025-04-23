import cv2 # opencv lib is used for image processing tasks
import time # module handles timing functions , here it is used to add delays
import imutils # This lib has convience functions for image processing tasks like resizing
# camera initialization
cam=cv2.VideoCapture(0) # intialize the camera
time.sleep(3) # wait for camera to intialize for 3 seconds
# script captures the first frame of video and uses it as refrence firstframe
firstFrame=None #This intialize the first frame of the video and can be refrenced in future
area=500 #A threshold value defining the minimum area (in pixels) for an object to be considered significant during motion detection.
while True: #creates the infinite loop for processing framers in the video
    # _ indicates that frame was successfully captured  and cam.read() single frame
    _, img=cam.read()
    text="Normal" #Sets the initial status of the frame to "Normal". This can be updated later based on detected motion.
    img=imutils.resize(img,width=500) #resizing the image while maintaining the aspect ratio
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # BGR image to gray image
    gaussianImg=cv2.GaussianBlur(grayImg,(21,21),0) # reduces the noise of image make the image blurr easy for detection
    if firstFrame is None: # if first frame is none it sets the current frame as gaussian image for refrence
        firstFrame = gaussianImg
        continue # kips the rest of the loop for this iteration and moves to the next frame. This ensures the first frame is only captured once.
    imgDiff = cv2.absdiff(firstFrame, gaussianImg) # this applies the absolute difference between  firstframe and gaussian image
    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1] # threshing converts the absolute differenced image to binary image
    # using threshold value of 25 
    #Pixels with values greater than 25 are set to 255 (white), representing significant changes.
    #Pixels with values 25 or below are set to 0 (black), ignoring minor changes.
    
    threshImg = cv2.dilate(threshImg, None, iterations=2)
    # dilate :Expands the white areas in the binary image to fill gaps and emphasize regions of interest.
    # iterations=2: Specifies that the dilation process will be repeated twice for a more pronounced effect.
    cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.findContours: Identifies the boundaries of white regions (contours) in the binary image:
    #cv2.RETR_EXTERNAL: Retrieves only the outermost contours.
    #cv2.CHAIN_APPROX_SIMPLE: Compresses horizontal, vertical, and diagonal segments to store only essential points.
    #imutils.grab_contours: Simplifies contour retrieval across OpenCV versions.

    cnts = imutils.grab_contours(cnts)
    count = 0
    for c in cnts:
        if cv2.contourArea(c)<area:
            continue
        #cv2.contourArea(c): Calculates the area of the contour.
        #Skips contours smaller than the defined area (500 pixels) to ignore insignificant motion or noise.

        
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x,y), (x+w,y+h), (0, 255, 0),  2)
        text = "Moving Object detected"
        count = count+1
        text2 = f"No of Objects : {count}"
        print(text)
        print(text2)
    cv2.putText(img, text, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    #cv2.putText: Overlays the status (text) on the top-left corner of the frame (img):
    #(10, 20): Coordinates for the text.
    #Font and Size: cv2.FONT_HERSHEY_SIMPLEX and 0.5.
    #Color: Red ((0, 0, 255)).
    #Thickness: 2.
    cv2.imshow("camerafeed",img)
    #opens a window named "camerafeed" to display the current frame (img) with the detected objects and status overlayed.

    key = cv2.waitKey(3)
    if key==ord("t"):
        break
cam.release()
cv2.destroyAllWindows()
