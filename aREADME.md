# App de Instrumentos - FastAPI

Esta aplicación utiliza FastAPI para exponer una API RESTful simple que permite gestionar una colección de instrumentos musicales. Los usuarios pueden listar, crear, actualizar y eliminar instrumentos mediante solicitudes HTTP.

## Características

* **Endpoints CRUD** para gestionar instrumentos.
* **Autenticación y Autorización** (opcional).
* **Documentación Interactiva** generada automáticamente con Swagger UI.

## Requisitos

* Python 3.8+
* FastAPI
* Uvicorn (para servir la aplicación)

## Instalación

1. Clona el repositorio o descarga el código fuente.
2. Navega al directorio del proyecto en tu terminal.
3. Instala las dependencias con pip:

<pre><div class="mt-3 p-1"><div><code class="language-text"><span>pip install fastapi uvicorn pydantic
</span></code></div><div class="flex"><button class="btn btn-circle mt-n5" type="submit"><i class="fe fe-copy"></i></button><button class="btn btn-circle mt-n5" type="submit"><i class="fe fe-play"></i></button><a class="fw-bold fs-6 text-white mt-n1" target="_blank" href="https://www.phind.com/search?cache=j74vc9vol34cf7l8pwgqunhw" rel="noreferrer"><h6 class="text-always-white"></h6></a></div></div></pre>

## Ejecución

Para iniciar la aplicación, ejecuta el siguiente comando en tu terminal:

<pre><div class="mt-3 p-1"><div><code class="language-css"><span>uvicorn </span><span class="token">main</span><span class="token">:</span><span>app </span><span class="token">--reload</span><span>
</span></code></div><div class="flex"><button class="btn btn-circle mt-n5" type="submit"><i class="fe fe-copy"></i></button><button class="btn btn-circle mt-n5" type="submit"><i class="fe fe-play"></i></button><a class="fw-bold fs-6 text-white mt-n1" target="_blank" href="https://www.phind.com/search?cache=j74vc9vol34cf7l8pwgqunhw" rel="noreferrer"><h6 class="text-always-white"></h6></a></div></div></pre>

Esto iniciará la aplicación en modo de desarrollo con recarga automática. La API estará disponible en `http://localhost:8000`.

## Endpoints

### Obtener un Instrumento por ID

* **Método:** GET
* **Ruta:** `/instrument/{id}`
* **Descripción:** Obtiene los detalles de un instrumento por su ID.

### Obtener Todos los Instrumentos

* **Método:** GET
* **Ruta:** `/instruments/`
* **Descripción:** Obtiene una lista de todos los instrumentos disponibles.

### Crear un Nuevo Instrumento

* **Método:** POST
* **Ruta:** `/instruments`
* **Cuerpo de la solicitud:** JSON con los detalles del instrumento.
* **Descripción:** Crea un nuevo instrumento en la base de datos.

### Actualizar un Instrumento Existente

* **Método:** PUT
* **Ruta:** `/instruments/{instrument_id}`
* **Cuerpo de la solicitud:** JSON con los nuevos detalles del instrumento.
* **Descripción:** Actualiza un instrumento existente por su ID.

### Eliminar un Instrumento

* **Método:** DELETE
* **Ruta:** `/instruments/{instrument_id}`
* **Descripción:** Elimina un instrumento por su ID.

## Documentación

La documentación interactiva de la API está disponible en `http://localhost:8000/docs` después de iniciar la aplicación. Puedes probar los endpoints directamente desde la interfaz de usuario.

## Contribuciones

Las contribuciones son bienvenidas Por favor, abre un issue o haz un pull request con tus cambios.
