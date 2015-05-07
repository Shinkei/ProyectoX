# REST API for Products

##Description
>This project is a demo writen in python with the microframework Flask, to provide an test a REST API, instead of this, it is important to highlight that the project use python 3.4 and MongoDB

##Instalation

####Virtualenvwrapper
sudo pip install virtualenv virtualenvwrapper

echo -e "\n# virtualenvwrapper\nsource /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc

>Just to consider this commands, We use virtualenvwrapper to isolate the project  
`mkvirtualenv projectAPI`  
`pip install flask`  
`pip install pep8`  
`pip install pyflakes`  
`pip install mongoengine`  
`pip install flask_mongoengine`  
`pip install flask-httpauth`  
`pip install pymongo==2.8 # there is an error with the verson 3`

##Curl Examples
> * To find all the products:  
`curl -i -u manito:proyectox http://localhost:5000/proyectox/v2/products`
* To find a product by id:  
`curl -i http://localhost:5000/proyectox/v2/products/5521bf3ee555c0249d496250`
* TO create a new product:  
`curl -i -H "Content-Type: application/json" -X POST -d '{"name":"product test","product_type":"product type test","description":"description product test","price": 1000}' http://localhost:5000/proyectox/v2/products`
* To update a product:  
`curl -i -H "Content-Type: application/json" -X PUT -d '{"name":"perro","product_type":"tipo de perro"}' http://localhost:5000/proyectox/v2/products/5521bf3ee555c0249d496250`
* To delete a product:  
`curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/proyectox/v2/products/5521bf3ee555c0249d496250`

#Docker
command to build the docker image for the product's application
> docker build -t shinkei/proyectox:alpha .

command to create the container and use bash to run the requirements file (we do this way to apply the DRY principle)
> docker run -i -t --name productapi -v <<path_to_the_proyect>>:/home/proyectox shinkei/proyectox:alpha /bin/bash
  #in the bash console run
  cd /home/proyectoX/ProductAPI
  pip install -r requirements.txt
  exit

command to save the image with the changes done in the previous step
>1. check the container id  
  docker ps -l  
2. save the container into the image  
  docker commit <<3 first numbers of the image id>> shinkei/proyectox:alpha

command to run the database and prepare the linking
> docker run --name db-proyectox -v <<path to save the database>>:/data -d mongo mongod

command to start the application and linked it with the database container
> docker run -d -p 5000:5000 --name productoapi -v <<path_to_the_proyect>>:/home/proyectox --link db-proyectox:db-proyectox shinkei/proyectox:alpha python /home/proyectox/ProductAPI/product_api.py
