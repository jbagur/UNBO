#Importamos librerias
import serial
#inicia el programa
print("Sistema iniciado")
#puerto de donde obtendremos la data
arduinodata = serial.Serial('COM3',9600)
#variables globales, contadores
a = 0
b = 0
#Dependiendo el tipo de cadena que reciba el puerto, dependera que mensaje se mostrara en pantalla
#En caso alguno de los dos contadores pase de 10 este lanzara un mensaje de alerta
#imprimira en pantalla
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
