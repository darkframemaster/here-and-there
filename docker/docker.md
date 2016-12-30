# docker
## install
* [install in mac](https://docs.docker.com/docker-for-mac/)

## commands
### version check:
```bash
$docker --version

$docker-machine --version

$docker-compose --version
```
### process check:
```bash
# list running docker process
$docker ps

# list all docker process
$docker ps -a
```
### examples:
#### hello world:
```bash
$docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
c04b14da8d14: Pull complete 
Digest: sha256:0256e8a36e2070f7bf2d0b0763dbabdd67798512411de4cdcf9431a1feb60fd9
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker Hub account:
 https://hub.docker.com

For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/
```
#### Dockerized web server
```bash
$docker run -d -p 80:80 --name webserver nginx
CONTAINER ID        IMAGE               COMMAND
6ab6f0e2a66a        nginx               "nginx -g 'daemon off"   

CREATED             STATUS              PORTS 
27 minutes ago      Up 27 minutes     0.0.0.0:80->80/tcp, 443/tcp   

NAMES
webserver
```
### stop, restart or remove containers and images
```bash
# stop use process's name
$docker stop webserver
# stop use process's id
$docker stop 6ab6f0e2a66a

# restart
$docker start webserver

# stop and remove a container
$docker rm -f webserver

# list images
$docker images
# remove a image by image's name or image's id
$docker rmi image_name|image_id
```

## settings
While docker is running,there will be a whale in the status bar, like this:

![](https://docs.docker.com/docker-for-mac/images/whale-x.png)

You can change your docker settings use this whale  `·(>^ω^<)·`.
### preferences

 


