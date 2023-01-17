#imports here
import cv2 


#code here 
vidoe = cv2.VideoCapture(0)
while True:
    _, okno = vidoe.read()
    cv2.imshow("Security_cam", okno)
    if cv2.waitKey(1) == ord('q'):
        break

vidoe.release()
cv2.destroyAllWindows()