# escritura_csv_01.py
import csv

# Datos a escribir
datos = [
    ["Mes", "Luz", "Agua", "Internet", "Comunidad"],
    ["Enero", 120.5, 45.3, 30.2, 50.0],
    ["Febrero", 110.0, 48.1, 35.0, 50.0],
    ["Marzo", 130.7, 42.8, 32.0, 50.0]
]

# Escribir datos en un archivo CSV
with open("datos.csv", mode="w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datos)

print("Archivo CSV creado con éxito.")
