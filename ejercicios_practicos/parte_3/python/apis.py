import requests
from schemas import Category, Product, User
class PlatziAPI:
    """Clase para interactuar con la API de Platzi."""
    def __init__(self)->None:
        """Función constructora que inicializa la URL base de la API."""
        self.BASE_URL = "https://api.escuelajs.co/api/v1"
        self.HEADERS = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        self.ENDPOINTS = {
            "categories": f"{self.BASE_URL}/categories",
            "products": f"{self.BASE_URL}/products",
            "users": f"{self.BASE_URL}/users"
        }
        self.products = []
        self.users = []
        self.categories = []
    @classmethod
    async def crear_platzi_api(cls)-> "PlatziAPI":
        """Método de clase para crear una instancia de PlatziAPI."""
        instance = cls()
        return instance
    
    async def get_categories(self)-> None:
        """Obtiene todas las categorías de la API."""
        try:
            response = requests.get(self.ENDPOINTS["categories"], headers=self.HEADERS)
        except requests.RequestException as e:
            print(f"Error al obtener categorías: {e}")
            return None
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None
        if response.status_code == 200:
            data = response.json()
            for category in data:
                self.categories.append(
                    Category(
                        id=category["id"],
                        name=category["name"],
                        slug=category["slug"],
                        image=category["image"],
                        creationAt=category["creationAt"],
                        updatedAt=category["updatedAt"]
                    )
                )
        else:
            response.raise_for_status()
            print(f"Error al obtener categorías: {response.status_code} - {response.text}")
    
    async def get_products(self)-> None:
        """Obtiene todos los productos de la API."""
        try:
            response = requests.get(self.ENDPOINTS["products"], headers=self.HEADERS)
        except requests.RequestException as e:
            print(f"Error al obtener productos: {e}")
            return None
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None
        if response.status_code == 200:
            data = response.json()
            for product in data:
                category = product.get("category", {})
                if category["id"] not in self.categories:
                    # Si la categoría no está en la lista de categorías,
                    # agregarla a la lista de categorías
                    self.categories.append(
                        Category(
                            id=category["id"],
                            name=category["name"],
                            slug=category["slug"],
                            image=category["image"],
                            creationAt=category["creationAt"],
                            updatedAt=category["updatedAt"]
                        )
                    )
                # Buscar la categoría en la lista de categorías
                # utilizando el ID de la categoría del producto
                category_obj = next(
                    (cat for cat in self.categories if cat.id == category["id"]), None
                )
                # Comprobar si la categoría existe
                # y si no, continuar con el siguiente producto
                if not category_obj:
                    continue
                # Agregar el producto a la lista de productos
                # utilizando la categoría encontrada
                self.products.append(
                    Product(
                        id=product["id"],
                        title=product["title"],
                        slug=product["slug"],
                        price=product["price"],
                        description=product["description"],
                        category=category_obj,
                        image=product["images"],
                        creationAt=product["creationAt"],
                        updatedAt=product["updatedAt"]
                    )
                )
        else:
            response.raise_for_status()
            print(f"Error al obtener productos: {response.status_code} - {response.text}")
    
    async def get_users(self)-> None:
        """Obtiene todos los usuarios de la API."""
        try:
            response = requests.get(self.ENDPOINTS["users"], headers=self.HEADERS)
        except requests.RequestException as e:
            print(f"Error al obtener usuarios: {e}")
            return None
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None
        if response.status_code == 200:
            data = response.json()
            for user in data:
                self.users.append(
                    User(
                        id=user["id"],
                        email=user["email"],
                        password=user["password"],
                        name=user["name"],
                        role=user["role"],
                        avatar=user["avatar"],
                        creationAt=user["creationAt"],
                        updatedAt=user["updatedAt"]
                    )
                )
        else:
            response.raise_for_status()
            print(f"Error al obtener usuarios: {response.status_code} - {response.text}")


    def print_data(self):
        """Imprime los datos obtenidos de la API."""

        if not self.categories:
            print("No se han encontrado categorías.")
        else:
            print("Categorías:")
            for category in self.categories:
                print(f"- {category.name} (ID: {category.id})")
        
        if not self.products:
            print("No se han encontrado productos.")
        else:
            print("Productos:")
            for product in self.products:
                print(f"- {product.title} (ID: {product.id}, Precio: {product.price})")

        if not self.users:
            print("No se han encontrado usuarios.")
        else:
            print("Usuarios:")
            for user in self.users:
                print(f"- {user.name} (ID: {user.id}, Email: {user.email})")