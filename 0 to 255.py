import cv2
import numpy as np 
def nothing(x):
    print (x)

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow("colour")
cv2.createTrackbar("b","colour",0,400,nothing)
cv2.createTrackbar("g","colour",0,400,nothing)
cv2.createTrackbar("r","colour",0,400,nothing)

while(1):
    cv2.imshow("colour",img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    b = cv2.getTrackbarPos("b","colour")
    g = cv2.getTrackbarPos("g","colour")
    r = cv2.getTrackbarPos("r","colour")
    img[:] = [b,g,r]
cv2.destroyAllWindows()
    