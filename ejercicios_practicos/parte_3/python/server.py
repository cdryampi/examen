from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from dotenv import load_dotenv
from apis import PlatziAPI
import os
import asyncio


load_dotenv()

app = FastAPI()

# Para servir archivos estáticos como CSS, imágenes, etc.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar motor de plantillas
templates = Jinja2Templates(directory="templates")

# Global variable to store the API instance
platzi_api = None

@app.on_event("startup")
async def startup_event():
    """Initialize PlatziAPI when the FastAPI app starts."""
    global platzi_api
    try:
        # Create the PlatziAPI instance asynchronously
        platzi_api = await PlatziAPI.crear_platzi_api()
        
        # Load data asynchronously
        await platzi_api.get_categories()
        await platzi_api.get_products()
        await platzi_api.get_users()
        
        print("PlatziAPI initialized successfully")
    except Exception as e:
        print(f"Error al crear la instancia de PlatziAPI: {e}")
        # Don't exit here, let the app start but handle the None case in routes

# Manejador de errores 404
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return templates.TemplateResponse("error.html", 
            {"request": request, "message": "Página no encontrada (404)."}, 
            status_code=404)
    return templates.TemplateResponse("error.html", 
        {"request": request, "message": f"Error {exc.status_code}: {exc.detail}"}, 
        status_code=exc.status_code)

# Manejador de errores de validación
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return templates.TemplateResponse("error.html", 
        {"request": request, "message": "Error de validación en la solicitud."}, 
        status_code=422)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Ruta principal que renderiza la plantilla HTML."""
    api_key = os.getenv("API_KEY")
    return templates.TemplateResponse("index.html", {"request": request, "api_key": api_key})

@app.get("/users", response_class=HTMLResponse)
async def get_users(request: Request):
    """Ruta para obtener los usuarios de PlatziAPI."""
    if not platzi_api:
        return templates.TemplateResponse("error.html", {"request": request, "message": "API no disponible."})
    
    users = platzi_api.get_list_users()
    if not users:
        return templates.TemplateResponse("error.html", {"request": request, "message": "No se encontraron usuarios."})
    
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/categories", response_class=HTMLResponse)
async def get_categories(request: Request):
    """Ruta para obtener las categorías de PlatziAPI."""
    if not platzi_api:
        return templates.TemplateResponse("error.html", {"request": request, "message": "API no disponible."})
    
    categories = platzi_api.get_list_categories()
    if not categories:
        return templates.TemplateResponse("error.html", {"request": request, "message": "No se encontraron categorías."})
    
    return templates.TemplateResponse("categories.html", {"request": request, "categories": categories})

@app.get("/products", response_class=HTMLResponse)
async def get_products(request: Request):
    """Ruta para obtener los productos de PlatziAPI."""
    if not platzi_api:
        return templates.TemplateResponse("error.html", {"request": request, "message": "API no disponible."})
    
    products = platzi_api.get_list_products()
    if not products:
        return templates.TemplateResponse("error.html", {"request": request, "message": "No se encontraron productos."})
    
    return templates.TemplateResponse("products.html", {"request": request, "products": products})

# Ruta de errores personalizada (opcional)
@app.get("/error", response_class=HTMLResponse)
async def error_page(request: Request):
    """Ruta para mostrar una página de error personalizada."""
    return templates.TemplateResponse("error.html", {"request": request, "message": "Página de error personalizada."})

