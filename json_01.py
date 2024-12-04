# json_01.py
import json

class GestorJSON:
    """
    Clase para gestionar operaciones con archivos JSON utilizando la librería json de Python.
    Proporciona métodos para leer, escribir, y manipular datos JSON.
    """

    def __init__(self, archivo=None):
        """
        Inicializa la clase con la ruta del archivo JSON.
        :param archivo: Nombre del archivo JSON para leer/escribir datos.
        """
        self.archivo = archivo
        self.datos = None

    def cargar_desde_archivo(self):
        """
        Carga datos desde un archivo JSON al atributo 'datos'.
        :raises FileNotFoundError: Si el archivo no existe.
        """
        if not self.archivo:
            raise ValueError("No se ha especificado un archivo JSON.")
        try:
            with open(self.archivo, "r") as f:
                self.datos = json.load(f)
            print(f"Datos cargados desde '{self.archivo}':")
            print(json.dumps(self.datos, indent=4))
        except FileNotFoundError:
            print(f"Error: El archivo '{self.archivo}' no existe.")
    
    def guardar_a_archivo(self, datos, indent=4):
        """
        Guarda los datos proporcionados en el archivo JSON especificado.
        :param datos: Estructura de datos de Python a guardar en el archivo.
        :param indent: Nivel de indentación para el archivo JSON.
        """
        if not self.archivo:
            raise ValueError("No se ha especificado un archivo JSON.")
        with open(self.archivo, "w") as f:
            json.dump(datos, f, indent=indent)
        print(f"Datos guardados en '{self.archivo}'.")

    def cargar_desde_cadena(self, cadena_json):
        """
        Carga datos desde una cadena JSON.
        :param cadena_json: Cadena con formato JSON.
        """
        try:
            self.datos = json.loads(cadena_json)
            print("Datos cargados desde la cadena JSON:")
            print(json.dumps(self.datos, indent=4))
        except json.JSONDecodeError as e:
            print(f"Error al cargar JSON: {e}")

    def convertir_a_cadena(self, datos, indent=4):
        """
        Convierte una estructura de datos de Python a una cadena JSON.
        :param datos: Estructura de datos de Python a convertir.
        :param indent: Nivel de indentación para la salida JSON.
        :return: Cadena JSON generada.
        """
        try:
            cadena_json = json.dumps(datos, indent=indent)
            print("Estructura convertida a cadena JSON:")
            print(cadena_json)
            return cadena_json
        except TypeError as e:
            print(f"Error al convertir a JSON: {e}")

    def mostrar_datos(self):
        """
        Imprime los datos cargados en formato JSON con indentación.
        """
        if self.datos is None:
            print("No hay datos cargados.")
        else:
            print("Datos actuales:")
            print(json.dumps(self.datos, indent=4))

    def agregar_dato(self, clave, valor):
        """
        Agrega un nuevo par clave-valor a los datos cargados.
        :param clave: Clave para el nuevo dato.
        :param valor: Valor asociado a la clave.
        """
        if self.datos is None:
            self.datos = {}
        self.datos[clave] = valor
        print(f"Se agregó el dato: {clave} -> {valor}")

    def eliminar_dato(self, clave):
        """
        Elimina un dato de los datos cargados basado en su clave.
        :param clave: Clave del dato a eliminar.
        """
        if self.datos is None or clave not in self.datos:
            print(f"No se encontró la clave '{clave}' en los datos.")
        else:
            del self.datos[clave]
            print(f"Se eliminó el dato con clave '{clave}'.")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de la clase
    gestor = GestorJSON("datos.json")

    # Datos iniciales
    datos_iniciales = {
        "nombre": "Juan",
        "edad": 30,
        "ciudad": "Madrid",
        "hobbies": ["lectura", "ciclismo", "ajedrez"]
    }

    # Guardar los datos iniciales en el archivo JSON
    gestor.guardar_a_archivo(datos_iniciales)

    # Cargar datos desde el archivo
    gestor.cargar_desde_archivo()

    # Agregar un nuevo dato
    gestor.agregar_dato("profesion", "Ingeniero")

    # Mostrar los datos actuales
    gestor.mostrar_datos()

    # Guardar los cambios en el archivo
    gestor.guardar_a_archivo(gestor.datos)

    # Eliminar un dato
    gestor.eliminar_dato("edad")

    # Mostrar los datos actuales
    gestor.mostrar_datos()

    # Convertir a cadena JSON
    cadena_json = gestor.convertir_a_cadena(gestor.datos)

    # Cargar desde una cadena JSON
    gestor.cargar_desde_cadena(cadena_json)
