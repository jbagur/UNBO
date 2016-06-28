import serial
from Tkinter import *
from time import sleep
print("Sistema iniciado")
arduinodata = serial.Serial('COM3',9600)

def update():
    a = 0
    b = 0
    while (1==1):
        myData.set(arduinodata.readline().strip())

        root.update()
        sleep(1)

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

root.after(2,update)
root.mainloop()