#2. Leer 10 números y obtener la cantidad de mayores y la cantidad de
#menores a 100, cuál es el número máximo y cuál es el número mínimo.

Numeros = input("ingrese 10 numeros:").split()

mayores = 0
menores = 0 

for Contador in Numeros:
    numero = int(Contador)
    if numero < 100:
        menores += 1

ValorMaximo = max(Numeros)
ValorMinimo = min(Numeros)
    
print ("cantidad de menores: ", menores)
print ("cantidad de mayores: ", 10 - menores)
print ( "el valor maximo: ", ValorMaximo)
print ( "el valor minimo: ", ValorMinimo)