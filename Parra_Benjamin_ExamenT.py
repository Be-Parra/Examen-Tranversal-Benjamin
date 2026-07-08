def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_autor(autor):
    return autor.strip() != ""

def validar_genero(genero):
    return genero.strip() != ""

def validar_año(año):
    try:
        val = int(año)
        return val > 0
    except ValueError:
        return False

def validar_editorial(editorial):
    return editorial.strip() != ""

def validar_codigo(codigo):
    return codigo.strip() != ""

def validar_es_novedad(es_novedad):
    return es_novedad.lower() in ['s', 'n']

def validar_multa(multa):
    try:
        val = int(multa)
        return val > 0
    except ValueError:
        return False

def validar_copias_disponibles(copias):
    try:
        val = int(copias)
        return val >= 0
    except ValueError:
        return False

def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===============")
    print("1. Copias por género")
    print("2. Búsqueda de libros por rango de multa")
    print("3. Actualizar multa de libro")
    print("4. Agregar libro")
    print("5. Eliminar libro")
    print("6. Salir")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                return opcion
            print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")

def copias_genero(libros, prestamos, genero):
    total = 0
    genero_lower = genero.lower()
    for cod, datos in libros.items():
        if datos[2].lower() == genero_lower:
            if cod in prestamos:
                total += prestamos[cod][1]
                print(f"El total de copias disponibles es: {total}")

def busqueda_multa(libros, prestamos, multa_min, multa_max):
    resultados = []
    for cod, datos_p in prestamos.items():
        multa = datos_p[0]
        copias = datos_p[1]
    if multa_min <= multa <= multa_max and copias > 0:
        if cod in libros:
            titulo = libros[cod][0]
            resultados.append(f"{titulo}--{cod}")
    if resultados:
        resultados.sort()
        print(f"Los libros encontrados son: {resultados}")
    else:
        print("No hay libros en ese rango de multa.")

def buscar_codigo(prestamos, codigo):
    for cod in prestamos.keys():
        if cod.lower() == codigo.lower():
            return True
    return False

def obtener_clave_exacta(prestamos, codigo):
    for cod in prestamos.keys():
        if cod.lower() == codigo.lower():
           return cod
    return codigo

def actualizar_multa(prestamos, codigo, nueva_multa):
    if buscar_codigo(prestamos, codigo):
        clave = obtener_clave_exacta(prestamos, codigo)
        prestamos[clave][0] = nueva_multa
        return True
    return False

def agregar_libro(libros, prestamos, codigo, titulo, autor, genero, año, editorial, es_novedad, precio_multa, copias_disponibles):
    if buscar_codigo(prestamos, codigo):
        return False
    novedad_bool = True if es_novedad.lower() == 's' else False
    libros[codigo] = [titulo, autor, genero, int(año), editorial, novedad_bool]
    prestamos[codigo] = [int(precio_multa), int(copias_disponibles)]
    return True

def eliminar_libro(libros, prestamos, codigo):
    if buscar_codigo(prestamos, codigo):
        clave = obtener_clave_exacta(prestamos, codigo)
        libros.pop(clave)
        prestamos.pop(clave)
        return True
    return False

def despedida():
    print("Fin del Programa")

def main():
    libros = {}
    prestamos = {}

    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            genero = input("Ingrese el genero a consultar: ")
            posicion = copias_genero(genero)
            if posicion != -1:
                g = genero[posicion]

        elif opcion == 2:
            multa_min = int(input("Ingrese multa minima: "))
            multa_max = int(input("Ingrese multa maxima: "))


        elif opcion == 3:
            codigo= input("Ingrese el codigo del libro: ")
            eliminar_libro(libros, codigo)
        
        elif opcion == 4:
            agregar_libro(libros)
            
        elif opcion == 6:
            despedida()
            break

if __name__ == "__main__":
    main()