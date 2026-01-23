#Importamos las funciones de gestión del sistema
from gestion import (
    cargar_estudiantes,
    guardar_estudiantes,
    agregar_estudiante,
    listar_estudiantes,
    buscar_estudiante,
    eliminar_estudiante,
)
#Funcion que controla el menú principal
def mostrar_menu():
    estudiantes = cargar_estudiantes() #Se cargan datos de estudiantes desde archivo CSV al iniciar el sistema
    
    #Tupla que almacena las opciones del menú
    opciones = (
        "1. Agregar estudiante",
        "2. Lista de estudiantes",
        "3. Buscar estudiante por RUT",
        "4. Eliminar estudiante",
        "5. Salir"
    )
#Bucle para mantener menú activo
    while True:
        print("\n--- MENÚ GESTIÓN DE ESTUDIANTES ---")
    #Recorremos tupla para mostrar opciones
        for opcion in opciones:
            print(opcion)
        #Bloque para registrar opcion ingresada por usuario
        opcion = input("Seleccione una opción: ")
        #Bloque condicional para decidir acción a ejecutar
        if opcion == "1":
            agregar_estudiante(estudiantes)
        elif opcion == "2":
            listar_estudiantes(estudiantes)
        elif opcion == "3":
            rut = input("Ingrese RUT a buscar: ")
            buscar_estudiante(estudiantes, rut)
        elif opcion == "4":
            rut = input("Ingrese RUT a eliminar: ")
            eliminar_estudiante(estudiantes, rut)
        elif opcion == "5":
            #Antes de salir guarda los datos
            guardar_estudiantes(estudiantes)
            print("Datos guardados. ¡Hasta luego!")
            break # Sale del bucle y finaliza el programa
        else:
            print("Opción invalida")

#🧠 Explicación
#Controla toda la interacción con el usuario
#Usa:
#Tuplas
#Bucles
#Condicionales
#No gestiona datos directamente → delega a gestion.py
#Mantiene el programa activo hasta que el usuario decide salir