
""" password = "cfp10Python"
usuariosActivos = ['supervisor','vendedor','tecnico']

while True:
    usuario = input("usuario")
    if usuario in usuariosActivos:
        passUsu = input("Contraseña: ")
    if passUsu == password:
        print("Se ha logueado correctamente")
        break
    else:
        print("Usuario no válido") """

usuariosActivos = {'supervisor':'1234','vendedor':'5678','tecnico':'91011'}
autos = {"ABC123":{"km":0, "precio":0,"tipo":"alquiler", "disponibilidad":"SI"}, "HLS555":{"km":50000, "precio":13000000,"tipo":"alquiler", "disponibilidad":"no"},"AB976CC":{"km":20000, "precio":19000000,"tipo":"venta", "disponibilidad":"si"},"AD571RA":{"km":10000, "precio":42000000,"tipo":"venta", "disponibilidad":"si"},"GSM788":{"km":20000, "precio":19000000,"tipo":"venta", "disponibilidad":"si"}}




while True:
    usuario = input("Ingrese usuario:")
    if usuario in usuariosActivos:
        passUsu = input("Ingrese contraseña: ")
        if passUsu==usuariosActivos[usuario]:
            print("Bienvenido",usuario)
            if usuario=="supervisor":

# --------------------------------- MENÚ SUPERVISOR -------------------------------
                while True:                
                    print("""
1.	Flota de rodados  
2.	Empleados ABM 
3.	Promociones y Precios
4.	Compra de repuestos (Autorización y pago)
5.	Acceso a informes mensuales
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
                                km = float(input("Kilómetros: "))
                                precio = float(input("Precio: "))
                                tipo = input("Tipo: ")
                                disponibilidad = input("Disponibilidad (SI/NO): ").upper()

                                autos[patente] = {"km":km, "precio":precio, "tipo":tipo}
                                print(autos)
                                print("\nVehículo ingresado correctamente!")
                                input("ENTER para continuar...")

                            elif opcSub == "B":
                                patente = input("Ingrese la patente del vehículo a eliminar: \n")
                                del(autos[patente])
                                print(autos)
                                print("\nVehículo eliminado")
                                input("ENTER para continuar...")

                            elif opcSub == "C":
                                patente = input("Ingrese la patente del vehículo a modificar: \n")
                                for x in autos:
                                    if x == patente:
                                        km = float(input("Kilómetros: "))
                                        precio = float(input("Precio: "))
                                        tipo = input("Tipo: ")
                                        disponibilidad = input("Disponibilidad (SI/NO): ").upper()
                                        autos[patente] = {"km":km, "precio":precio, "tipo":tipo, "disponibilidad":disponibilidad}
                                        
                                print(autos)
                                print("\nVehículo modificado")
                                input("ENTER para continuar...")

                            elif opcSub == "D":
                                for x in autos:
                                    if autos["ABC123"]["disponibilidad"] == "SI":
                                        print(autos)
                                        print("\nVehículo modificado")
                                        input("ENTER para continuar...")

                                


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