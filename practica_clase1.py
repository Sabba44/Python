#Ejercicio 1
nombre_calle = "Plaza del Music Lopez Chavarri"
numero_calle = "7"
ciudad = "Valencia"
codigo_postal = "46001"
direcion = f"{nombre_calle}, {numero_calle}, {ciudad}, {codigo_postal}"
print(direcion)
print(f"Esta cadena tiene {len(direcion)} caracteres!")

#Ejercicio 2
#3 -> no se puede llamar True
#4 -> no puede tener espacio
#5 -> no se puede llamar import
#6 -> no puede empezar por un numero

#Ejercicio 3
x : int = 10
y : float = 4.44
print(type(x))
print(type(y))
suma = x + y
print(type(suma))
del x
del y

#Ejercicio 4.1
a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print((a + b) * 2 -5)
print(a // b)
print(a** 2)
print(b** 2)

#Ejercicio 4.2
print(a == b)
print(a != b)
print(a > b)
print(b <= a)
print(a+5 >= b*2)

#Ejercicio 4.3
print(a>5 and b<5)
print(a<5 and b<5)
print(a != b)
print(a>5 and b!=10)