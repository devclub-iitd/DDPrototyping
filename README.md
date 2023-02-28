# DDPrototyping
Distributed Docker Prototyping

A repository to prototype a distributed storage setting for our production servers. We intend to utilize docker containers to emulate multiple VMs used in production.


## Cockroach DB (SQL)

### Docker Compose

1) Install the CockroachDB Docker Image.
2) Run `docker-compose build` followed by `docker-compose up` in 'example-app-python-django' directory to start the CockroachDB Cluster of 3 containers and the Django app in a separate container.\
**Note**: The docker compose does not run the command in point (3) of the manual docker commands. Run the command once after using `docker compose up` for the first time.

### Manual Docker Commands

The django app added above is configured to run with a local cluster of CockroachDB.
The instructions to run the app in Windows are specified below:

1) Install the CockroachDB Docker Image. Now, make sure that your working directory is set to 'example-app-python-django'.

2) Run the below four commands in a bash terminal after ensuring that Docker Desktop is running in order to initialize a local CockroachDB cluster of 3 containers all of which are linked with each other. This cluster can be used by apps at port 26257 of localhost.\
a)`docker network create -d bridge roachnet`\
b)`docker run -d --name=roach1 --net=roachnet -p 26257:26257 -p 8080:8080 -v "//c/Users/<username>/cockroach-data/roach1:/cockroach/cockroach-data" cockroachdb/cockroach:v22.2.2 start --insecure --join=roach1,roach2,roach3`\
c)`docker run -d --name=roach2 --net=roachnet -v "//c/Users/<username>/cockroach-data/roach2:/cockroach/cockroach-data" cockroachdb/cockroach:v22.2.2 start --insecure --join=roach1,roach2,roach3`\
d)`docker run -d --name=roach3 --net=roachnet -v "//c/Users/<username>/cockroach-data/roach3:/cockroach/cockroach-data" cockroachdb/cockroach:v22.2.2 start --insecure --join=roach1,roach2,roach3`\

3) Now, we have 3 running containers. This last command will perform the intialization of the cluster.\
`docker exec -it roach1 ./cockroach init --insecure`

4) The django app can be started in the docker container using the below 2 commands.\
a)`docker build . -t weba`\
b)`docker run --add-host host.docker.internal:host-gateway -p 8000:8080 weba`\
The first command will build the image and the second command will run the container. The `-add-host host.docker.internal:host-gateway` allows the docker container to access the localhost ports of the host machine using the keyword `host.docker.internal` which has been placed in the settings.py file. This allows the app to connect to the CockroachDB cluster using the localhost port 26257. The `8000:8080` represents localhost port `8000` where we can access the app and the `8080` port is the port inside the docker container where the app is hosted.

5) Note that the app does not have HTML pages. We can send a curl POST request using bash as shown below to add to the database and we can check if it is added using the second command which is a GET request.\
a)`curl --header "Content-Type: application/json" --request POST --data '{"name":"Santhosh"}' http://127.0.0.1:8000/customer/`\
b)`curl http://127.0.0.1:8000/customer/`



