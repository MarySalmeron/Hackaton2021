from typing import Optional
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect, Depends, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.pqsql_lib.sqlBd import Bd
from pydantic import BaseModel
import redis
import os
from typing import Optional

description = """
Buró de contracargos, reduciendo fraudes. 🚀

## Rutas Score 

Permite evaluar rápidamente una compra para aceptar o rechazar el cargo,
el score devuelto son el porcentaje de Personas, Comercios, Nombres de Comprador, etc. 
con la misma cantidad o menos de contracargos en el lapso de tiempo.

## Buscar Persona

Permite análizar un perfil o perfiles con la busqueda realizada, permitiendo 
detectar extraños comportamientos. Al agregar el campo de RFC este nos permite
eliminar homónimos en la búsqueda mejorando la calidad de los resultados.

## Dashboard

Devuelve todos los datos necesarios para llenar el Dashboard, de esta manera 
al ser un objeto completo se reducen las peticions ( sin hacer petición por cada componente ).

## Token y User

Proceso de login Oauth 2.0, usuario de prueba:

Usuario: gustavo
Password: secret

## dbTest

Permite hacer una prueba a la base de datos, devolviendo todos los datos actuales.

*Las rutas actualmente envian modelos de los datos sin hacer peticiones con la excepción de dbTest

"""


class Persona(BaseModel):
    RFC: Optional[str] = None
    Nombres: Optional[str] = None
    Apellido_Paterno: Optional[str] = None
    Apellido_Materno: Optional[str] = None
    Telefono: Optional[str] = None
    Correo_Electronico: Optional[str] = None
    Codigo_Postal: Optional[str] = None
    Numero_Tarjetas: Optional[str] = None
    Bancos_Cliente: Optional[str] = None
    Estado: Optional[str] = None
    Ciudad: Optional[str] = None
    Score: Optional[str] = None
    Detalle: Optional[list] = None

class Score(BaseModel):
    Tiempo1Dia: Optional[str] = None
    Tiempo30Dias: Optional[str] = None
    Tiempo90Dias: Optional[str] = None

class Query(BaseModel):
    RFC: Optional[str] = None
    Telefono: Optional[str] = None
    Correo_Electronico: Optional[str] = None
    Comercio: Optional[str] = None
    Nombre_Comprador: Optional[str] = None
    IP: Optional[str] = None
    

r = redis.Redis(host=os.getenv('REDIS_URL'), port=6379, db=0)
r.set('foo', 1)

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("wss://hackatonbbva.g-cs.dev/ws");
            var envio;
            ws.onmessage = function(event) {
                console.log((Date.now()-envio)/2);
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                envio = Date.now();
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

app = FastAPI(
    title="Buró de Contracargos",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Deadpoolio the Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

@app.get("/")
async def get():
    return HTMLResponse(html)


@app.get("/score/comercio/{comercio}", response_model=Score)
async def read_score_comercio(comercio: str):
    return Score(
        Tiempo1Dia = "99%",
        Tiempo30Dias = "40%",
        Tiempo90Dias = "10%"
    )

@app.get("/score/nombre_comprador/{nombre_comprador}", response_model=Score)
async def read_score_nombre_comprador(nombre_comprador: str):
    return Score(
        Tiempo1Dia = "39%",
        Tiempo30Dias = "30%",
        Tiempo90Dias = "10%"
    )

@app.get("/score/ip/{ip}", response_model=Score)
async def read_score_ip(ip: str):
    return Score(
        Tiempo1Dia = "10%",
        Tiempo30Dias = "20%",
        Tiempo90Dias = "10%"
    )

@app.post("/score/query/", response_model=Score)
async def buscarQuery(Query: Query):
    return Score(
        Tiempo1Dia = "29%",
        Tiempo30Dias = "20%",
        Tiempo90Dias = "10%"
    )

@app.post("/buscar/persona/", response_model=Persona)
async def buscarPersona(Persona: Persona):
    Persona = Persona(
        id='123',
        RFC="ROMG9887765M5",
        Nombres="Gustavo",
        Apellido_Paterno="Robles",
        Apellido_Materno="Martínez",
        Telefono="556667778877",
        Correo_Electronico="hi@gus.works",
        Codigo_Postal="09212",
        Numero_Tarjetas="5",
        Bancos_Cliente="BBVA,Santander",
        Estado="Ciudad de México",
        Ciudad="Coyoacán",
        Score="80%",
        Detalle=[

        ]
    )
    return Persona




@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")

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





### ENDPOINTS para consultar Cosas del buró
@app.get("/dbTest")
def tests_db(q: Optional[str] = None):
    bd = Bd(
        'postgres',
        'database-2-instance-1.cr3eijvzbpoy.us-east-2.rds.amazonaws.com', #writer
        'postgres',
        'holamundo',
        )
    result = bd.do_query('SELECT * from contracargosact LIMIT 10;', returnAffectedRows=True)
    return {"results": result}



### Endpoints para cargar contracargos


### Endpoints para autenticar
fake_users_db = {
    "gustavo": {
        "username": "gustavo",
        "full_name": "Gustavo Robles",
        "email": "gustavo@bbva.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}


def fake_hash_password(password: str):
    return "fakehashed" + password


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class UserInDB(User):
    hashed_password: str


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

### 