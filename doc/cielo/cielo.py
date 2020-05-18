import random
from estrella import Estrella

class Cielo():
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.cielo = []
        for i in range(filas):
            self.cielo.append([])
            for j in range(columnas):
                self.cielo[i].append(" ")

    def poner_estrellas(self, cant_estrellas):
        for i in range(cant_estrellas):
            x = random.randint(0, self.columnas - 1)
            y = random.randint(0, self.filas - 1)

            estrella = Estrella(x, y)
            self.cielo[y][x] = estrella

    def mostrar(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                print(self.cielo[i][j], end="")
            print()