# Tienda de muebles con Django y MongoDB

Aplicacion Django que muestra un catalogo de muebles almacenados en MongoDB Atlas mediante **MongoEngine** y el motor de plantillas de Django.

## Ejecutar localmente

```powershell
cd tienda_muebles
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
py manage.py sembrar_productos
py manage.py runserver
```

Abre `http://127.0.0.1:8000/` para ver el catalogo.

## Configuracion

El archivo `.env` se carga automaticamente y contiene `MONGODB_URI`. No se debe versionar: ya esta incluido en `.gitignore`. Para compartir el proyecto, entrega solo `.env.example` y configura las variables de entorno en el servidor de despliegue.

## Comandos utiles

- `py manage.py sembrar_productos`: crea o actualiza los productos de ejemplo en MongoDB.
- `py manage.py check`: valida la configuracion de Django.

