from servicio import CatalogoPeliculas

opcion = 0
catalogo = CatalogoPeliculas
while opcion < 4:
    print('Catálago de películas'.center(50, '-'))
    print('1. Agregar película')
    print('2. Listar películas')
    print('3. Eliminar archivo de películas')
    print('4. Salirs')
    opcion = int(input('Elige una opción (1-4): '))

    if opcion == 1:
        nombre = input('Ingresa el nombre de la pelicula: ')
        catalogo.CatalogoPeliculas.agregar_pelicula(nombre)

    elif opcion == 2:
        catalogo.CatalogoPeliculas.listar_peliculas()

    elif opcion == 3:
        respuesta = input('Seguro que quieres eliminar el catalogo? (S = si / N = no): ')
        if respuesta == 'S':
            catalogo.CatalogoPeliculas.eliminar_peliculas()
            print()

    else:
        print('Adiosito mi programador precioso, tecueme')