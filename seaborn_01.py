# seaborn_01.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns


class Analisis3D:
    """
    Clase para manejar datos y generar visualizaciones 3D interactivas utilizando pandas, numpy, matplotlib y seaborn.
    """

    def __init__(self, num_puntos=100):
        """
        Inicializa la clase generando un conjunto de datos simulados.
        :param num_puntos: Número de puntos a generar en el conjunto de datos.
        """
        self.num_puntos = num_puntos
        self.datos = None

    def generar_datos(self):
        """
        Genera datos aleatorios simulados y los organiza en un DataFrame de pandas.
        """
        # Crear datos aleatorios para las variables X, Y y Z
        x = np.random.uniform(0, 10, self.num_puntos)
        y = np.random.uniform(0, 20, self.num_puntos)
        z = 2 * x + y + np.random.normal(scale=5, size=self.num_puntos)  # Relación no lineal con ruido

        # Crear un DataFrame con pandas
        self.datos = pd.DataFrame({
            "X": x,
            "Y": y,
            "Z": z
        })

        print("Datos generados:")
        print(self.datos.head())  # Mostrar las primeras filas como verificación

    def calcular_estadisticas(self):
        """
        Calcula estadísticas descriptivas básicas para las variables.
        """
        if self.datos is None:
            raise ValueError("Los datos no han sido generados. Llama a 'generar_datos' primero.")

        # Estadísticas básicas con pandas
        estadisticas = self.datos.describe()
        print("\nEstadísticas descriptivas:")
        print(estadisticas)

        # Cálculo adicional con numpy
        correlacion = np.corrcoef(self.datos["X"], self.datos["Z"])[0, 1]
        print(f"\nCorrelación entre X y Z: {correlacion:.2f}")

    def graficar_3d(self):
        """
        Genera un gráfico de dispersión 3D con matplotlib y aplica estética de seaborn.
        """
        if self.datos is None:
            raise ValueError("Los datos no han sido generados. Llama a 'generar_datos' primero.")

        # Configurar la estética de seaborn
        sns.set(style="whitegrid", palette="muted")

        # Crear figura y eje 3D
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection="3d")

        # Dibujar puntos 3D
        scatter = ax.scatter(
            self.datos["X"], self.datos["Y"], self.datos["Z"],
            c=self.datos["Z"], cmap="coolwarm", s=50, alpha=0.8
        )

        # Etiquetas y título
        ax.set_title("Gráfico 3D de Variables X, Y y Z", fontsize=16)
        ax.set_xlabel("X", fontsize=14)
        ax.set_ylabel("Y", fontsize=14)
        ax.set_zlabel("Z", fontsize=14)

        # Barra de colores para representar la magnitud de Z
        cbar = fig.colorbar(scatter, ax=ax, shrink=0.5)
        cbar.set_label("Magnitud de Z", fontsize=12)

        # Mostrar gráfico
        plt.show()


# Ejecución del análisis
if __name__ == "__main__":
    # Crear una instancia de la clase
    analisis = Analisis3D(num_puntos=200)

    # Generar datos
    analisis.generar_datos()

    # Calcular estadísticas descriptivas
    analisis.calcular_estadisticas()

    # Generar un gráfico 3D interactivo
    analisis.graficar_3d()
