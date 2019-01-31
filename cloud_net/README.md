# CS436 lab4
# webpack built project

## install dependency
Make sure you have mySQL and memcached installed. Please start your mysql and memcached service before running the command below. By default, mySQL login as root, and you can leave the password empty. Config file for mySQL is in cloud_net/my.cnf.
Feel free to put more data into the db when testing locally. We also had a minimal db snapshot (cs436.dump) in the repo that you could import via
```
mysql -h localhost -u root cs436 < cs436.dump
```

Other dependencies:
```
cd cloud_net
pip install -r requirements.txt
npm install
npm run build
```

## run server
```
cd cloud_net
npm start
```

## kill server
I know this is silly but we have to kill the django server in this way for now.
```
killall python
```

## Docker

If you would like to connect the MySql server on the host machine from the Docker container, the easiest way to do so is using the [host network](https://docs.docker.com/network/host). Make sure the host field in my.cnf is set to "127.0.0.1" instead of "localhost". 

To build the image, run
```
docker build --network="host" -t cs436lab4 .
```

You can check your newly built image by running
```
docker image ls
```

To run the webserver
```
docker run --network=host cs436lab4
```

To stop the webserver, you could get the container id in another terminal
```
docker container ls
```

Then, you can stop this container by
```
docker container kill CONTAINER_ID
```