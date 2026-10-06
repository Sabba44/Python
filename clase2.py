# #Set
# numeros_set= {1, 2, 3, 3, 3, 4, 4} 
# # print(numeros_set)
# # print(len(numeros_set))

# #Diccionario
# persona= {
#     "nombre": "Aurelio García",
#     "hobbies": [
#         "Escalada",
#         "Lectura",
#         "Cocina"
#     ],
#     "contacto": {
#         "email": "aurelio@gmail.com",
#         "telefono": "123456789"
#     }
# }

# # print(persona["hobbies"][1])
# # print(persona["contacto"]["telefono"])

# #Practica 1
# contrasena = "mimama"
# longitud_minima = 8
# longitud_maxima = 20
# # print(len(contrasena))

# # if len(contrasena) < longitud_minima:
# #     print("Muy corta")
# # elif len(contrasena) > longitud_maxima:
# #     print("Demasiado larga")
# # else:
# #     print("Valida")

# #Bucle
# personas = ["Io", "Tu", "Egli"]
# for i in personas:
#     print(i)

#Practica 2
# colores = ["rojo", "verde", "azul", "amarillo"]
# for colore in colores:
#     print(colore)

#Practica 3
# numeros = [1,2,3,4,5,6,7,8,9,10,11,12]
# contador = 6

# while contador < 11:
#     print(f"{numeros[contador]}")
#     contador += 1

#     numeros = [1,2,3,4,5]
# contador = 4


# def saludar (nombre):
#     return f"Hola, {nombre}"

# print(saludar("Lorenzo"))


# def cuentaCaracteres(palabra):
#     if type(palabra) == str:
#         return len(palabra)
#     else:
#         return "Debe ser un string"

# print(cuentaCaracteres(1))


# def contar_letra(texto, letra):
#     count = 0
#     for t in texto.lower():
#         if t == letra.lower():
#             count +=1
#     return count

# print(contar_letra("Arroz", "r"))


#Lambda
# primeraLetra = lambda palabra: palabra[0]
# print(primeraLetra("fghjkol"))


def obtener_nombre_completo(nombre, apellido):
    return nombre + " " + apellido
def main():
    usuarios = [
        {"nombre": "Sofía"},
        {"nombre": "Luis", "apellido": "Martínez"},
    ]
    
    for usuario in usuarios:
        completo = obtener_nombre_completo(usuario["nombre"], usuario["apellido"])
        print(completo)
main()
