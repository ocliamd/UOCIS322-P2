# UOCIS322 - Project 2 #

A "getting started with Docker" project for CIS 322, Introduction to Software Engineering, at the University of Oregon.

* Basic project that demonstrates the basics when using flask and docker. 

## Basic Docker commands

* Get information about docker setup the machine

  ```
  docker info
  ```

* List running docker containers

  ```
  docker ps
  ```

* List all docker containers

  ```
  docker ps -a
  ```

* List images using

  ```
  docker images
  ```

* Build an image

  ```
  docker build -t <Tag name> path/
  ```

  or just do this if your `Dockerfile` is in the same directory:
  ```
  docker build -t <Tag Name> .
  ```

* Remove containers

  ```
  docker container rm <Container Name>
  ```

* Run containers
  ```
  docker run <Tag Name / Image ID>
  ```

  ```
  docker run -h CONTAINER1 -i -t debian /bin/bash
  docker run -h CONTAINER1 -i -t ubuntu /bin/bash
  ```

  Here, `-h` is used to specify a container name, `-t` to start with tty, and `-i` means interactive. Note: second times will be quick because of caching.

* Docker with networking

  ```
  docker run -h CONTAINER2 -i -t --net="bridge" debian /bin/bash
  ```

* When the containers are not running and when you're done, kill them using

  ```
  docker rm `docker ps --no-trunc -aq`
  ```

* Rename using

  ```
  docker rename name_v0 name_v1
  ```

* Start a container

  ```
  docker start <container name>
  ```

* Stop a container

  ```
  docker stop <container name>
  ```

# Creating images

* Create a `Dockerfile`. The name is case sensitive and it has to be `Dockerfile`

  ```
  vim Dockerfile
  ```

* The `FROM` command specifies the base image you are going to use. It can be an existing image, like ubuntu, alpine, debian, etc.

  ```
   FROM debian
  ```

* `CMD` command specifies all the commands you need to run

  ```
   CMD echo hello world
  ```

* Build the image with folder name (`.` in this case)

  ```
   docker build .
  ```

* Final output
  ```
  Successfully built e2e741ea5f6f  
  ```

* Run the image using the image ID (`e2e741ea5f6f` in this case) and a test name of your choice

  ```
  docker run --name <test name> e2e741ea5f6f
  ```

* Remove images using

  ```
  docker rmi <Image ID>
  ```


## Credits

Michal Young, Ram Durairajan, Steven Walton, Joe Istas.
