#Input
nombre = input("Como te llamas?")
print(f"Hola, yo soy {nombre}")

numero = int(input("Perir un numero"))  #Convertire str in int


#Practica 1
lista_edades = [15,22,17,30,65,45,70,19]

 for edad in lista_edades:
     if edad > 18 and edad < 65:
         print(f"{edad} es mayor")
         continue
     elif edad >= 65:
         print(f"{edad} demasiado viejo")
         break

#Try, Expect and Finally
 try:
     resultado = 10/0
 except:
     print("Errore")

 try:
     resultado = 10/0
 except ZeroDivisionError:
     print("no se puede dividir")
 finally:
     print("finito")

#Practica 2
contador_intentos = 0

while contador_intentos < 5:
    numero = input("Elige un numero: ")
    try:
        entero = int(numero)
        print("El numero es valido")
        break
    except:
        print(("Tienes que poner un numero"))
        contador_intentos += 1



import saludos

print(saludos.saludar("Lorenzo"))
print(saludos.despedir("Juan"))
