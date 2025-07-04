# Resumen del ejercicio práctico - Parte 3 Python

## Descripción del proyecto:
En este ejercicio práctico, necesitamos consumir la **API REST de Platzi** (Fake Store API) y procesar los datos usando **Python** con **requests** y **Pydantic**.

## Funcionalidad principal:
- Hacemos **peticiones HTTP** a la API de Platzi usando `requests`
- Guardamos en **listas** el resultado de los endpoints: `products`, `categories` y `users`
- Validamos los datos usando **modelos Pydantic** para garantizar la integridad
- Con `print_data()` mostramos por consola los datos procesados de cada endpoint

## Estructura del código:
- **`schemas.py`**: Define los modelos Pydantic (`Category`, `Product`, `User`)
- **`apis.py`**: Contiene la clase `PlatziAPI` con métodos asíncronos para consumir la API
- **`main.py`**: Función principal que ejecuta todo el proceso de obtener y mostrar datos
- **`requirements.txt`**: Dependencias necesarias (requests, pydantic, etc.)

## Flujo de ejecución:
Al final tenemos una función `main` que ejecuta todo el proceso de:
1. Crear instancia de `PlatziAPI` 
2. Obtener los datos de forma **asíncrona** con `await`
3. Validar datos con **Pydantic**
4. Mostrar resultados por consola
5. Manejar errores con `try/catch`

## Tecnologías utilizadas:
- ✅ **Python** con programación asíncrona (`async/await`)
- ✅ **Requests** para peticiones HTTP
- ✅ **Pydantic** para validación de datos
- ✅ **Manejo de errores** robusto

**Nota**: Asegúrate de instalar las dependencias con `pip install -r requirements.txt`
**MotivBot**: Puedes utilizarlo para realizar modificaciones en el código y pedirle explicaciones sobre el mismo.

## Modo web para poder ver los resultados de la API de Platzi:
- Puedes iniciarla con el comando `uvicorn server:app --reload` y acceder a la documentación interactiva en `http://localhost:8000/`.