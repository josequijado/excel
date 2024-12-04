# lectura_csv_01.py
import csv

# Leer datos de un archivo CSV
with open("datos.csv", mode="r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)
