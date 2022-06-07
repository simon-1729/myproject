# API Service Gateway

#### Details
This is a first draft of an API Service Gateway for a system of microservices. As such it has a dependency on the [ModernJava](https://github.com/CodePeeler/modernjava.git) backend microservice. The url for the backend service may be configured in the myapp.py file. The recommended usecase is to avail of Docker Compose and spin-up both the gateway and the backend service.

##### Setup (virtual environment and install dependencies) 
###### win10, python3
```bash
> cd myproject
> python -m venv .\flask-app\venv
> cd flask-app
> .\venv\Scripts\activate\venv
> pip install -r requirements.txt
```

##### Start service and go to http://localhost:5001/api
```bash
> python myapp.py
```

___


#### Optional 
##### Build and tag a Docker image
```bash
docker build -t simon1729/myflaskapp .
```

##### Start Docker container.
```bash
docker run -d -p 5001:5001 --name myflaskapp simon1729/myflaskapp
```

___


#### Optional
##### Alternatively, spin up all containers with Docker-Compose.
```bash
docker-compose up -d
```

##### The API gateway is available [here](http://localhost:5001/api) and the back end service is available [here](http://localhost:8888/swagger-ui.html#/).

