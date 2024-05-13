#2- Escriba un programa que pregunte al usuario la hora actual t del reloj y un número
#entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

t = int(input("Ingrese la Hora Actual: "))
h = int(input("Ingrese la Cantidad de Horas: "))


print ("en: " + str(h) + " Horas, seran las: " + str((t+h)%24) )