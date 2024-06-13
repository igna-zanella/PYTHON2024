
usuariosActivos = {'supervisor':'1234','vendedor':'5678','tecnico':'91011'}

autos = {"ABC123":{"kilometraje":0, "precio":0,"tipo":"alquiler", "disponibilidad":"SI"}, 
        "HLS555":{"kilometraje":50000, "precio":13000000,"tipo":"alquiler", "disponibilidad":"SI"},
        "AB976CC":{"kilometraje":20000, "precio":29000000,"tipo":"venta", "disponibilidad":"NO"},
        "AD571RA":{"kilometraje":10000, "precio":42000000,"tipo":"alquiler", "disponibilidad":"SI"},
        "GSM788":{"kilometraje":20000, "precio":16000000,"tipo":"venta", "disponibilidad":"NO"}}




while True:
    usuario = input("Ingrese usuario: ")
    if usuario in usuariosActivos:
        passUsu = input("Ingrese contraseña: ")
        if passUsu==usuariosActivos[usuario]:
            print("Bienvenido",usuario)
            if usuario=="s":

# --------------------------------- MENÚ SUPERVISOR -------------------------------
                while True:                
                    print("""
1.	Flota de rodados  
2.	Empleados ABM 
3.	Promociones y Precios
4.	Compra de repuestos (Autorización y pago)
5.  Acceso a informes mensuales
6.  Cerrar Sesion 
            """) 
                    opc=input()
                    if opc=="1":
                        while True:
                            print("""
A.Ingreso (Alta: Datos y Finalidad) 
B.Baja (Motivo)
C.Modificación (Precio / KM / Tipo)
D.Disponibilidad de alquiler (SI / NO)
E.Listado de rodados 
F.Lista de precios (Visualización y modificación)
G.Volver al Menú principal
""")
                            opcSub = input("Ingrese opción: ").upper()
                            if opcSub == "A":
                                print("Ingrese los datos del nuevo vehículo: \n")
                                patente = input("Patente: ")
                                km = int(input("Kilometraje: "))
                                precio = int(input("Precio: $"))
                                tipo = input("Tipo: ")
                                if tipo == "alquiler":
                                    disponibilidad = "SI"
                                else:
                                    disponibilidad = "NO"
                                    
                                autos[patente] = {"kilometraje":km, "precio":precio, "tipo":tipo, "disponibilidad": disponibilidad}
                                
                                for x in autos: #Obtenemos la key de cada elemento dentro del diccionario 
                                    if x == patente:
                                        print("\nEl vehículo con patente '{}' contiene los siguientes datos: \nKilometraje: {} kms  \nPrecio: ${}  \nTipo: {}  \nDisponibilidad: {} ".format(patente, autos[patente]['kilometraje'], autos[patente]['precio'], autos[patente]['tipo'], autos[patente]['disponibilidad']))
                                print("\nVehículo ingresado correctamente")
                                input("ENTER para continuar...")

                            elif opcSub == "B":
                                patente = input("Ingrese la patente del vehículo a eliminar: \n")
                                del(autos[patente])
                                print("\nVehículo eliminado")
                                input("ENTER para continuar...")

                            elif opcSub == "C":
                                patente = input("Ingrese la patente del vehículo a modificar: \n")
                                for x in autos:
                                    if x == patente:
                                        km = int(input("Kilometraje: "))
                                        precio = int(input("Precio: $"))
                                        tipo = input("Tipo: ")
                                        disponibilidad = input("Disponibilidad (SI/NO): ").upper()
                                        autos[patente] = {"kilometraje":km, "precio":precio, "tipo":tipo, "disponibilidad":disponibilidad}
                                        
                                for key in autos: #Obtenemos la key de cada elemento dentro del diccionario 
                                    
                                    print("\nEl vehículo con patente '{}' contiene los siguientes datos: \nKilometraje: {}  \nPrecio: {}  \nTipo: {}  \nDisponibilidad: {} ".format(key, autos[key]['kilometraje'], autos[key]['precio'], autos[key]['tipo'], autos[key]['disponibilidad']))
                                print("\nVehículo modificado")
                                input("ENTER para continuar...")

                            elif opcSub == "D":
                                print("\nVehículos disponibles:")
                                for patente, clave in autos.items():
                                    if autos[patente]['disponibilidad'] == "SI" and autos[patente]['tipo'] == "alquiler":
                                        print("\nPatente:", patente)
                                        for valor in clave:
                                            print(valor + ":", clave[valor])
                                input("\nENTER para continuar...")
                            
                            elif opcSub == "E":
                                
                                print("\nNuestra flota:")
                                for patente, clave in autos.items():
                                    print("\nPatente:", patente)
                                    for valor in clave:
                                        print(valor + ":", clave[valor])
                                input("\nENTER para continuar...")
                            
                            elif opcSub == "F":
                                
                                print("\nListado de precios:")
                                for patente in autos.items():
                                    print("\nPatente:", patente)
                                    print("Precio: $", autos[patente]['precio'])
                                input("\nENTER para continuar...")
                                
                            else:
                                break

                    elif opc=="2":
                        print("""
A.Ingreso (Alta)
B.Baja (Motivo)
C.Modificación (Categoría / Sueldo / Comisión)
D.Volver al Menú principal
""")
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
                    else:
                        print("Ha cerrado sesión")
                        break                 
# --------------------------------- FIN MENÚ SUPERVISOR ---------------------------

# --------------------------------- MENÚ VENDEDOR ---------------------------------
            elif usuario=="vendedor":
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

# --------------------------------- FIN MENÚ VENDEDOR -----------------------------

# --------------------------------- MENÚ TÉCNICO ----------------------------------
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
# --------------------------------- FIN MENÚ TÉCNICO ------------------------------
            break
        else:  
            print("contraseña incorrecta.")
            
    else:
        print("Usuario incorrecto.")