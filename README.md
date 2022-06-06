# API Service Gateway

#### Details
This is a first draft of an API service Gateway for system of microservices. As such it has a dependency on the [ModernJava app](https://github.com/CodePeeler/modernjava.git). The url may be configured in the myapp.py. However, the recommended usecase is to avail of Docker Compose and spin-up all dependencies.

##### SETUP (virtual environment and install dependencies)
```bash
> cd myproject
> python -m venv .\flask-app
> cd flask-app
> .\Scripts\activate
> pip install -r requirements.txt
```

##### Start service and go to [(http://localhost:5001/api)]
```bash
> python myapp.py
```

##### --------------------------------------------------------------------
##### (Optional) Build and tag a Docker image
```bash
docker build -t simon1729/myflaskapp .
```

##### Start Docker container.
```bash
docker run -d -p 5001:5001 --name myflaskapp simon1729/myflaskapp
```

##### --------------------------------------------------------------------
##### (Optional) Alternatively, spin up all containers with Docker-Compose.
```bash
docker-compose up -d
```

##### The API gateway is available at [link](http://localhost:5001/api).
##### And the back end service is available at [link](http://localhost:8888/swagger-ui.html#/).

