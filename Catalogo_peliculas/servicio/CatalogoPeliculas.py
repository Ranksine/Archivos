from dominio.Pelicula import Pelicula
import os
class CatalogoPeliculas:

    @staticmethod
    def ruta_archivo(nombre):
        return nombre

    @staticmethod
    def agregar_pelicula(Pelicula):
        with open('peliculas.txt', 'a', encoding='utf8') as archivo_pelis:
            archivo_pelis.write(Pelicula + '\n')
            print(f'Se ha agregado la pelicula "{Pelicula}" al catálogo')

    @staticmethod
    def listar_peliculas():
        try:
            listado = open('peliculas.txt', 'r', encoding='utf8')
            print('Peliculas listadas'.center(60, '*'))
            print(listado.read())
            print(''.center(60, '*'))
            listado.close()
        except Exception as e:
            print('Ha ocurrido un error al intentar leer el archivo de catalogo: ', e)


    @staticmethod
    def eliminar_peliculas():
        try:
            os.remove('peliculas.txt')
            print('Archivo eliminado correctamente')
        except Exception as e:
            print('Ha ocurrido un error al eliminar el archivo')
