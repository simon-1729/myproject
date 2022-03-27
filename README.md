### This application has a dependency on the [ModernJava app](https://github.com/CodePeeler/modernjava.git). See myapp.py for specific url details.


### Activate the virtual environment.
```
> venv\Scripts\activate
```

### Start service and go to [link](http://localhost:5001/api)
```
> python myapp.py
```
#### (Optional) Build and tag a Docker image
```bash
docker build -t simon1729/myflaskapp .
```

#### (Optional) Start Docker container.
```bash
docker run -d -p 5001:5001 --name myflaskapp simon1729/myflaskapp
```

#### (Optional) Alternatively, spin up all containers with Docker-Compose.
```bash
docker-compose up -d
```