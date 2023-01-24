# Docker 
* [Installation on ubuntu](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

**WHAT DOCKER?**
* Delivers packages in form of containers (light-weight)
  > Basically solves the problem of works-on-my-machine

**WHY DOCKER**
* Reproducibility (by delivering containers)
* Local experiments 
* Integration tests
* Running pipelines on cloud 
* PySpark 
* Serverless/ AWS Lambda

**Docker vs Virtual-machines**

## Basic commands
1. Hello world
```bash
docker run $image_name # runs image locally (and exits once execution is done)
docker run hello-world
```
```
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.
```
2. Running images in interactive mode using command `docker run -it $image_name`
   1. Note: Making changes to images in interactive mode, does not store changes to image; i.e for local experimentation
3. Getting inside the docker-image via **entry_point** `docker run -it $image_name $entrypoint`
   1. Example: `sudo docker run -it --entrypoint ls alpine:3.16` or `sudo docker run -it --entrypoint ls alpine:3.16`

## Dockerfile 

### About file
Save file named `Dockerfile` inside application 

Contents: 

```docker
# FROM {base_image_name}
FROM python:3.11.1
# COPY check.py /app/check.py

# SET working directory inside container
WORKDIR /usr/src/app

# Source to destination from Workspace to container
COPY . .

# Running the expected application via command: comma-seperated array
ENTRYPOINT [ "python", "./check.py"] 
```

Build and run commands
```bash
paramm@paramm-X556UQK:~/projects/ML-Everything/0.Basics/3.Docker/test$ sudo docker build -t test:latest .
Sending build context to Docker daemon  3.072kB
Step 1/4 : FROM python:3.11.1
 ---> b44268c8cbc0
Step 2/4 : WORKDIR /usr/src/app
 ---> Using cache
 ---> 80aa1fd42c86
Step 3/4 : COPY . .
 ---> 21bc3eb2bd05
Step 4/4 : ENTRYPOINT [ "python", "./check.py"]
 ---> Running in 78e9e199d973
Removing intermediate container 78e9e199d973
 ---> 19ff7bc08e71
Successfully built 19ff7bc08e71
Successfully tagged test:latest
paramm@paramm-X556UQK:~/projects/ML-Everything/0.Basics/3.Docker/test$ sudo docker run  test:latest
Hello from check.py!!!
```

### Individual commands 

1. `FROM {base_image}` gets base_image 
2. `RUN {shell_command}` runs shell command 
3. `WORKDIR` sets working directory 
4. `COPY {SOURCE} {DEST}` copies files from build source folder to container 
5. `ENTRYPOINT ["{command}"]` comma sperated array, example: `ENTRYPOINT [ "python", "./check.py"] `

Interesting read: [understand-how-cmd-and-entrypoint-interact](https://docs.docker.com/engine/reference/builder/#understand-how-cmd-and-entrypoint-interact)





Example: POSTGRES image

[Documnetation:](https://hub.docker.com/_/postgres) 

Command to start postgres

```bash
$ docker run -d \
	--name some-postgres \
	-e POSTGRES_PASSWORD={mysecretpassword} \
	-e PGDATA=/var/lib/postgresql/data/pgdata \
	-v /custom/mount:/var/lib/postgresql/data \
	postgres
```

Custom:

```bash
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -p 5432:5432 \
  -v /home/param/projects/ML-Everything/0.Basics/3.Docker/test/ny_taxi_postgres_data:/var/lib/postgresql/data  \
  
  postgres:13

  # -v c:/Users/alexe/git/data-engineering-zoomcamp/week_1_basics_n_setup/2_docker_sql/ny_taxi_postgres_data:/var/lib/postgresql/data \
  
```

```bash
# PCCLI: PostGresCLI to talk to postgres
pgcli -h localhost -u root -d ny_taxi
```

**Docker network**

* Docker containers and independent and cannot talk to one another; hence need to be present on the same container; here is an example: 

    **Create a network**

    ```bash
    docker network create pg-network
    ```

    **Run Postgres (change the path)**

    ```bash
    docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v c:/Users/alexe/git/data-engineering-zoomcamp/week_1_basics_n_setup/2_docker_sql/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    --network=pg-network --name pg-database \
    postgres:13
    ```

    **Run pgAdmin**

    ```bash
    docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    --network=pg-network --name pgadmin-2 \
    dpage/pgadmin4
    ```

    Note: 

    1. `--network={network_name} --name {unique_name_for_container}`

## `docker-compose.yml` file 

1. Used to configure many docker-containers and bring them up together. 

Example: Run pg-admin & postgres into one YML file 

Note: 

* If applications are part of same docker-compose file, they automatically become part of same network, hence no need to make a network;


Build docker-compose file: `docker-compose up`

# Best practives 

1. Having individual docker container for each service
   1. Example 

        ```
        r
        ├── README.md
        ├── mariadb-service
        │   └── docker-compose.yml
        ├── mongodb-service
        │   ├── README.md
        │   └── docker-compose.yml
        ├── mysql-service
        │   └── docker-compose.yml
        └── postgre-service
        └── docker-compose.yml
        ```

# Resources
PFA section-wise various recources which can be used to revisit concepts. 

## Courses 


## Videos 

## Blogs 

