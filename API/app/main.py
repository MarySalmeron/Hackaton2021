from typing import Optional

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.pqsql_lib.sqlBd import Bd

#Lectura Datos Dummy
file = open('./app/ejemplo.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="./static"), name="static")


@app.get("/")
def read_root():
    return {"Nvl": "World"}

@app.get("/page", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "page": "Home page adfadsfads"
    }
    return templates.TemplateResponse("page.html", {"request": request, "data": data})

#Niveles de contracargos por banco o procesador


@app.get("/Dashboard")
def read_root():
    return {
        "Porcentaje_de_contracargos_por_banco_o_procesador": {
            "OPENPAY" : "22",
            "BBVA" : "25",
            "Banamex" : "27",
            "Otros" : "23"
        },
        "Porcentaje_de_contracargo_por_BIN": {
            "231423" : "22",
            "231424" : "25",
            "231421" : "27",
            "231429" : "23"
        }
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


### ENDPOINTS para consultar Cosas del buró
@app.get("/items")
def tests_db(q: Optional[str] = None):
    bd = Bd('instruments_dev', 'localhost', 'postgres', 'postgres')
    result = bd.do_query('SELECT * from opportunities LIMIT 10;', returnAffectedRows=True)
    print(result)
    return {"results": result}



### Endpoints para cargar contracargos


### Endpoints para autenticar


### 