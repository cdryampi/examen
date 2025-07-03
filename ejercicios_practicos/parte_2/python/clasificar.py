import pathlib
import json
import asyncio
from schema import Alumno
class Clasificar():
    # Clase que representa todo el proceso de clasificación de alumnos
    def __init__(self)-> None:
        # Inicializa la lista de alumnos
        self.alumnos = []
        self.media = 0.0
    @classmethod
    async def crear_clasificar(cls)-> "Clasificar":
        # Método de clase para crear una instancia de Clasificar
        instance = cls()
        await instance.leer_alumnos()
        instance.calcular_media()
        # Si no hay alumnos, lanza una excepción
        if not instance.alumnos:
            raise ValueError("No se han encontrado alumnos en el fichero JSON.")
        return instance
    
    async def agregar_alumno(self, alumno):
        # Método para agregar un alumno a la lista
        self.alumnos.append(Alumno(nombre=alumno['nombre'], nota=alumno['nota']))

    async def leer_alumnos(self)-> None:
        # Método para leer los alumnos desde un JSON
        json_url = await self.obeter_url_absoluta()
        alumnos_json = []
        # Abre el fichero JSON y lo carga
        try:
            with open(json_url, "r", encoding="utf-8") as f:
                # Carga el contenido del fichero JSON
                alumnos_json = json.load(f)
        except FileNotFoundError:
            print(f"El fichero {json_url} no se ha encontrado.")
            return
        except json.JSONDecodeError:
            print(f"Error al decodificar el fichero JSON {json_url}.")
            return
        except Exception as e:
            print(f"Se ha producido un error inesperado: {e}")
            return
        # Recorre la lista de alumnos y los agrega a la lista de alumnos
        for alumno in alumnos_json:
            await self.agregar_alumno(alumno)

    async def obeter_url_absoluta(self)-> pathlib.Path:
        # El fichero JSON esta en la misma carpeta del script y # se llama alumnos.json
        ruta_relativa = pathlib.Path(__file__).parent / "alumnos.json"
        # Devuelve la ruta absoluta del fichero
        return ruta_relativa.resolve()
    def calcular_media(self)->None:
        # Método para calcular la media de las notas de los alumnos
        if not self.alumnos:
            return
        total = sum(alumno.nota for alumno in self.alumnos)
        self.media = total / len(self.alumnos)
    def obtener_aprobados(self)-> list:
        # Método para obtener la lista de alumnos aprobados
        return [alumno for alumno in self.alumnos if alumno.nota >= self.media]
    def __str__(self):
        # Método para representar la instancia de Clasificar como una cadena
        return "\n".join(str(alumno) for alumno in self.alumnos)