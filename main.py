#Importamos la funcion principal que muestra el menú del sistema
from menu import mostrar_menu

#Funcion principal del programa, inicia el sistema
def main():
    mostrar_menu() #Llama al menú principal

#Código solo se ejecuta cuando este archivo es el principal
if __name__ == "__main__":
    main()

#🧠 Explicación
#main.py es el archivo de inicio del proyecto
#No contiene lógica de negocio
#Su función es iniciar el sistema de forma ordenada
#Permite reutilizar el proyecto como módulo en el futuro