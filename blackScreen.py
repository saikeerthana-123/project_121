# Importing libraries
import cv2  
import numpy as np  

# Capturin video
video = cv2.VideoCapture(0) 
image = cv2.imread("me.jpg") 
  
while True: 
  # Creating frame
    ret, frame = video.read() 
    print(frame)
    frame = cv2.resize(frame, (640, 480)) 
    image = cv2.resize(image, (640, 480)) 
    
  #Generating mask to detect red colour
    u_black = np.array([104, 153, 70]) 
    l_black = np.array([30, 30, 0]) 
    
  # Creating mask for black background
    mask = cv2.inRange(frame, l_black, u_black) 
    res = cv2.bitwise_and(frame, frame, mask = mask) 
  
    f = frame - res 
    f = np.where(f == 0, image, f)  
    
  # Creating final output
    cv2.imshow("Magic", frame) 
    cv2.imshow("mask", f) 
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
  
video.release() 
cv2.destroyAllWindows() 
