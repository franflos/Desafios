#3- Escribir un programa que pida al usuario un número entero y muestre por pantalla si
#es un número primo o no.

Numero = int(input("ingrese un numero entero: "))

def Primos (Numeros):
    for n in range(2,Numeros):           
        if Numeros%n == 0:
            return False
    return True

Resultado = Primos (Numero) 
if Resultado:
    print ("el numero es primo")
else:
    print("El numero, no es primo")
