
usuariosActivos = {'supervisor':'1234','vendedor':'5678','tecnico':'91011'}

while True:
    usuario = input("\nUsuario: ")
    if usuario in usuariosActivos:
        passUsu = input("Contraseña: ")
        if passUsu==usuariosActivos[usuario]:
            print("\nBienvenido",usuario)
            if usuario=="supervisor":

# --------------------------------- MENÚ SUPERVISOR -------------------------------
                while True:                
                    print("""
1)  Flota de rodados  
2)  Empleados ABM 
3)  Promociones y Precios
4)  Compra de repuestos (Autorización y pago)
5)  Acceso a informes mensuales
6)  Cerrar Sesión 
""") 
                    opc=input()
                    if opc=="1":
                        print("""
A) Ingreso (Alta: Datos y Finalidad) 
B) Baja (Motivo)
C) Modificación (Precio / KM / Seguro / VTV / Repuestos / Accesorios)
D) Disponibilidad de alquiler (SI / NO)
E) Listado de rodados 
F) Lista de precios (Visualización y modificación)
G) Volver al Menú principal
""")

                    elif opc=="2":
                        print("""
A) Ingreso (Alta)
B) Baja (Motivo)
C) Modificación (Categoría / Sueldo / Comisión)
D) Volver al Menú principal
""")
                    elif opc=="3":
                        print("""
A) Ingreso y modificación de precios
B) Descuentos bancarios 
C) Volver al Menú principal
""")
                    elif opc=="4":
                        print("""
A) Autorización de compra repuestos (SI / NO)
B) Volver al Menú principal
""")
                    elif opc=="5":
                        print("""
A) Caja (Entrada / Salida / Saldo)
B) Operaciones de alquiler y venta (General / Por vendedor)
C) Compra de repuestos
D) Volver al Menú principal
""")
                    else:
                        print("Ha cerrado sesión")
                        break                 
# --------------------------------- FIN MENÚ SUPERVISOR ---------------------------

# --------------------------------- MENÚ VENDEDOR ---------------------------------
            elif usuario=="vendedor":
                while True:
                
                    print("""
                                    
1) Flota de rodados  
2) Presupuesto 
3) Cerrar Sesion 
            """)
                    opc=input() 
                    if opc=="1":
                        print("""                                     
A) Listado de rodados (solo los disponibles)
B) Disponibilidad de alquiler (SI / NO)
C) Lista de precios (Visualización)
D) Volver al menú principal
""")                       
                    elif opc == "2":
                        print('''
A) Tipo de operación
B) Carga de cliente
C) Medio de pago
D)Promociones (SI / NO)
E) Facturación
F) Volver al menú principal
''')
                    else:
                        print("Ha cerrado sesión")
                        break

# --------------------------------- FIN MENÚ VENDEDOR -----------------------------

# --------------------------------- MENÚ TÉCNICO ----------------------------------
            else:
                while True:                
                    print("""
1) Flota de rodados  
2) Devolución 
3) Compra de repuestos 
4) Acceso a informes mensuales 
5) Cerrar Sesion 
            """)
                    opc=input() 
                    if opc=="1":
                        print("""                                     
A) Listado de rodados 
B) Disponibilidad de alquiler (SI / NO)
C) Modificación (KM / Repuestos)
D) Volver al menú principal
""")                       
                    elif opc == "2":
                        print('''
A) Reingreso de rodado
B) Volver al menú principal
''')
                    elif opc == "3":
                        print('''
A) Presupuesto para compra de repuestos
B) Presupuestos aprobados (Compra)
C) Acceso a la caja chica
D) Volver al menú principal
''')
                    elif opc == "4":
                        print('''
A) Caja (Entrada / Salida / Saldo)
B) Operaciones de alquiler y venta (General / Por vendedor)
C) Compra de repuestos
D) Volver al menú principal
''')
                    else:
                        print("Ha cerrado sesión")
                        break
# --------------------------------- FIN MENÚ TÉCNICO ------------------------------
            break
        else:  
            print("Contraseña incorrecta")
            
    else:
        print("Usuario incorrecto")