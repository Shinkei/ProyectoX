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


##Curl Examples
> * To find all the products:  
`curl -i -u manito:proyectox http://localhost:5000/proyectox/v1/products`
* To find a product by id:  
`curl -i http://localhost:5000/proyectox/v1/products/5521bf3ee555c0249d496250`
* TO create a new product:  
`curl -i -H "Content-Type: application/json" -X POST -d '{"name":"product test","product_type":"product type test","description":"description product test","price": 1000}' http://localhost:5000/proyectox/v1/products`
* To update a product:  
`curl -i -H "Content-Type: application/json" -X PUT -d '{"name":"perro","product_type":"tipo de perro"}' http://localhost:5000/proyectox/v1/products/5521bf3ee555c0249d496250`
* To delete a product:  
`curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/proyectox/v1/products/5521bf3ee555c0249d496250`

#Docker
command to build the docker image for the product's application
> docker build -t shinkei/proyectox:alpha .

command to run the database and prepare the linking
> docker run -d --name db mongo

command to start the application and linked it with the database container
> docker run -d -P --name productoapi --link db:db shinkei/proyectox /bin/bash