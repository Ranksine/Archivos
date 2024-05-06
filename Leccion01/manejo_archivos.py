try:
    archivo = open('prueba.txt', 'w')
    archivo.write('Agregamos informacion al archivo\n')
    archivo.write('Adios le pido')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    archivo.close()