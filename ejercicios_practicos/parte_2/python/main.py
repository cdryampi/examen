import asyncio
from schema import Alumno
from clasificar import Clasificar

def run_async(func):
    """Función para ejecutar funciones asíncronas en un entorno síncrono."""
    def wrapper(*args, **kwargs):
        return asyncio.run(func(*args, **kwargs))
    return wrapper
if __name__ == "__main__":
    # Crea una instancia de Clasificar de forma asíncrona
    clasificar = None
    try:
        # Ejecuta la función asíncrona para crear la instancia de Clasificar
        clasificar = run_async(Clasificar.crear_clasificar)()
    except Exception as e:
        print(f"Error al crear la instancia de Clasificar: {e}")
        exit(1)
    # Recorre la lista de alumnos y los imprime
    if clasificar:
        try:
            print("Nota media:")
            print(f"{clasificar.media:.2f}")
            print("---------------------------------")
            print("Lista de alumnos a aprovados:")
            print("---------------------------------")
            for alumno in clasificar.obtener_aprobados():
                print(alumno)
        except Exception as e:
            print(f"Error al imprimir la lista de alumnos: {e}")
    else:
        print("No se pudo crear la instancia de Clasificar.")
