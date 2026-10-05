print("Hola mundo")


nombre: str = "Lorenzo"
apellido: str = "Sabbatini"
print(f"Soy {nombre} y mi appellido es {apellido}")


edad: int = 25
ciudad: str = "Milan"
tengo_carnet: bool = True
print(f"{edad} + {ciudad} + {tengo_carnet}")

print(nombre.upper())
print(apellido.lower())
print(len(nombre))
print(nombre[0])
print(apellido[-1])


persona = {
    "nombre":"Lorenzo",
    "edad":25,
    "ciudad":"Milan", 
    "solterx":False}
print(persona["nombre"])


compra = ["pan", "leche", "huevos"]
compra.append("frutas")
compra.insert(1, "verduras")
compra.pop(-1)
print(compra)


culpable = False
if culpable == True:
    print("Es culpable")
else:
    print("No es culpable")