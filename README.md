
# Hipo Todo (Flask) 📝  
This is a simple todo application built on the flask python framework.  

## Author  
- [@Afolabi](https://www.github.com/billiegate)  

## Get Started 🚀  
To get started, hit the 'clear' button at the top of the editor!  

## Run 🔥  
Clone the project from it repository by runing `git clone https://github.com/billiegate/pay-hippo-todo.git`. 

After cloning it, you can run this project by either using the makefile or
the serve.sh bash script provided in the root directory. You can also spin up a 
docker container hosting the project by running the image in the Dockerfile provided at the 
project root directory

## Bash ✨  
Once you're done, run `bash serve.sh` in your command line!

## Make
run `make all` which will run the following make command in this order

~~~javascript  
make install: install required packages as needed by the poject  
make migrate: run database migration  
make tests: run unit and feature test  
make run: starts the application
~~~

## Docker
run `docker image build -t hipo_todo:1.0 .` to build the image
run `docker run --name hipo_todo -p 5000:5000 -d hipo_todo:1.0` to run the container 

## Tech Stack  
**Server:** Python, Flask, SQLite  
 
