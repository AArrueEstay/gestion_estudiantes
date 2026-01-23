#Importamos módulo csv para trabajar con el archivo CSV
import csv

#Importamos funciones de validación y utilidades
from validaciones import validar_rut, validar_edad
from utils import buscar_recursivo

#Ruta donde se guardan los estudiantes
ruta_archivo = "datos/estudiantes.csv"

#Función que carga datos desde archivo CSV
def cargar_estudiantes():
    estudiantes = [] #Lista donde almacenarán los datos
    try:
        #Se abre el archivo en modo lectura
        with open(ruta_archivo, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            #Bloque que recorre cada fila del archivo
            for fila in lector:
                fila["edad"] = int(fila["edad"]) #Para convertir edad a entero
                estudiantes.append(fila)
    #Si el archivo no existe el sistema continua sin error
    except FileNotFoundError:
        pass
    
    return estudiantes

#Funcion que guarda datos en archivo CSV
def guardar_estudiantes(estudiantes):
    #Se abre el archivo en modo escritura
    with open(ruta_archivo, "w", newline="", encoding="utf-8") as archivo:
        campos = ["rut", "nombre", "edad", "carrera"]
        
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader() #Escribir encabezados
        escritor.writerows(estudiantes) #Escribir datos

#Funcion para agregar nuevo estudiante al sistema
def agregar_estudiante(estudiantes):
    rut = input("RUT: ")
    #Bloque que revisa que rut no este repetido
    if not validar_rut(rut, estudiantes):
        print("RUT inválido o duplicado.")
        return
    
    nombre = input("Nombre: ")
    edad = validar_edad()
    carrera = input("Carrera: ")
    
    #Diccionario
    estudiante = {
        "rut": rut,
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera
    }
    
    estudiantes.append(estudiante)
    print("Estudiante agregado correctamente.")
    
#Funcion que muestra usuarios registrados
def listar_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    for e in estudiantes:
        print(f"{e['rut']} - {e['nombre']} - {e['edad']} - {e['carrera']}")

#Funcion que busca a usuario usando recursividad
def buscar_estudiante(estudiantes, rut):
    resultado = buscar_recursivo(estudiantes, rut, 0)
    
    if resultado:
        print("Estudiante encontrado: ")
        print(resultado)
    else:
        print("Estudiante no encontrado.")

#Funcion que elimina a usuario segun RUT
def eliminar_estudiante(estudiantes, rut):
    for e in estudiantes:
        if e["rut"] == rut:
            estudiantes.remove(e)
            print("Estudiante eliminado.")
            return
    
    print("Estudiante no encontrado.")

#🧠 Explicación
#gestion.py contiene toda la lógica del sistema
#Maneja:
#Archivos
#Datos
#Operaciones CRUD
#Usa listas, diccionarios, bucles y condicionales
#Se apoya en otros módulos para validaciones y recursividad