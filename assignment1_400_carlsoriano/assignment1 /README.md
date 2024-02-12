# Assignment 1

## Dockerized Application

This repository contains a Dockerized Python application that generates random text data and stores it in a file.

### Building the Docker Image

To build the Docker image, run the following command at the root of the 'assignment1' directory:

```bash
docker build -t assignment1 .



The way I created my volumes was through the Dockerfile  

line 12 

#VOLUME /serverdata 


### Building the Docker Image   

To find the image run this command: 

docker image ls

### Running the application container 

TO run the applicaiton container run this command: 

docker run -it -v servervol:/serverdata assignment1:latest


### Accessing the Container Shell 

Now to access the container shell you must run this command: 

docker run -it -v servervol:/serverdata assignment1:latest /bin/bash 


This should be all that you need to do to make your container and as well as to make my own specific volume.  


 
