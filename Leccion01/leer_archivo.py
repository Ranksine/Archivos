try:
    archivo = open('prueba.txt', 'r', encoding='utf8')
    # Se puede especificar la ruta completa del archivo, o cualquier ruta inferior a la carpeta raiz del proyecto
    # archivo = open('C:\\Users\\Usuario\\Desktop\\Cursos\\Python\\Archivos\\Leccion01\\prueba.txt', 'r', encoding='utf8')
    # print(archivo.read())

    # Leer algunos caracteres
    # print(archivo.read(5))
    # print(archivo.read(3))

    # Leer lineas compleatas
    # print(archivo.readline())
    # print(archivo.readline())

    # Iterar el archivo
    # for linea in archivo:
    #     print(linea)

    # Leer lineas
    # print(archivo.readlines())

    # Acceder a una linea de la lista
    # print(archivo.readlines()[2])

    #Abrir un nuevo archivo
    # a = anexar informacion
    archivo2 = open('copia.txt', 'a', encoding='utf8')
    archivo2.write(archivo.read())
    archivo2.close()
    archivo.close()
    print('Se ha terminado el proceso de leer y copiar archivos')

except Exception as e:
    print('error:', e)
finally:
    archivo.close()