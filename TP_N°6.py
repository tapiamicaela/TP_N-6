"""1) Hacer un programa que gestiones datos para una escuela.
El programa tiene que ser capaz de:
    a) Llevar un registro de todos los datos de alumnos de la escuela (Nombre,
    Apellido, fecha de nacimiento, DNI, Nombre de Tutor, registro de todas las
    notas, cantidad de faltas, cantidad de amonestaciones recibidas.
    Recomendación: Para llevar un registro de estos dato se puede
    utilizar un diccionario estructurado de la siguiente manera:
    {
    “Alumnos” : [alumno1,alumno2,alumno3 ]
    }
    Donde cada alumno es otro diccionario estructurado de la
    siguiente forma:
    {
    “Nombre”: nombre de alumno,
    “Apellido” : apellido de alumno,
    “DNI” : DNI de alumno
    “Fecha de nacimiento”, fecha de nacimiento de alumno,
    “Tutor” : nombre y apellido de tutor,
    “Notas” : todas las notas del alumno,
    “Faltas” : cantidad de faltas,
    “amonestaciones” : cantidad de amonestaciones
    }
    En esta estructura:
    Datos = {
    “Alumnos” : [alumno1,alumno2,alumno3 ]
    }
    Para acceder por ejemplo al numero de DNI del tercer alumno
    podríamos hacer algo así:
    Datos[“Alumnos”][2][“DNI”]
Este es un ejemplo de estructura, se puede cambiar
completamente o hacer algunos cambios sobre el para mejorar el
orden (si lo consideran necesario)
b) Mostrar los datos de cada alumno
c) Modificar los datos de los alumnos
d) Agregar alumnos
e) Expulsar alumnos"""


datos_alumnos={
    'Alumnos' : [
        {
        'Nombre': "Milagros",
        'Apellido' : "Tapia",
        'DNI' : "43441001",
        'Fecha de nacimiento': "17/06/2001",
        'Tutor' : "Graciela Cutipa",
        'Notas' : [10,9,8,7],
        'Faltas' : 2,
        'Amonestaciones' : 0
        },

        {
        'Nombre': "Juan",
        'Apellido' : "Perez",
        'DNI' : "46441023",
        'Fecha de nacimiento': "15/07/2004",
        'Tutor' : "Osar Perez",
        'Notas' : [7,8,8,7],
        'Faltas' : 6,
        'Amonestaciones' : 2
        },

        {
        'Nombre': "Luis",
        'Apellido' : "Martinez",
        'DNI' : "46229209",
        'Fecha de nacimiento': "27/08/2006",
        'Tutor' : "Lucia Martinez",
        'Notas' : [6,7,9,6],
        'Faltas' : 4,
        'Amonestaciones' : 1
        },

        {
        'Nombre': "Rodrigo",
        'Apellido' : "Fernandez",
        'DNI' : "46229118",
        'Fecha de nacimiento': "27/01/2006",
        'Tutor' : "Ana Martinez",
        'Notas' : [6,8,10,6],
        'Faltas' : 5,
        'Amonestaciones' : 4
        },
    ]
}


def mostrar_alumno(dni,datos_alumnos):
    for alumno in datos_alumnos['Alumnos']: 
        if alumno["DNI"]==dni:
            for dato in alumno:
                print(f"{dato}: {alumno[dato]}")
            return
    print("Alumno no encontrado.")


def agregar_alumno(datos_alumnos):
    nuevo_alumno={}
    nombre=input(f"Ingrese el nombre del alumno: ")
    nuevo_alumno['Nombre'] = nombre
    apellido=input(f"Ingrese el apellido del alumno: ")
    nuevo_alumno['Apellido'] = apellido
    dni=input(f"Ingrese el DNI del alumno: ")
    nuevo_alumno['DNI'] = dni
    nacimiento=input(f"Ingrese la Fecha de nacimiento del alumno: ")
    nuevo_alumno['Fecha de nacimiento'] = nacimiento
    tutor=input(f"Ingrese el nombre del tutor: ")
    nuevo_alumno['Tutor'] = tutor
    notas_str = input("Ingrese las notas separadas por comas (ej: 10,9,8): ")
    nuevo_alumno["Notas"] = [int(nota) for nota in notas_str.split(',')]
    faltas=int(input(f"Ingrese el numero de faltas: "))
    nuevo_alumno['Faltas'] = faltas
    amonestacion=int(input(f"Ingrese el numero de amonestaciones: "))
    nuevo_alumno['Amonestaciones'] = amonestacion

    datos_alumnos['Alumnos'].append(nuevo_alumno)
    print("Alumno agregado correctamente.")

         
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
    print("1-MOSTRAR ALUMNO")
    print("2-AGREGAR ALUMNO")
    print("3-MODIFICAR ALUMNO")
    print("4-ELIMINAR ALUMNO")
    print("5-SALIR")
    print("----------------------")

    operacion= int(input("Ingrese el numero correspondiente a la operacion que desee realizar: "))
    if operacion==1:
        dni= input("Ingrese el DNI del alumno que desee ver la informacion: ")
        mostrar_alumno(dni,datos_alumnos)
    elif operacion==2:
         agregar_alumno(datos_alumnos)
         for alumno in datos_alumnos['Alumnos']: 
            for dato in alumno:
                print(f"{dato}: {alumno[dato]}")
            print("--------")
    #elif operacion==3:
         
    elif operacion==4:
        dni= input("Ingrese el DNI del alumno que desee eliminar: ")
        eliminar_alumno(dni,datos_alumnos)
        for alumno in datos_alumnos['Alumnos']: 
            for dato in alumno:
                print(f"{dato}: {alumno[dato]}")
            print("--------")
    
    elif operacion==5:
         break
    else:
         print("Error: Operación no encontrada")