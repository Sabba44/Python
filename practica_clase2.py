# #Ejercicio 1
# numero = 10
# numeros = [2, 4, 10]

# print(numero * numeros[0])
# print(numero * numeros[1])
# print(numero * numeros[2])

# #Ejercicio 2
# x = range(-10, 0)
# for n in x:
#     print(n)

# #Ejercicio 3
# y = range(150, 351)
# for m in y:
#     if m % 5 == 0 and m % 7 == 0:
#         print(m)

# #Ejercicio 4
# z = range(5, 0, -1)

# for l in z:
#     for s in range(l, 0, -1):
#         print(s, end = " ")
#     print()

# #Ejercicio 5
# nums = [1, 13, 22, 27, 33, 15, 25]
# count = 0

# for n in nums:
#     if n % 3 == 0 or "3" in str(n):
#         count += 1
# print(count)

# #Ejercicio 6
# def conto_atraz(n):
#     r = range(n, -1, -1)
#     for u in r:
#         if u % 4 == 0 or u == 0:
#             print("Pum!")
#         else:
#             print(u)

# conto_atraz(15)

# #Ejercicio 7
# count_mayusculas = 0
# count_minusculas = 0
# count_numeros = 0

# for i in "Ole Python como mola! Me está encantando. De verdad que SÍ":
#     if i.isupper() == True:
#         count_mayusculas += 1
#     elif i.islower() == True:
#         count_minusculas += 1
#     elif i.isdigit() == True:
#         count_numeros += 1
# print(f"Hay {count_mayusculas} mayusculas, {count_minusculas} minusculas y {count_numeros} numeros")


# #Ejercicio 8
# dias_semana = {
#     1: "lunes",
#     2: "martes",
#     3: "miercoles",
#     4: "jueves",
#     5: "viernes",
#     6: "sabado",
#     7: "domingo"
# }

# print(dias_semana[2])

# #Ejercicio 9
# def piramides(n):
#     z = range(n, 0, -1)

#     for l in z:
#         for s in range(l, 0, -1):
#             print(s, end = " ")
#         print()

# piramides(6)

# #Ejercicio 10
# def comparador_numeros(x, y):
#     if x == y:
#         print("Son iguales")
#     elif x > y:
#         print("Primero es mayor")
#     elif x < y:
#         print("Segundo es mayor")

# comparador_numeros(7, 6)

# #Ejercicio 11
# def conta_letra(frase, letra):
#     count_letra = 0
#     for i in frase.lower():
#         if i == letra.lower():
#             count_letra += 1
#     return count_letra

# print(conta_letra("Ciao, come stai?", "C"))

