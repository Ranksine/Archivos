# with sustituye el bloque try en cuestion de que abre y cierra el archivo automaticamente
# with open('prueba.txt', 'r', encoding='utf8') as archivo:
#     print(archivo.read())
from ManejoArchivos import ManejoArchivos
with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())