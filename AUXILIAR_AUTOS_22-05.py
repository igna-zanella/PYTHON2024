
autos = {"HLS555":{"km":50000, "precio":13000000,"tipo":"alquiler"},"AB976CC":{"km":20000, "precio":19000000,"tipo":"venta"},"AD571RA":{"km":10000, "precio":42000000,"tipo":"venta"},"GSM788":{"km":20000, "precio":19000000,"tipo":"venta"}}

# print(autos)
# del(autos["HLS555"])
# print("--------------------------------------")
# print(autos)

# patente = input("Patente: ")
# km = float(input("Kilómetros: "))
# precio = float(input("Precio: "))
# tipo = input("Tipo: ")

# autos[patente] = {"km":km, "precio":precio, "tipo":tipo}

# print(autos)

# while True:
#     opcsub = input("Ingrese opción: ").upper
#     if opcsub == "A":
#         print("Ingrese los datos del nuevo vehículo: \n")
#         patente = input("Patente: ")
#         km = float(input("Kilómetros: "))
#         precio = float(input("Precio: "))
#         tipo = input("Tipo: ")

#         autos[patente] = {"km":km, "precio":precio, "tipo":tipo}
#         print(autos)
#         break

people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'}, 2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}

print(people[1]['Sex'])


for p_id, p_info in people.items():
    if people[p_id]['Sex'] == 'Male':
        print("\nPerson ID:", p_id)

    
        for key in p_info:
            print(key + ':', p_info[key])
