# escritura_csv_02.py
import pandas as pd

# Crear un DataFrame con los datos
datos = {
    "Mes": ["Enero", "Febrero", "Marzo"],
    "Luz": [120.5, 110.0, 130.7],
    "Agua": [45.3, 48.1, 42.8],
    "Internet": [30.2, 35.0, 32.0],
    "Comunidad": [50.0, 50.0, 50.0]
}
df = pd.DataFrame(datos)

# Escribir el DataFrame a un archivo CSV
df.to_csv("datos_pandas.csv", index=False, encoding="utf-8")
print("Archivo CSV creado con éxito.")
