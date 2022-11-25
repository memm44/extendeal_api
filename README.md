# extendeal_challenge
challenge of extendeal company

# Extendeal API
Proyecto construido con **[FastAPI](https://fastapi.tiangolo.com/)** como framework de desarrollo y **[Uvicorn](https://www.uvicorn.org/)** como servidor en combinación con Selenium para la extracción de datos.

# Pogramas necesarios para levantar el proyecto.
docker 

# Comando de levantamiento
con el servicio docker activo y situados en la carpeta donde se encuentra el archivo docker-compose.yml ejecutamos la linea:

`docker-compose up`

y se levantarán todos los servicios necesarios y solo restaria acceder a las rutas de la documentación para observar los endpoints.

# Credenciales

el archivo `.env` que almacena el usuario habilitado para consumir el endpoint serán enviadas via correo electronico

# Documentación  

La Api cuenta con una autenticación basica y las credenciales seran enviadas aparte para que puedan 
accionar el endpoint de `items` que es el que realiza el scrapping y devuelve los elementos de la pagina.
  
La API cuenta con un sistema de versionado provisto por [fastapi-versioning](https://github.com/DeanWay/fastapi-versioning).  
  
Al ejecutar la aplicación encontrará la documentación autogenerada en los siguientes links:  
   
[Extendeal API - ReDoc - V1.0](http://127.0.0.1:8000/redoc)
  
[Extendeal API - Swagger UI - V1.0](http://127.0.0.1:8000/docs)
