# MIT
MNIST: tensorflow https://github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/examples/tutorials/mnist/mnist_softmax.py 
My name is Nan Zhang and I am also called Gabrielle or Gabby or Naan bread all the time. I want to pursue a career in academic.
This is my first Github repository and my first project on Bigdata and my first time use a Linux system - Ubuntu and my first time using an IDE rather than Jupyter notebook.


It's pretty much what is happenning here and I feel more like a 80 years old lady using computer or smart phone for the fist time. God it's exiting and scary.



fork and clone with "git clone git://github.com/gabriellezhang/tensorflow" and "git clone git://github.com/gabriellezhang/tensorflow"


\\\\\\

Steps:
Train the mnistdeep and run test at the local computer

Using local dockerfile and requirement build a mirroring and using
docker run to start the container, connect to cassandra and enter the
container cqlsh interface

Upload the pys into the container 

Using sudo enter bash to enter and cd pys to build the mnist in
docker and run app.py

Upload pic using the same port  and write the result to cassandra 

Keywords:
Docker build
Dockerfile and requirment
Upload docker minist_deep run to train the docker environment change home to root
Run app.py (test past, change home to root
Connect to docker
Curl upload pic
identify numbers

docker run --name nanz-cassandra -p 9042:9042 -d cassandra 
docker exec -it nanz-cassandra cqlsh
docker run --link nanz-cassandra:cassandra -p 4000:80 mnist
local: Dockerfile.txt和requirements.txt目录中docker buid -t python3-tensorflow
docker run -it --name python3-tensorflow --link nanz-cassandra:cassandra -p 4000:80 python3-tensorflow
docker inspect -f '{{.ID}}' python3-tensorflow 
sudo docker exec -it 
curl localhost:4000/upload -F "file=@picname“ 
curl 0.0.0.0:4000 -F "file=@url"
You can also use the browser and open 0.0.0.0:4000/html
docker run -it --link nanz-cassandra:cassandra --rm cassandra cqlsh cassandra
describe keyspaces;
use mykeyspace;
select * from nanztable;
