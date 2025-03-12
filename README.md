# Hello World Python Docker

### Project Structure
`main.py`: source code
`Dockerfile`: configuration file for building the image
`compose.yaml`: configuration file for running the container

### Run the Container
To run the docker container:
```
docker compose up
```

To remove docker container:
```
docker compose down
```
`compose.yaml`: configuration file for running the container

### Build the Image
```
docker build -t <IMAGE_NAME> .
```
Command should be run where `Dockerfile` is
