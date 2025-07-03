from pydantic import BaseModel

class Category(BaseModel):
    """Clase que representa una categoría de la API de Platzi."""
    id: int
    name: str
    slug: str
    image: str
    creationAt: str
    updatedAt: str

class Product(BaseModel):
    """Clase que representa un producto de la API de Platzi."""
    id: int
    title: str
    slug: str
    price: float
    description: str
    category: Category
    image: list[str]
    creationAt: str
    updatedAt: str

class User(BaseModel):
    """Clase que representa un usuario de la API de Platzi."""
    id: int
    email: str
    password: str
    name: str
    role: str
    avatar: str
    creationAt: str
    updatedAt: str