
usuarios = {"fede":{"tipo":'s',"clave":'1234'},
            "juan":{"tipo":'v',"clave":'5678'},
            "marian":{"tipo":'v',"clave":'8765'},
            "rafa":{"tipo":'v',"clave":'abcd'},
            "pau":{"tipo":'t',"clave":'4321'},
            "pepe":{"tipo":'t',"clave":'1111'}
}

empleados = {
            "11223344":{"nombre":'Juan', "apellido":'Cardozo',"tipo":'Ventas',"sueldo":500000},
            "98765432":{"nombre":'Mariana', "apellido":'Cruz',"tipo":'Ventas', "sueldo":500000},
            "87654321":{"nombre":'Paula', "apellido":'Vieytes',"tipo":'Ventas', "sueldo":500000},
            "33112244":{"nombre":'José', "apellido":'Barrios',"tipo":'Taller', "sueldo":500000},
            "12345678":{"nombre":'Rafael', "apellido":'Walsh',"tipo":'Taller',"sueldo":450000}
}

autos={
    "ABC123":{"km":5000,"precio":90000,"tipo":'v',"disponibilidad":'s'},
    "JKL123":{"km":10000,"precio":100000,"tipo":'a',"disponibilidad":'n'},
    "AD123JK":{"km":0,"precio":190000,"tipo":'v',"disponibilidad":'s'}
}
operaciones={"1":{"cliente":'12345678',"patente":'ABC123',"usuario":'fede'},
            "2":{"cliente":'12345678',"patente":'JKL123',"usuario":'juan'},   
            "3":{"cliente":'1234',"patente":'JKL123',"usuario":'juan'}
}
clientes={"12345678":{"nombre":'hector',"clas":1,"tel":1234},
        "1234":{"nombre":'lopez',"clas":1,"tel":111235}
}

# for o in operaciones:
#     if autos[operaciones[o]["patente"]]["tipo"]=="a":
#         print(operaciones[o],clientes[operaciones[o]["cliente"]]["tel"],clientes[operaciones[o]["cliente"]]["nombre"])
    

i=0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)

while True:
    usuario = input("Ingrese usuario: ")
    if usuario in usuarios:
        clave = input("Ingrese contraseña: ")
        if clave==usuarios[usuario]["clave"]:
            print("Bienvenido",usuario)
            if usuarios[usuario]["tipo"]=="s":
                
# ------------------------------ MENÚ PRINCIPAL SUPERVISOR ------------------------------
                while True:                
                    print("""
1)	Flota de rodados  
2)	Empleados ABM 
3)	Promociones y Precios
4)	Compra de repuestos (Autorización y pago)
5)	Acceso a informes mensuales
0)	Cerrar sesión
            """) 
                    opc=input()
                    if opc=="1":
                        print("""
A)  Ingreso (Alta: Datos y Finalidad) 
B)  Baja (Motivo)
C)  Modificación (Precio / KM / Seguro / VTV / Repuestos / Accesorios)
D)  Disponibilidad de alquiler (SI / NO)
E)  Disponibilidad de venta (SI / NO)
F)  Listado de rodados 
0)  Volver al Menú principal
""")
                        
                        opc2=input().lower()
                        if opc2=="a":
                            print("ALTA DE VEHÍCULOS\n")
                            patente=input("Ingrese patente: ").upper()
                            km=int(input("Ingrese kilometraje: "))
                            precio=int(input("Ingrese el precio: "))
                            tipo=input("Ingrese tipo: ")
                            dis=input("¿Está disponible? ")
                            autos[patente]={"km":km,"precio":precio,"tipo":tipo,"disponibilidad":dis}
                            
                        elif opc2=="b":
                            print("BAJA DE VEHÍCULOS\n")
                            print("Nuestra Flota:")
                            for p in autos:
                                print(f"""
PATENTE: {p}
Kilometraje: {autos[p]["km"]}
Precio: {autos[p]["precio"]}
Tipo: {autos[p]["tipo"]}
Disponibilidad: {autos[p]["disponibilidad"]}
""")
                            while True:
                                patente=input("Ingrese patente: ").upper()
                                if patente in autos:
                                    del(autos[patente])
                                    print("\nVehículo eliminado correctamente")
                                    input("ENTER para continuar...")
                                    break
                                else:
                                    print("Patente incorrecta. Intente nuevamente.\n")
                            
                        elif opc2=="c":
                            print("MODIFICACIONES DE VEHÍCULOS\n")
                            print("Nuestra Flota:")
                            for p in autos:
                                print(f"""
PATENTE: {p}
Kilometraje: {autos[p]["km"]}
Precio: {autos[p]["precio"]}
Tipo: {autos[p]["tipo"]}
Disponibilidad: {autos[p]["disponibilidad"]}
""")
                            x = True
                            while x:
                                patente=input("Ingrese patente: ").upper()
                                if patente in autos:
                                    while True:
                                        print("""
1)	Kilometraje 
2)	Precio
3)	Tipo
4)	Disponibilidad
""")
                                        opc3 = input()
                                        if opc3 == "1":
                                            km=int(input("Nuevo kilometraje: "))
                                            autos[patente]={"km":km}
                                            print("Valor modificado ✔")
                                            x = False
                                            break
                                        elif opc3 == "2":
                                            precio=int(input("Nuevo precio: "))
                                            autos[patente]={"precio":precio}
                                            print("Valor modificado ✔")
                                        elif opc3 == "3":
                                            tipo=input("Nuevo tipo: ")
                                            autos[patente]={"tipo":tipo}
                                            print("Valor modificado ✔")
                                        elif opc3 == "4":
                                            dis=input("Disponiblidad: ")
                                            autos[patente]={"tipo":tipo}
                                            print("Valor modificado ✔")
                                        else:
                                            print("\nOpción incorrecta. Intente nuevamente.")

                                            input("ENTER para continuar...") 
                                        # autos[patente]={"km":km,"precio":precio,"tipo":tipo,"disponibilidad":dis}
                                        
                                else:
                                    print("Patente inexistente")
                                    
                        elif opc2=="d":
                            for p in autos:
                                if autos[p]["tipo"]=="a" and autos[p]["disponibilidad"]=="s":
                                    print(autos[p])
                        elif opc2=="e":
                            for p in autos:
                                if autos[p]["tipo"]=="v" and autos[p]["disponibilidad"]=="s":
                                    print(autos[p])
                        elif opc2=="f":
                            print("Nuestra Flota:")
                            for p in autos:
                                print(f"""
PATENTE: {p}
Kilometraje: {autos[p]["km"]}
Precio: {autos[p]["precio"]}
Tipo: {autos[p]["tipo"]}
Disponibilidad: {autos[p]["disponibilidad"]}
""")
                        elif opc2=="0":
                            print("Volviendo al menú principal....")
                        else:
                            print("opcion incorrecta")
                        
                    elif opc=="2":
                        while True:
                            print("""
    A)  Ingreso (Alta)
    B)  Baja (Motivo)
    C)  Modificación (Categoría / Sueldo / Comisión)
    0)  Volver al Menú principal
    """)
                            opc2 = input()
                            if opc2 == "a":
                                print("ALTA DE EMPLEADO/A\n")
                                print("Ingrese los datos:")
                                dniCorrecto = True
                                while dniCorrecto:
                                    dni = input("DNI: ")
                                    if len(dni) == 8:
                                        if dni.isnumeric():
                                            dniCorrecto = False
                                        else:
                                            print("Debe ser numérico")
                                    else:
                                        print("Debe ser contener 8 dígitos")
                                nombre = input("Nombre: ").capitalize()
                                apellido = input("Apellido: ").capitalize()
                                tipo = input("Sector (Ventas / Taller): ").capitalize()
                                sueldo = int(input("Sueldo: "))
                                
                                empleados[dni] = {"nombre":nombre, "apellido":apellido,"tipo":tipo,"sueldo":sueldo}
                                for e in empleados:
                                    print("Empleado/a:",empleados[e]["nombre"],empleados[e]["apellido"])
                                    print("\nDNI:",e)
                                    print("Sector:",empleados[e]["tipo"])                            
                                    print("Sueldo:",empleados[e]["sueldo"])  
                                                            
                            elif opc2=="b":
                                print("BAJA DE EMPLEADOS")
                                for e in empleados:
                                    print("DNI:",e,"\n")
                                    print("Empleado:",empleados[e]["nombre"],empleados[e]["apellido"])
                                    print("Sector:",empleados[e]["tipo"])
                                while True:
                                    dni = input("Ingrese DNI: ")
                                    if dni in empleados:
                                        del empleados[dni]
                                        print("Baja exitosa ✅")
                                        break
                                    else:
                                        print("DNI no válido. Intente nuevamente.")
                                        
                            elif opc2=="c":
                                print("MODIFICACIONES")
                                for e in empleados:
                                    print("DNI:",e,"\n")
                                    print("Empleado:",empleados[e]["nombre"],empleados[e]["apellido"])
                                    print("Sector:",empleados[e]["tipo"])
                                    print("Sueldo:",empleados[e]["sueldo"])
                                while True:
                                    dni = input("Buscar DNI: ")
                                    print("Ingrese los datos a modificar\n")
                                    if dni in empleados:
                                        nombre=input("Nombre: ").capitalize()
                                        apellido=input("Apellido: ").capitalize()
                                        cargo=input("Sector (Ventas / Taller): ").capitalize()
                                        sueldo=input("Sueldo: ")
                                        empleados[dni]={"nombre":nombre,"apellido":apellido,"cargo":cargo,"sueldo":sueldo}
                                        break
                                    else:
                                        print("DNI no válido. Intente nuevamente.")                    

                            elif opc2 == "0":
                                print("Volviendo al menú principal....")
                                break
                            else:
                                print("opcion incorrecta")
                                
                    elif opc=="3":
                        print("""
A.Ingreso y modificación de precios
B.Descuentos bancarios 
C.Volver al Menú principal
""")
                    elif opc=="4":
                        print("""
A.Autorización de compra repuestos (SI / NO)
B.Volver al Menú principal
""")
                    elif opc=="5":
                        print("""
A.Caja (Entrada / Salida / Saldo)
B.Operaciones de alquiler y venta (General / Por vendedor)
C.Compra de repuestos
D.Volver al Menú principal
""")
                    elif opc == "0":
                        print("Ha cerrado sesión")
                        break
                    else:
                        print("Opción incorrecta. Intente nuevamente.\n")
# ------------------------------ FIN MENÚ PRINCIPAL SUPERVISOR --------------------------


# ------------------------------ MENÚ PRINCIPAL VENDEDOR --------------------------------
            elif usuario=="v":
                while True:
                
                    print("""
                                    
1.	Flota de rodados  
2.	Presupuesto 
3.  Cerrar Sesion 
            """)
                    opc=input() 
                    if opc=="1":
                        print("""                                     
A. Listado de rodados (solo los disponibles)
B. Disponibilidad de alquiler (SI / NO)
C. Lista de precios (Visualización)
D. Volver al menú principal
""")                       
                    elif opc == "2":
                        print('''
A. Tipo de operación
B. Carga de cliente
C. Medio de pago
D. Promociones (SI / NO)
E. Facturación
F. Volver al menú principal
''')
                    else:
                        print("Ha cerrado sesión")
                        break

# ------------------------------ FIN MENÚ PRINCIPAL VENDEDOR ----------------------------

# ------------------------------ MENÚ PRINCIPAL TÉCNICO ---------------------------------
            else:
                while True:                
                    print("""
1.	Flota de rodados  
2.	Devolución 
3.	Compra de repuestos 
4.	Acceso a informes mensuales 
5.  Cerrar Sesion 
            """)
                    opc=input() 
                    if opc=="1":
                        print("""                                     
A. Listado de rodados 
B. Disponibilidad de alquiler (SI / NO)
C. Modificación (KM / VTV / Repuestos / Accesorios)
D. Volver al menú principal
""")                       
                    elif opc == "2":
                        print('''
A. Reingreso de rodado
B. Volver al menú principal
''')
                    elif opc == "3":
                        print('''
A. Presupuesto para compra de repuestos
B. Presupuestos aprobados (Compra)
C. Acceso a la caja chica
D. Volver al menú principal
''')
                    elif opc == "4":
                        print('''
A. Caja (Entrada / Salida / Saldo)
B. Operaciones de alquiler y venta (General / Por vendedor)
C. Compra de repuestos
D. Volver al menú principal
''')
                    else:
                        print("Ha cerrado sesión")
                        break
# ------------------------------ FIN MENÚ PRINCIPAL TÉCNICO -----------------------------
            break
        else:  
            print("contraseña incorrecta.")
            
    else:
        print("Usuario incorrecto.")