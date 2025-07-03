import asyncio
from apis import PlatziAPI


def run_async(func):
    """Función para ejecutar funciones asíncronas en un entorno síncrono."""
    def wrapper(*args, **kwargs):
        return asyncio.run(func(*args, **kwargs))
    return wrapper

if __name__ == "__main__":
    # Crea una instancia de PlatziAPI de forma asíncrona
    platzi_api = None
    try:
        # Ejecuta la función asíncrona para crear la instancia de PlatziAPI
        platzi_api = run_async(PlatziAPI.crear_platzi_api)()
    except Exception as e:
        print(f"Error al crear la instancia de PlatziAPI: {e}")
        exit(1)
    # Obtiene las categoríasm productos y usuarios de forma asíncrona
    if platzi_api:
        try:
            run_async(platzi_api.get_categories)()
            run_async(platzi_api.get_products)()
            run_async(platzi_api.get_users)()
        except Exception as e:
            print(f"Error al obtener datos de PlatziAPI: {e}")
    else:
        print("No se pudo crear la instancia de PlatziAPI.")
    # Utilizar la función para imprimir los datos obtenidos
    if platzi_api:
        print("Categorías:")
        for category in platzi_api.categories:
            print(category)
        print("\nProductos:")
        for product in platzi_api.products:
            print(product)
        print("\nUsuarios:")
        for user in platzi_api.users:
            print(user)