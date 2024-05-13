#ngresar las edades y el sexo de 15 personas y determinar cuántas son
#mujeres, cuántos varones, cuántos mayores de edad y cuántos
#menores de edad.
Edades = []
Sexo = []

for x in range(4):
    edad = int(input("ingrese su edad: ", ))
    sexo = input("ingrese su sexo (M/F) ")
    Edades.append(edad)
    Sexo.append(sexo)

mujeres = Sexo.count("F")
varones = Sexo.count("M") #asi se cuetna lo que esta dentro de la lista Sexo, teniendo en cuenta la cadena M o F


mayoresDeEdad = sum(1 for edad in Edades if edad >= 18)
menoresDeEdad = 15 - mayoresDeEdad



print ("la cantidad de mujeres es: ", mujeres)
print (" la cantidad de varones es: ", varones)
print ("cantidad de mayores de edad:", mayoresDeEdad)
print ("cantidad de menores de edad:", menoresDeEdad)