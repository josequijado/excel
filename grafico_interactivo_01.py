# grafico_interactivo_01.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons


class AnalisisVentasInteractivo:
    """
    Clase para analizar y visualizar ventas interactivamente usando numpy, pandas y matplotlib.
    """

    def __init__(self, datos):
        """
        Inicializa la clase con los datos de ventas.
        :param datos: Diccionario con datos de ventas.
        """
        self.datos = datos
        self.df = pd.DataFrame(datos)  # Convertir datos a un DataFrame de pandas
        self.promedios = None

    def calcular_promedios(self):
        """
        Calcula el promedio de ventas para cada producto utilizando numpy.
        """
        self.promedios = self.df.iloc[:, 1:].mean(axis=0).to_numpy()
        print("Promedios de ventas por producto:")
        print(self.promedios)

    def graficar_ventas(self):
        """
        Genera un gráfico interactivo de las ventas mensuales.
        """
        # Configurar el gráfico
        fig, ax = plt.subplots(figsize=(10, 6))
        plt.subplots_adjust(left=0.2)  # Espacio para el menú de opciones

        # Dibujar líneas para cada producto
        lineas = []
        for producto in self.df.columns[1:]:
            linea, = ax.plot(self.df["Mes"], self.df[producto], label=producto, lw=2)
            lineas.append(linea)

        # Etiquetas y leyenda
        ax.set_title("Ventas Mensuales por Producto", fontsize=16)
        ax.set_xlabel("Meses", fontsize=14)
        ax.set_ylabel("Ventas", fontsize=14)
        ax.legend(fontsize=12, loc="upper left")

        # Crear CheckButtons para activar/desactivar productos
        axcheck = plt.axes([0.01, 0.4, 0.15, 0.2], facecolor="lightgoldenrodyellow")
        check = CheckButtons(axcheck, self.df.columns[1:], [True] * len(self.df.columns[1:]))

        # Función de actualización interactiva
        def actualizar(label):
            index = list(self.df.columns[1:]).index(label)
            lineas[index].set_visible(not lineas[index].get_visible())
            plt.draw()

        check.on_clicked(actualizar)

        # Mostrar gráfico
        plt.show()


# Datos simulados de ventas
datos = {
    "Mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
    "Producto A": [120, 150, 170, 130, 160, 175],
    "Producto B": [80, 90, 100, 95, 85, 110],
    "Producto C": [200, 220, 210, 230, 240, 250]
}

# Crear instancia de la clase y ejecutar análisis
analisis = AnalisisVentasInteractivo(datos)
analisis.calcular_promedios()
analisis.graficar_ventas()
