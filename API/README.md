# Comandos

### To build the image with tag hackaton
docker build -t hackaton .

### To run the container
docker run -d --name hackcontainer -p 80:80 hackaton

### To run with the docker-compose
docker-compose run --rm backend