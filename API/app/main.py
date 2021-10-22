from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

#Niveles de contracargos por banco o procesador

@app.get("/Dashboard")
def read_root():
    return {"Niveles de contracargos por banco o procesador": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}