#Funcion recursiva que busca a usuario en la lista
def buscar_recursivo(estudiantes, rut, indice):
    if indice >= len(estudiantes):
        return None
    
    #Si encuentra al usuario
    if estudiantes[indice]["rut"] == rut:
        return estudiantes[indice]
    
    #Llamada recursiva que avanza en la lista
    return buscar_recursivo(estudiantes, rut, indice + 1)
