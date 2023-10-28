def guardar_tabla_multiplicar(numero):
    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10")
        return
    
    with open(f"tabla-{numero}.txt", "w") as file:
        for i in range(1, 11):
            resultado = numero * i
            file.write(f"{numero} x {i} = {resultado}\n")
    
    print(f"Se ha guardado la tabla de multiplicar de {numero} en el archivo tabla-{numero}.txt")

def mostrar_tabla_multiplicar(numero):
    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10")
        return
    
    try:
        with open(f"tabla-{numero}.txt", "r") as file:
            contenido = file.read()
            print(contenido)
    except FileNotFoundError:
        print(f"No se encontró el archivo tabla-{numero}.txt")

def mostrar_linea_tabla_multiplicar(numero, linea):
    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10")
        return
    
    try:
        with open(f"tabla-{numero}.txt", "r") as file:
            lineas = file.readlines()
            if linea < 1 or linea > len(lineas):
                print("El número de línea no es válido")
                return
            linea_deseada = lineas[linea - 1]
            print(linea_deseada)
    except FileNotFoundError:
        print(f"No se encontró el archivo tabla-{numero}.txt")

def menu():
    while True:
        print("----- Menú -----")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de la tabla de multiplicar")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            guardar_tabla_multiplicar(numero)
        elif opcion == "2":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            mostrar_tabla_multiplicar(numero)
        elif opcion == "3":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            linea = int(input("Ingrese el número de línea: "))
            mostrar_linea_tabla_multiplicar(numero, linea)
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()
