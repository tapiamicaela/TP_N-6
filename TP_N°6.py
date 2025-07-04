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
    dato.append(input(f"Ingrese el nombre del alumno: "))
    dato.append(input(f"Ingrese el apellido del alumno: "))
    dato.append(input(f"Ingrese el DNI del alumno: "))
    dato.append(input(f"Ingrese la Fecha de nacimiento del alumno: "))
    dato.append(input(f"Ingrese el nombre del tutor: "))
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


def modificar_alumno(dni,datos_alumnos):
    for alumno in datos_alumnos['Alumnos']:
        if alumno["DNI"]==dni:
            print("¿Qué dato desea modificar?")
            print("1. Nombre")
            print("2. Apellido")
            print("3. DNI")
            print("4. Fecha de nacimiento")
            print("5. Tutor")
            print("6. Notas")
            print("7. Faltas")
            print("8. Amonestaciones")
            dato_modificar=input("¿Que dato desea modificar? ")
            if dato_modificar!="DNI":
                dato_modificar=dato_modificar.capitalize()

            if dato_modificar=="Nombre" or dato_modificar=="Apellido" or dato_modificar=="DNI" or dato_modificar=="Fecha de nacimiento" or dato_modificar=="Tutor":
                modifica=input(f"Ingrese el nuevo {dato_modificar}: ")
                alumno[dato_modificar]=modifica
            elif dato_modificar=="Faltas" or dato_modificar=="Amonestaciones":
                modifica=int(input(f"Ingrese la nueva cantidad de {dato_modificar}: "))
                alumno[dato_modificar]=modifica
            elif dato_modificar=="Notas":
                notas_str = input("Ingrese las nuevas notas separadas por comas: ")
                lista=[]
                for notas in notas_str.split(','):
                    lista.append(int(notas))
                alumno["Notas"] =lista
            else:
                print("Error: Opción no valida")
            print("Dato modificado correctamente.")
            return
    print("Alumno no encontrado.")


def eliminar_alumno(dni,datos_alumnos):
    for alumno in datos_alumnos['Alumnos']: 
        if alumno["DNI"]==dni:
            datos_alumnos['Alumnos'].remove(alumno)
            print("Alumno eliminado correctamente.")
            return
    print("Alumno no encontrado.")


print()
print("Bienvenido al Sistema de Gestión de la Nuestra Escuela")
while True:
    print("----------------------")
    print("1- MOSTRAR ALUMNO")
    print("2- MOSTRAR TODOS LOS ALUMNOS")
    print("3- AGREGAR ALUMNO")
    print("4- MODIFICAR ALUMNO")
    print("5- ELIMINAR ALUMNO")
    print("6- SALIR")
    print("----------------------")

    operacion= int(input("Ingrese el numero correspondiente a la operacion que desee realizar: "))
    if operacion==1:
        dni= input("Ingrese el DNI del alumno que desee ver la informacion: ")
        print("\n")
        mostrar_alumno(dni,r"C:\repositorioGit\legajodealumnos.txt")
    elif operacion==2:
        print("\n")
        mostrar_todos_alumnos(r"C:\repositorioGit\legajodealumnos.txt")
    elif operacion==3:
        agregar_alumno(r"C:\repositorioGit\legajodealumnos.txt")
        print("\n")
        mostrar_todos_alumnos(r"C:\repositorioGit\legajodealumnos.txt")
    elif operacion==4:
        dni= input("Ingrese el DNI del alumno que desee modificar: ")
        modificar_alumno(dni,r"C:\repositorioGit\legajodealumnos.txt")
        print("\n")
        mostrar_todos_alumnos(r"C:\repositorioGit\legajodealumnos.txt")
    elif operacion==5:
        dni= input("Ingrese el DNI del alumno que desee eliminar: ")
        eliminar_alumno(dni,r"C:\repositorioGit\legajodealumnos.txt")
        print("\n")
        mostrar_todos_alumnos(r"C:\repositorioGit\legajodealumnos.txt")
    elif operacion==6:
        print("Saliendo del programa, ¡Hasta luego!") 
        break
    else:
         print("Error: Operación no encontrada")