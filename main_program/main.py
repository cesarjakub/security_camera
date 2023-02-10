#imports 
import cv2 
import tkinter as tk
from tkinter import messagebox

#code  
class myGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x250")
        self.root.title("Login")

        self.label = tk.Label(self.root, text="Name: ")
        self.label.pack(padx=20, pady=10)

        self.entry = tk.Entry(self.root)
        self.entry.pack(padx=40, pady=10)

        self.label1 = tk.Label(self.root, text="Password: ")
        self.label1.pack(padx=20, pady=20)

        self.entry1 = tk.Entry(self.root, show="*")
        self.entry1.pack(padx=40, pady=2)

        self.button = tk.Button(self.root, text="login", command=self.check)
        self.button.pack(padx=20, pady=20)

        self.root.mainloop()

    def check(self):
        username = self.entry.get()
        password = self.entry1.get()
        if username == "" and password == "" or username == "" or password == "":
            messagebox.showerror(title="login error", message="vyplnte pole prosim")
        else:
            if username == "admin" and password == "admin":
                self.root.destroy()
            else:
                messagebox.showerror(title="login error", message="heslo nebo jmeno je spatne")



def detect_face(img):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for(x ,y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

def getVideo():
    cap = cv2.VideoCapture(0)
    while True:
        _, img = cap.read()       
        detect_face(img)
        cv2.imshow("Security_cam", img)    
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows() 

def main():
    try:
        if myGui():
            getVideo() 
    except:
        print("Something went wrong")



if __name__ == "__main__":
    main()

