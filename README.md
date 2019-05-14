# MIT
MNIST: tensorflow https://github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/examples/tutorials/mnist/mnist_softmax.py 
1.	Project description:

Train the MNIST hand-written recognition program on local computer, push into a docker container and by applying restful web service API, the program is able to handle the request from client console and print out the result of prediction of hand-written picture, and get back a result in Cassandra database built in container.


2.	Steps:

(1)Train the mnistdeep and run test at the local computer

(2)Using local dockerfile and requirement build a mirroring and using
docker run to start the container, connect to cassandra and enter the
container cqlsh interface

(3)Upload the pys into the container 

(4)Using sudo enter bash to enter and cd pys to build the mnist in
docker and run app.py

(5)Upload pic using the same port  and write the result to cassandra 

3.	Keywords:

Docker build

Dockerfile and requirment

Upload docker minist_deep run to train the docker environment change home to root

Run app.py (test past, change home to root

Connect to docker

Curl upload pic

identify numbers


4.	Commands:
docker run --name nanz-cassandra -p 9042:9042 -d cassandra.

docker exec -it nanz-cassandra cqlsh.

docker run --link nanz-cassandra:cassandra -p 4000:80 mnist.

local: Dockerfile.txt和requirements.txt目录中docker buid -t python3-tensorflow.

docker run -it --name python3-tensorflow --link nanz-cassandra:cassandra -p 4000:80 python3-tensorflow.

docker inspect -f '{{.ID}}' python3-tensorflow.

sudo docker exec -it.

curl localhost:4000/upload -F "file=@picname“. 

curl 0.0.0.0:4000 -F "file=@url".

You can also use the browser and open 0.0.0.0:4000/html.

docker run -it --link nanz-cassandra:cassandra --rm cassandra cqlsh cassandra.

describe keyspaces;

use mykeyspace;

select * from nanztable;
