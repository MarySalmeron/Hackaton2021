from typing import Optional

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="./static"), name="static")


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/page", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "page": "Home page adfadsfads"
    }
    return templates.TemplateResponse("page.html", {"request": request, "data": data})

#Niveles de contracargos por banco o procesador

@app.get("/Dashboard")
def read_root():
    return {"Niveles de contracargos por banco o procesador": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


### ENDPOINTS para consultar Cosas del buró


### Endpoints para cargar contracargos


### Endpoints para autenticar


### 