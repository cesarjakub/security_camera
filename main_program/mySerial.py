import serial

ser = serial.Serial(port='COM4', baudrate=9600)

def openAndClose(isopne):
    if isopne: 
        ser.write(b'1')
    else:
        ser.write(b'0')        
        