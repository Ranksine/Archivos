class Pelicula:
    def __init__(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'Nombre: {self._nombre}'
