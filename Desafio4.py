#4- Tiempo de viaje. Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él
#tiene la duración en minutos de cada uno de los tramos del viaje.
#Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y
#entregue como resultado el tiempo total de viaje en formato horas:minutos.
#El programa deja de pedir tiempos de viaje cuando se ingresa un 0.

TiempodeViaje = [int(input("ingrese el tiempo de viaje: "))]

while TiempodeViaje[-1] > 0:
    time = int(input("ingrese otro tiempo de viaje: "))
    TiempodeViaje.append (time)
    if TiempodeViaje == 0:
        break

sumadeValores = sum(TiempodeViaje)

print ("tu viaje duro: " + str(int(sumadeValores / 60)) + ":" + str((sumadeValores%60)))
