def contar_lineas_codigo(archivo):
    if not archivo.endswith(".py"):
        print("El archivo debe tener extensión .py")
        return
    
    try:
        with open(archivo, "r") as file:
            lineas = file.readlines()
            contador = 0
            for linea in lineas:
                linea = linea.strip()
                if linea != "" and not linea.startswith("#"):
                    contador += 1
            print(f"El número de líneas de código en el archivo {archivo} es: {contador}")
    except FileNotFoundError:
        print(f"No se encontró el archivo {archivo}")

ruta_archivo = input("Ingrese la ruta del archivo .py: ")
contar_lineas_codigo(ruta_archivo)
