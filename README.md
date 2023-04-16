# eaas
Embeddings as a service
## Installing prerequisites
Prerequisites can be installed by running `pip install -r requirements.txt` in the directory. 
## Running this service
There are two ways to run this service:
### Running async version
This is the recommended way, and it can be run with the command `python encoder.py`. 
The service would be run on port 8080 by default. 
### Running non_async version
This requires [`flask`](https://github.com/pallets/flask) and can be run with the following commands in this directory:
`export FLASK_APP=non_async_encoder.py`
`flask run --host=0.0.0.0`
The service would be run on port 5000 by default. 
## Building and running docker images
There are docker images for both of the above running methods. 
### Async version
Use the Makefile and run: `make build`. This creates an image named eaas. Run via: 
`docker run --name <name> -p <port>:8080 eaas`
### Non_async version
Use the Makefile and run: `make non-async-build`. This creates an image named eaas. Run via: 
`docker run --name <name> -p <port>:8080 eaas_non_async`
