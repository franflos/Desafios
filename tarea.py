numeros = input("ingrese 4 numeros: ").split()

suma = 0
pares = 0

for i in numeros:  #el codigo se ejecuta por cada valor.
    numero = int(i)     # por cada numero en numeros lo hacemos entero con el int.
    if numero % 2 == 0:
        suma += numero
        pares += 1
 
print ("cantidad de pares:", pares)
print ("cuantos impares", 4 - pares)
print ("la suma de los pares es:", suma)
