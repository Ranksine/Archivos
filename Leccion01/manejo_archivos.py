try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('Agregamos información al archivo\n')
    archivo.write('Adios le pido')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    archivo.close()
    print('Fin del archivo')
    # archivo.write('holis')