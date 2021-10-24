## Buró de contracargos, reduciendo fraudes. 🚀
# Bienvenido al Backend

[Visitar Fronend : https://frontend.hackatonbbva.g-cs.dev/2021auth-login.html ](https://frontend.hackatonbbva.g-cs.dev/2021auth-login.html)


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

## ws

Permite el conectarse por websocket y mandar las peticiones por este socket para reducir 
los tiempos de respuesta.

# Deployment

Toda lo trabajado esta hecho en Docker y Docker-Compose, permitiendo hacer un replicado del
servicio facilmente. 

### Letras Chiquititas

*Las rutas actualmente envian modelos de los datos sin hacer peticiones con la excepción de dbTest. 

*Esta activo el servicio de redis, sin guardar peticiones.