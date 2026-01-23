#Funcion para validar RUT
def validar_rut(rut, estudiantes):
    if not rut:
        return False
    
    #Conjunto de rut registrados para evitar duplicados
    ruts_existentes = {e["rut"] for e in estudiantes}
    
    return rut not in ruts_existentes

#Funcion que valida edad ingresada por usuario
def validar_edad():
    while True:
        try:
            edad = int(input("Edad: "))
            
            if edad >= 17:
                return edad
            else:
                print("La edad debe ser de 17 años o mayor ")
        
        except ValueError:
            print("Ingrese un número válido.")
            

#🧠 Explicación
#Centraliza validaciones
#Usa:
#Conjuntos
#Bucles
#Manejo de errores (try/except)
#Evita errores y mejora la calidad del sistema