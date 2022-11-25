import sys
from os.path import dirname, join, abspath

# identify app module
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from fastapi import FastAPI
from app.api.endpoints.items import item_router
from app.api.endpoints.users import user_router

# main Fastapi instance
app = FastAPI()

# Router Register
app.include_router(item_router)
app.include_router(user_router)


# entrypoint
@app.get("/")
def index():
    return {"title": "Challenge Extendeal",
            "Author": "Miguel",
            "Documentation URL Swagger": "/docs",
            "Documentation URL Redoc": "/redoc",
            }
