datosalumnos = {"nombre":"valor" , "nombre":"valor" , "nombre":"valor" , "nombre":"valor" , "nombre":"valor"}
seguir = "si"
while seguir == "si":
    opc = int(input("Que opcion desea elegir: 1(Añadir alumno/a), 2(Conocer numero de aprobados), 3(Mostrar todo el alumnado):"))
    if opc == 1:
        datosalumnos["nombre"] = input("introduce el nombre del alumno:")
        datosalumnos["valor"] = input("introduce si el alumno a aprobado/suspendido:")
        seguir = input("Desea seguir gestionanado informacion?")
    if opc == 2:
        numap = datosalumnos.get("aprobado")
        print("El numero de aprobados es " + str(numap))
        seguir = input("Desea seguir gestionanado informacion?")

    if opc == 3:
        print(datosalumnos)
        seguir = input("Desea seguir gestionanado informacion?")
else:
    print("Ha finalizado la sesion de gestion de la base de datos de la clase de 2K")
    