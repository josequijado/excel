# gastos_mensuales_01.py
import random
from openpyxl import Workbook

class GastosMensuales:
    """
    Clase que gestiona los gastos mensuales y genera un archivo Excel con los datos.
    """

    def __init__(self):
        """
        Inicializa los datos de los meses y las partidas de gastos.
        """
        self.meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
        self.partidas = ["Luz", "Agua", "Internet", "Comunidad"]
        self.datos = self._generar_datos()

    def _generar_datos(self):
        """
        Genera datos aleatorios para cada mes y cada partida de gastos.
        :return: Lista de listas con los datos generados.
        """
        return [[random.randint(50, 200) for _ in self.partidas] for _ in self.meses]

    def _calcular_totales(self):
        """
        Calcula los totales por columna y el total general.
        :return: Tupla con (totales_por_columna, total_general).
        """
        totales_por_columna = [sum(col) for col in zip(*self.datos)]
        total_general = sum(totales_por_columna)
        return totales_por_columna, total_general

    def generar_excel(self, nombre_archivo="gastos_mensuales_01.xlsx"):
        """
        Genera un archivo Excel con los datos y totales de gastos.
        :param nombre_archivo: Nombre del archivo Excel a generar.
        """
        wb = Workbook()
        ws = wb.active
        ws.title = "Gastos Mensuales"

        # Escribir encabezados
        ws.append(["Mes"] + self.partidas)

        # Escribir datos
        for i, mes in enumerate(self.meses):
            ws.append([mes] + self.datos[i])

        # Escribir totales
        totales, total_general = self._calcular_totales()
        ws.append(["Total"] + totales + [total_general])

        # Guardar archivo
        wb.save(nombre_archivo)
        print(f"Archivo Excel generado: {nombre_archivo}")


# Ejecución del script
if __name__ == "__main__":
    gastos = GastosMensuales()
    gastos.generar_excel()
