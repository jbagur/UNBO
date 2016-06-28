#importamos librerias
import serial
from Tkinter import *
from time import sleep
#inicia el programa
print("Sistema iniciado")
#puerto de onde obtendremos la data
arduinodata = serial.Serial('COM3',9600)
#funcion que actualiza el form con la informacion mas reciente del puerto
#toma la data del puerto y esta la añade a una variable
def update():
    a = 0
    b = 0
    while (1==1):
        myData.set(arduinodata.readline().strip())
        root.update()
        sleep(1)
#creacion de nuestra aplicacion grafica
root=Tk()
root.title("UNBO")
root.geometry('350x150+200+200')
myData = StringVar()

r = Label(root, text="UNBO", fg="blue", font=("Helvetica", 20))
r.pack()

y = Label(root, text="Sistema iniciado", fg="green", font=("Helvetica", 12))
y.pack()

w = Label(root, textvariable = myData)
w.pack()
#despues de 1 segundo se actualizara nuestra aplicacion
root.after(1,update)
root.mainloop()
