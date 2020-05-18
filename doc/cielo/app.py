import os
import sys
from cielo import Cielo


os.system("clear")
# python3 app.py 30 120 300

filas = int(sys.argv[1])
columnas = int(sys.argv[2])
estrellas = int(sys.argv[3])

cielo_1 = Cielo(filas, columnas)
cielo_1.poner_estrellas(estrellas)
cielo_1.mostrar()
