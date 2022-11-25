from typing import List

from pydantic import BaseModel, Field


class ItemOutput(BaseModel):
    marca: str = Field(description="marca del producto", example="microsoft")
    descripcion: str = Field(description="detalle del producto", example="mouse optico ergonomigo para juegos")
    precio: float = Field(description="precio en especificación dolar del producto", example=33.3)


class ItemRecords(BaseModel):
    records: List[ItemOutput] = []
