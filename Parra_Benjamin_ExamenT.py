#Validaciones Particulares Una a Una
def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_autor(autor):
    return autor.strip() != ""

def validar_genero(genero):
    return genero.strip() != ""

def validar_año(año):
    return año > 0

def validar_editorial(editorial):
    return editorial.strip() != ""

def validar_codigo(codigo):
    return codigo.strip() != ""

def validar_multa(multa):
    return multa > 0

def validar_copias_disponibles(copias):
    return copias > 0

def mostrar_menu():
    print("")

def leer_opcion():
    while True:
        try:
            opcion = int(input(""))
            if 1 < opcion < 6:
                return opcion
            print("Opcion fuera del rango")
        except ValueError:
            print("Error: Ingrese opcion numerica")

def agregar_libro(libros,codigo,titulo,autor,genero,año,editorial,multa,copias):
    codigo = input("Ingrese el codigo del libro: ")
    if not validar_codigo(codigo):
        print("El codigo no puede estar vacio, tiene que ser un valor alfanumerico")
        return
    
    try:
        titulo = input("Ingrese el titulo: ")
    except ValueError:
        print("Error: Ingrese un titulo no espacios en blanco")
        return
    if not validar_titulo(titulo):
        print("Error: No deje la entrada vacia")
        return
    
    try:
        autor = input("Ingrese autor: ")
    except ValueError:
        print("Error: Ingrese autor sin espacios en blanco")
        return
    if not validar_autor(autor):
        print("Error: No deje la entrada vacia")
        return
    
    try:
        genero = input("Ingrese genero: ")
    except ValueError:
        print("Error: Ingrese un genero sin espacios en blanco")
        return
    if not validar_genero(genero):
        print("Error: No deje la entrada vacia")
        return

    try:
        año = int(input("Ingrese año de publicacion: "))
    except ValueError:
        print("Error: Ingrese solo valores numericos")
        return
    if not validar_año(año):
        print("Error: Tiene que ser un numero entero mayor que cero")
        return
    
    try:
        editorial = input("Ingrese editorial: ")
    except ValueError:
        print("Error: Ingrese la editorial no espacios en blanco")
        return
    if not validar_editorial(editorial):
        print("Error: No deje la entrada vacia")
        return
    
    try:
        multa = int(input("Ingrese precio de multa: "))
    except ValueError:
        print("Error: Ingrese solo valores numericos")
        return
    if not validar_multa(multa):
        print("Error: Tiene que ser un numero entero mayor que cero")
        return
    
    try:
        copias = int(input("Ingrese copias disponibles: "))
    except ValueError:
        print("Error: Ingrese solo valores numericos")
        return
    if not validar_copias_disponibles(copias):
        print("Error: Tiene que ser un numero entero mayor que cero")
        return
    
    libro = {
        "titulo":titulo.strip(),
        "autor":autor.strip(),
        "genero":genero.strip(),
        "año":año,
        "editorial":editorial.strip(),
        "multa":multa,
        "novedad": False,
        "copias":copias
    }
    libros.append(libro)
    print("Libro Agregado")

def busqueda_libro(libros, multa):
    for i, libro in enumerate(libros):
        if libro["multa"] == multa:
            return  i
    return -1

def busqueda_genero(libros, genero):
    for i, libro in enumerate(libros):
        if libro["genero"] == genero:
            return i
    return -1

def eliminar_libro(libros, codigo):
    posicion = busqueda_libro(libros, codigo)
    if posicion != -1:
        libros.pop(posicion)
        print(f"Libro {codigo} eliminado correctamente del registro")
    else:
        print(f"Libro {codigo} no se encuentra registrado")
    
def actualizar_estado_libros(libros):
    for libro in libros:
        if libro["novedad"] == "s":
            libros["novedad"] = True
        else:
            libro["novedad"] = False

def despedida():
    print("Programa Finalizado")

def main():
    libros = []

    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            genero = input("Ingrese el genero a consultar: ")
            posicion = busqueda_genero(genero)
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