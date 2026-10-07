#Input
# nombre = input("Como te llamas?")
# print(f"Hola, yo soy {nombre}")

# numero = int(input("Perir un numero"))  #Convertire str in int


#Practica 2
lista_edades = [15,22,17,30,65,45,70,19]

for edad in lista_edades:
    if edad > 18 and edad < 65:
        print(f"{edad} es mayor")
        continue
    elif edad >= 65:
        print(f"{edad} demasiado viejo")
        break
