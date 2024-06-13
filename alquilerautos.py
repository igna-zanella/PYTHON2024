# usuarios = {"fede":{"tipo":'s',"clave":'1234'},"juan":{"tipo":'v',"clave":'1234'},"pepe":{"tipo":'t',"clave":'1234'}}
# autos={
#     "abc123":{"km":5000,"precio":90000,"tipo":"v","disponibilidad":"s"},
#     "jkl123":{"km":10000,"precio":100000,"tipo":"a","disponibilidad":"n"},
#     "ad123jk":{"km":0,"precio":190000,"tipo":"v","disponibilidad":"s"}
# }
# operaciones={"1":{"cliente":"12345678","patente":"abc123","usuario":"fede"},
#             "2":{"cliente":"12345678","patente":"jkl123","usuario":"juan"},   
#             "3":{"cliente":"1234","patente":"jkl123","usuario":"juan"}
# }
# clientes={"12345678":{"nombre":"hector","clas":1,"tel":1234},
#         "1234":{"nombre":"lopez","clas":1,"tel":111235}
#         }
# for o in operaciones:
#     if autos[operaciones[o]["patente"]]["tipo"]=="a":
#         print(operaciones[o],clientes[operaciones[o]["cliente"]]["tel"],clientes[operaciones[o]["cliente"]]["nombre"])

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
            "87654321":{"nombre":'Paula', "apellido":'Vieytes',"tipo":'Taller', "sueldo":500000},
            "33112244":{"nombre":'José', "apellido":'Barrios',"tipo":'Taller', "sueldo":500000},
            "12345678":{"nombre":'Rafael', "apellido":'Walsh',"tipo":'Ventas',"sueldo":450000}
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

repuestos = {
    "WWW111":{"pieza":'bomba de agua', "precio": 120000}
}

#caja = 2000000

# ------------------------- DECLARACIÓN DE FUNCIONES ------------------------------------

def loguear():
    while True:
        usuario = input("Ingrese usuario:")
        if usuario in usuarios:
            clave = input("Ingrese contraseña: ")
            if clave==usuarios[usuario]["clave"]:
                print("Bienvenido",usuario)
                return usuario
            else:  
                print("contraseña incorrecta.")
        else:
            print("Usuario incorrecto.")



# ------------------------- SISTEMA SUPERVISOR -------------------------------------------
# ------------------------- AUTOS --------------------------------------------------------

def menuRodados():
        print("""
A.Ingreso (Alta: Datos y Finalidad) 
B.Baja (Motivo)
C.Modificación (Precio / KM / Seguro / VTV / Repuestos / Accesorios)
D.Disponibilidad de alquiler (SI / NO)
E.Disponibilidad de venta (SI / NO)
F.Listado de rodados 
0.Volver al Menú principal
""")

def altaAutos():
    patente=input("Ingrese patente: ")
    km=int(input("Ingrese km:"))
    precio=int(input("Ingrese el precio:"))
    tipo=input("Ingrese tipo:")
    dis=input("Esta disponible?:")
    autos[patente]={"km":km,"precio":precio,"tipo":tipo,"disponibilidad":dis}

def bajaAutos():
    for p in autos:
        print(p)
        patente=input("ingrese una patente")
        del(autos[patente])

def modificarAuto():
    for p in autos:
        print(p)
    patente=input("Ingrese patente: ")
    if patente in autos:
        km=int(input("Ingrese km:"))
        precio=int(input("Ingrese el precio:"))
        tipo=input("Ingrese tipo:")
        dis=input("Esta disponible?:")
        autos[patente]={"km":km,"precio":precio,"tipo":tipo,"disponibilidad":dis}
    else:
        print("Patente inexistente")    

def dispAlquiler():
    for p in autos:
        if autos[p]["tipo"]=="a" and autos[p]["disponibilidad"]=="s":
            print(autos[p])

def dispVenta():
    for p in autos:
        if autos[p]["tipo"]=="v" and autos[p]["disponibilidad"]=="s":
            print(autos[p])

def listaAutos():
    for p in autos:
        print(autos[p])

def autorizarRepuestos(caja):
    print("Autorizaciones de repuestos")
    print(repuestos)
    autorizazion = input("Autoriza la compra de repuestos (SI / NO): ")
    if autorizazion == "SI":
        
        caja -= repuestos["WWW111"]["precio"]
        print("Repuesto autorizado")
        return caja
    else:
        print("Repuesto no autorizado")
        
def informeCaja(caja):
    print("Caja: ", caja)
    
        

# ------------------------- FIN AUTOS ---------------------------------------------------

# ------------------------- EMPLEADOS ---------------------------------------------------

def menuEmpleados():
    print("""
A.Ingreso (Alta)
B.Baja (Motivo)
C.Modificación (Categoría / Sueldo / Comisión)
0.Volver al Menú principal
""")
    
def altaEmpleados():
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

def bajaEmpleados():
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
                
def modificarEmpleados():
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


# ------------------------- FIN EMPLEADOS -----------------------------------------------
# ------------------------- FIN SISTEMA SUPERVISOR --------------------------------------


def menuSupervisor():
    while True:                
                    print("""
1.	Flota de rodados  
2.	Empleados ABM 
3.	Compra de repuestos (Autorización y pago)
4.	Acceso a informes mensuales
0.  Cerrar Sesion 
            """) 
                    opc=input()
                    if opc=="1":
# ------------------------- LLAMADO FUNCIONES AUTOS -------------------------------------
                        menuRodados()

                        opc2=input()
                        if opc2=="a":
                            altaAutos()

                        elif opc2=="b":
                            bajaAutos()

                        elif opc2=="c":
                            modificarAuto()
                            
                        elif opc2=="d":
                            dispAlquiler()

                        elif opc2=="e":
                            dispVenta()

                        elif opc2=="f":
                            listaAutos()

                        elif opc2=="0":
                            print("Volviendo al menu principal....")
                        else:
                            print("opcion incorrecta")
                            
                        
                    elif opc=="2":
# ------------------------- LLAMADO FUNCIONES EMPLEADOS ---------------------------------
                        menuEmpleados()

                        opc2=input()
                        if opc2=="a":
                            altaEmpleados()
                        elif opc2=="b":
                            bajaEmpleados()
                        elif opc2=="c":
                            modificarEmpleados()
                        elif opc2=="0":
                            print("Volviendo al menu principal....")
                        else:
                            print("opcion incorrecta")

                    elif opc=="3":
                        print("""
A.Autorización de compra repuestos (SI / NO)
B.Volver al Menú principal
""")
                        opc2=input()
                        if opc2 == "a":
                            autorizarRepuestos()

                    elif opc=="4":
                        print("""
A.Caja
0.Volver al Menú principal
""")
                        opc2=input()
                        if opc2 == "a":
                            informeCaja(caja)
                    else:
                        print("Ha cerrado sesión")
                        return caja                 

def menuVendedor():
    while True:
        print("""
1.	Flota de rodados  
2.	Presupuesto 
3.  Cerrar Sesion 
            """)
        opc=input() 
        if opc=="1":
            print("""                                     
A.Listado de rodados (solo los disponibles)
B-Disponibilidad de alquiler (SI / NO)
C.Lista de precios (Visualización)
D.Volver al menu principal
""")   


def menuTecnico():
    while True:
        print("""
    1.	Flota de rodados  
    2.	Devolución 
    3.	Compra de repuestos 
    4.	Acceso a informes mensuales 
    5.  Cerrar Sesion 
                """)
        break
        

def main():
    caja = 5000000
#    while True:
    usuario=loguear()
    print(usuario)
    if usuarios[usuario]["tipo"]=="s":
        menuSupervisor(caja)
    elif usuarios[usuario]["tipo"]=="v":
        menuVendedor()
    else:
        menuTecnico()
        


main()
