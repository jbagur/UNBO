from Tkinter import *
import serial
print("Sistema iniciado")
arduinodata = serial.Serial('COM3',9600)
a = 0
b = 0
while (1==1):
    myData = (arduinodata.readline().strip())
    if myData == 'Received: id=001$status=1':
        myData = "El boton 1, esta encendido"
        a = a+1
        b = 0
    if myData == 'Received: id=001$status=0':
        myData = "El boton 1, esta apagado"
        a = 0
        b = b + 1
    if a >= 10:
        print("ALERTA!")
    if b >= 10:
        print("ALERTA!")
    print(myData.decode('utf-8'))
