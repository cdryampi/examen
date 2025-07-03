from pydantic import BaseModel
# Modelo para leer el JSON de entrada

class Alumno(BaseModel):
    nombre: str
    nota: float
    def __str__(self):
        # Método para representar el objeto como una cadena
        return f"{self.nombre} - {self.nota}"