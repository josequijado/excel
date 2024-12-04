# numpy_y_pandas_01.py
import pandas as pd
import numpy as np


class AnalisisFinanciero:
    """
    Clase para realizar análisis financiero de ventas utilizando pandas y numpy.
    """

    def __init__(self, archivo_csv):
        """
        Inicializa la clase cargando los datos desde un archivo CSV.
        :param archivo_csv: Ruta del archivo CSV con los datos de ventas.
        """
        self.archivo_csv = archivo_csv
        self.datos = None
        self.estadisticas = None

    def cargar_datos(self):
        """
        Carga los datos desde el archivo CSV en un DataFrame de pandas.
        """
        self.datos = pd.read_csv(self.archivo_csv)
        print(f"Datos cargados con éxito desde '{self.archivo_csv}':\n")
        print(self.datos.head())  # Mostrar las primeras filas para verificar

    def calcular_estadisticas(self):
        """
        Calcula estadísticas clave de las ventas utilizando numpy.
        """
        if self.datos is None:
            raise ValueError("Los datos no han sido cargados. Llama a 'cargar_datos' primero.")

        # Calcular promedio y desviación estándar para cada producto
        promedios = self.datos.iloc[:, 1:].mean(axis=0).to_numpy()  # Promedio por columna
        desv_std = self.datos.iloc[:, 1:].std(axis=0).to_numpy()  # Desviación estándar por columna

        # Calcular el promedio global (todas las celdas excepto la columna de meses)
        promedio_global = np.mean(self.datos.iloc[:, 1:].to_numpy())

        # Identificar productos con ventas superiores al promedio global
        superiores_promedio = self.datos.iloc[:, 1:].mean(axis=0) > promedio_global

        # Crear un DataFrame con las estadísticas
        self.estadisticas = pd.DataFrame({
            "Producto": self.datos.columns[1:],
            "Promedio": promedios,
            "Desv. Estándar": desv_std,
            "Superior al Promedio Global": superiores_promedio
        })

        print("\nEstadísticas calculadas:\n")
        print(self.estadisticas)

    def exportar_estadisticas(self, archivo_salida):
        """
        Exporta las estadísticas calculadas a un archivo CSV.
        :param archivo_salida: Nombre del archivo CSV donde se guardarán las estadísticas.
        """
        if self.estadisticas is None:
            raise ValueError("Las estadísticas no han sido calculadas. Llama a 'calcular_estadisticas' primero.")

        self.estadisticas.to_csv(archivo_salida, index=False, encoding="utf-8")
        print(f"\nEstadísticas exportadas con éxito a '{archivo_salida}'.")


# Ejecución del análisis
if __name__ == "__main__":
    # Crear datos simulados en un archivo CSV
    datos = {
        "Mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
        "Producto A": [120, 150, 170, 130, 160, 175],
        "Producto B": [80, 90, 100, 95, 85, 110],
        "Producto C": [200, 220, 210, 230, 240, 250]
    }

    # Guardar datos simulados en un archivo
    archivo_entrada = "ventas.csv"
    pd.DataFrame(datos).to_csv(archivo_entrada, index=False)

    # Instanciar la clase y realizar el análisis
    analisis = AnalisisFinanciero(archivo_entrada)
    analisis.cargar_datos()
    analisis.calcular_estadisticas()
    analisis.exportar_estadisticas("estadisticas_ventas.csv")
