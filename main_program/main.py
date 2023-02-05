#imports 
import cv2 


#code  
def detect_face(img):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for(x ,y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

def main():
    cap = cv2.VideoCapture(0)


    while True:
        _, img = cap.read()
            
        detect_face(img)

        cv2.imshow("Security_cam", img)
            
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows() 

if __name__ == "__main__":
    main()

