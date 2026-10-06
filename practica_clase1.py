#Ejercicio 1
nombre_calle = "Plaza del Music Lopez Chavarri"
numero_calle = "7"
ciudad = "Valencia"
codigo_postal = "46001"
direcion = f"{nombre_calle}, {numero_calle}, {ciudad}, {codigo_postal}"
# print(direcion)
# print(f"Esta cadena tiene {len(direcion)} caracteres!")

#Ejercicio 2
#3 -> no se puede llamar True
#4 -> no puede tener espacio
#5 -> no se puede llamar import
#6 -> no puede empezar por un numero

#Ejercicio 3
x : int = 10
y : float = 4.44
# print(type(x))
# print(type(y))
suma = x + y
# print(type(suma))
del x
del y

#Ejercicio 4.1
a = 10
b = 3
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# print((a + b) * 2 -5)
# print(a // b)
# print(a** 2)
# print(b** 2)

# #Ejercicio 4.2
# print(a == b)
# print(a != b)
# print(a > b)
# print(b <= a)
# print(a+5 >= b*2)

# #Ejercicio 4.3
# print(a>5 and b<5)
# print(a<5 and b<5)
# print(a != b)
# print(a>5 and b!=10)

#Ejercicio 5
frase = "A quien madruga, dios le ayuda"
# print(frase)
# print(frase.upper())
# print(frase.lower())

#Ejercicio 6
puntuacion : int = 100
nombre_equipo : str = "Inter futbol"
promedio_tiempo : float = 3.5
es_habil : bool = True
lista_compras = ["pollo", "patatas", "pasta", "verduras", "ternera"]
tupla_mascota1 = ("Dora", 3, "Gato")
tupla_mascota2 = ("Leo", 1, "Perro")
dict_contactos = {
    "amigos" : ["Juan", "Manuel"],
    "telefonos" : ["3367448597", "3456745783"],
    "emails" : ["juan@gmail.com", "manuel@gmail.com"]
}

lista_actividades = []
lista_actividades.append(puntuacion)
lista_actividades.append(nombre_equipo)
lista_actividades.append(promedio_tiempo)
lista_actividades.append(es_habil)
lista_actividades.append(lista_compras)
lista_actividades.append(tupla_mascota1)
lista_actividades.append(tupla_mascota2)
lista_actividades.append(dict_contactos)
# print(lista_actividades)

#Ejerciccio 7
peliculas = ["Inception", "The Matrix", "Interstellar", "Gladiator"]
# a) Imprime todas las películas.
#print(peliculas)

# b) Añade "El Padrino" al final.
peliculas.append("El Padrino")
#print(peliculas)

# c) Inserta "Memento" en la posición 2.
peliculas.insert(3, "Memento")
#print(peliculas)

# d) Elimina "Gladiator".
peliculas.remove("Gladiator")
#print(peliculas)

# e) Elimina y muestra la última película. Investiga si puedes hacer lo mismo con cualquier elemento de la lista, o sólo con el último. Contéstalo en un comentario.
peliculas.pop(-1)
#print(peliculas[-1])

# f) Ordena la lista alfabéticamente.
peliculas.sort()
#print(peliculas)

# g) Vacía la lista y muestra que está vacía.
peliculas.clear()
#print(peliculas)

#Ejercicio 8
nota = 75
if nota >= 90:
    print("Excelente")
elif nota >= 70 and nota <= 89:
    print("Bueno")
elif nota >= 50 and nota <= 69:
    print("Suficiente")
else:
    print("Insuficiente")