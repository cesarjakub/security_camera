#imports 
import cv2 
import os
import numpy as np
import tkinter as tk
from tkinter import messagebox
from mySerial import openAndClose

#code
#login window class
class myGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x250")
        self.root.title("Login")

        self.label1 = tk.Label(self.root, text="Password: ")
        self.label1.pack(padx=20, pady=20)

        self.entry1 = tk.Entry(self.root, show="*")
        self.entry1.pack(padx=40, pady=2)

        self.button = tk.Button(self.root, text="login", command=self.check)
        self.button.pack(padx=20, pady=20)

        self.root.mainloop()

    def check(self):
        password = self.entry1.get()
        if password == "":
            messagebox.showerror(title="login error", message="vyplnte pole prosim")
        else:
            if password == "admin":
                self.root.destroy()
            else:
                messagebox.showerror(title="login error", message="heslo nebo jmeno je spatne")




#face detectiona and recognition class
class SecCam:
    def __init__(self):
        self.getVideo()

    def load_training_data(self):
        face_data = []
        labels = []
        for i, file_name in enumerate(os.listdir("main_program\\faces")):
            img_path = os.path.join("main_program\\faces", file_name)
            face_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            face_img = cv2.resize(face_img, (100, 100))
            face_data.append(face_img)
            labels.append(i)
        return np.array(face_data), np.array(labels)

    def getVideo(self):
        face_data, labels = self.load_training_data()
        face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        face_recognizer.train(face_data, labels)

        # inicializace videokamery
        cap = cv2.VideoCapture(0)
        rozpoznano = False

        while True:
            _, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
            
            if len(faces) > 0:
                for (x, y, w, h) in faces:
                    face_roi = gray[y:y+h, x:x+w]

                    face_roi = cv2.resize(face_roi, (100, 100))
                    label, _ = face_recognizer.predict(face_roi)

                    if label == 1:
                        rozpoznano = True
                    else:
                        rozpoznano = False
            else:
                rozpoznano = False

            openAndClose(rozpoznano)
            
            cv2.imshow('Face detection', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


def main():
    login = myGui()
    securityCameras = SecCam()
    try:
        if login:
             securityCameras
    except:
        print("Something went wrong")



if __name__ == "__main__":
    main()