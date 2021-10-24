from typing import Optional
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from app.pqsql_lib.sqlBd import Bd
import redis
import os

bd = Bd(
        'dbcontracargos',
        'dbcontracargos.cluster-cr3eijvzbpoy.us-east-2.rds.amazonaws.com',
        'postgres',
        'holamundo',
        )
    result = bd.do_query('SELECT * from opportunities LIMIT 10;', returnAffectedRows=True)
    print(result)

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
            var ws = new WebSocket("ws://137.184.155.141:82/ws");
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


app = FastAPI()

@app.get("/")
async def get():
    return HTMLResponse(html)

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


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


### ENDPOINTS para consultar Cosas del buró
@app.get("/items")
def tests_db(q: Optional[str] = None):
    bd = bd = Bd(
        'postgres',
        'database-2-instance-1.cr3eijvzbpoy.us-east-2.rds.amazonaws.com', #writer
        'postgres',
        'holamundo')
    result = bd.do_query('SELECT * from contracargosact LIMIT 10;', returnAffectedRows=True)
    print(result)
    return {"results": result}



### Endpoints para cargar contracargos


### Endpoints para autenticar


### 