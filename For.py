#numeros = list(map(int, input("Enter multiple values: ").split()))
#print (len(numeros))

#if len (numeros) > 4:
  #  raise Exception () 

numero1 = int(input("ingrese un numero 1: "))
numero2 = int(input("ingrese un numero 2: "))
numero3 = int(input("ingrese un numero 3: "))
numero4 = int(input("ingrese un numero 4: "))
suma = 0
pares = 0

if numero1 % 2 == 0:
    suma += numero1
    pares += 1
if numero2 % 2 == 0:
    suma += numero2
    pares += 1

if numero3 % 2 == 0:
    suma += numero3
    pares += 1

if numero4 % 2 == 0:
    suma += numero4
    pares += 1


print ("cantidad de pares:", pares)
print ("cuantos impares", 4 - pares)
print ("la suma de los pares es:", suma)
