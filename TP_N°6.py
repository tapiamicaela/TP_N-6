archivo_alumnos= r"C:\repositorioGit\legajodealumnos.txt"

def mostrar_alumno(dni,archivo):
    with open(archivo,"r") as file:
        lineas=file.readlines()
        for alumno in lineas:
            dato=alumno.split(";")
            if dato[2]==dni:
                print(f"Nombre: {dato[0]}")
                print(f"Apellido: {dato[1]}")
                print(f"DNI: {dato[2]}")
                print(f"Fecha de nacimiento: {dato[3]}")
                print(f"Tutor: {dato[4]}")
                print(f"Notas: {dato[5]}")
                print(f"Faltas: {dato[6]}")
                print(f"Amonestaciones: {dato[7]}")
                print("-------------------------------------")
                return
        print("Alumno no encontrado.")


def mostrar_todos_alumnos(archivo):
    with open(archivo, "r") as file:
        lineas=file.readlines()
        print("Listado de todos los alumnos:\n")
        for alumno in lineas:
            dato=alumno.strip().split(";")
            if len(dato) >= 8:
                print(f"Nombre: {dato[0]}")
                print(f"Apellido: {dato[1]}")
                print(f"DNI: {dato[2]}")
                print(f"Fecha de nacimiento: {dato[3]}")
                print(f"Tutor: {dato[4]}")
                print(f"Notas: {dato[5]}")
                print(f"Faltas: {dato[6]}")
                print(f"Amonestaciones: {dato[7]}")
                print("-------------------------------------")


def ingresar_datos():
    dato=[]
    dato.append(input(f"Ingrese el Nombre del alumno: "))
    dato.append(input(f"Ingrese el Apellido del alumno: "))
    dato.append(input(f"Ingrese el DNI del alumno: "))
    dato.append(input(f"Ingrese la Fecha de nacimiento del alumno: "))
    dato.append(input(f"Ingrese el nombre del Tutor: "))
    notas_str = input("Ingrese las notas separadas por comas (ej: 10,9,8): ")
    dato.append(f"[{notas_str}]")
    dato.append(input(f"Ingrese el numero de faltas: "))
    dato.append(input(f"Ingrese el numero de amonestaciones: "))

    return dato


def agregar_alumno(archivo):
    nuevo_alumno=ingresar_datos()
    nuevo_dni=nuevo_alumno[2]
    with open(archivo,"r") as file:
        lineas=file.readlines()
        for alumno in lineas:
            if alumno !="":
                dato=alumno.split(";")
                if dato[2]==nuevo_dni:
                    print("Error: este alumno ya existe")
                    return
        alumno=";".join(nuevo_alumno) + "\n"
        with open(archivo,"a") as file:
                file.write(alumno)
        print("Alumno agregado correctamente.")


def modificar_alumno(dni,archivo):
    with open(archivo,"r") as file:
        lineas=file.readlines()
        for i in range(len(lineas)):
            dato=lineas[i].split(";")
            if dato[2]==dni:
                print("¿Qué dato desea modificar?")
                print("1. Nombre")
                print("2. Apellido")
                print("3. DNI")
                print("4. Fecha de nacimiento")
                print("5. Tutor")
                print("6. Notas")
                print("7. Faltas")
                print("8. Amonestaciones")
                dato_modificar=input("Ingrese el numero correspondiente al dato que desea modificar: ")

                if dato_modificar=="1":
                    modifica=input(f"Ingrese el nuevo Nombre: ")
                    dato[0]=modifica
                elif dato_modificar=="2":
                    modifica=input(f"Ingrese el nuevo Apellido: ")
                    dato[1]=modifica
                elif dato_modificar=="3":
                    modifica=input(f"Ingrese el nuevo DNI: ")
                    dato[2]=modifica
                elif dato_modificar=="4":
                    modifica=input(f"Ingrese la nueva Fecha de nacimiento: ")
                    dato[3]=modifica
                elif dato_modificar=="5":
                    modifica=input(f"Ingrese el nuevo Tutor: ")
                    dato[4]=modifica
                elif dato_modificar=="6":
                    modifica=input(f"Ingrese las nuevas Notas: ")
                    dato[5]=f"[{modifica}]"
                elif dato_modificar=="7":
                    modifica=input(f"Ingrese la nueva cantidad de Faltas: ")
                    dato[6]=modifica
                elif dato_modificar=="8":
                    modifica=input(f"Ingrese la nueva cantidad de Amonestaciones: ")
                    dato[7]=modifica
                else:
                    print("Error: Opción no valida")
                    return

                alumno_modif=";".join(dato) + "\n"
                lineas[i]= alumno_modif
                with open(archivo,"w") as file:
                    file.writelines(lineas)
                print("Dato modificado correctamente.")
                return
        print("Alumno no encontrado.")


def eliminar_alumno(dni, archivo):
    with open(archivo, "r") as file:
        lineas = file.readlines()
        for i in range(len(lineas)):
            dato = lineas[i].split(";")
            if dato[2] == dni:
                lineas.remove(lineas[i])
                with open(archivo, "w") as file:
                    file.writelines(lineas)
                print("Alumno eliminado correctamente.")
                return

        print("Alumno no encontrado.")


print()
print("Bienvenido al Sistema de Gestión de Nuestra Escuela")
while True:
    print()
    print("====== MENÚ PRINCIPAL ======")
    print("1- MOSTRAR ALUMNO")
    print("2- MOSTRAR TODOS LOS ALUMNOS")
    print("3- AGREGAR ALUMNO")
    print("4- MODIFICAR ALUMNO")
    print("5- ELIMINAR ALUMNO")
    print("6- SALIR")
    print("===========================")
    print()

    operacion= input("Ingrese el numero correspondiente a la operacion que desee realizar: ")
    if operacion=="1":
        dni= input("Ingrese el DNI del alumno que desee ver la informacion: ")
        print("\n")
        mostrar_alumno(dni,archivo_alumnos)
    elif operacion=="2":
        print("\n")
        mostrar_todos_alumnos(archivo_alumnos)
    elif operacion=="3":
        agregar_alumno(archivo_alumnos)
        print("\n")
        mostrar_todos_alumnos(archivo_alumnos)
    elif operacion=="4":
        dni= input("Ingrese el DNI del alumno que desee modificar: ")
        modificar_alumno(dni,archivo_alumnos)
        print("\n")
        mostrar_todos_alumnos(archivo_alumnos)
    elif operacion=="5":
        dni= input("Ingrese el DNI del alumno que desee eliminar: ")
        eliminar_alumno(dni,archivo_alumnos)
        print("\n")
        mostrar_todos_alumnos(archivo_alumnos)
    elif operacion=="6":
        print("Saliendo del programa, ¡Hasta luego!") 
        break
    else:
         print("Error: Operación no encontrada")