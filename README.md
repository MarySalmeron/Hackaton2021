## Buró de contracargos, reduciendo fraudes. 🚀
# Bienvenido al repositorio

[Visitar Frontend : https://frontend.hackatonbbva.g-cs.dev/2021auth-login.html ](https://frontend.hackatonbbva.g-cs.dev/2021auth-login.html)

[Visitar Backend : https://hackatonbbva.g-cs.dev/docs ](https://hackatonbbva.g-cs.dev/docs)

[Visitar Video : https://www.youtube.com/watch?v=0Bh6zLS4p5w ](https://www.youtube.com/watch?v=0Bh6zLS4p5w)

[Visitar Figma ](https://www.figma.com/proto/ffmfewFhIRegoy8XqWj67G/Buro-de-contracargos?node-id=248%3A167&scaling=min-zoom&page-id=226%3A324&starting-point-node-id=248%3A167)

## Deployment

Toda lo trabajado esta hecho en Docker y Docker-Compose, permitiendo hacer un replicado del
servicio facilmente. 


# Backend


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



### Letras Chiquititas

*Las rutas actualmente envian modelos de los datos sin hacer peticiones con la excepción de dbTest. 

*Esta activo el servicio de redis, sin guardar peticiones.