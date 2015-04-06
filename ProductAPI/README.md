# REST API for Products

##Description
>This project is a demo writen in python with the microframework Flask, to provide an test a REST API, instead of this, it is important to highlight that the project use python 3.4 and MongoDB

##Instalation
>Just to consider this commands, We use virtualenvwrapper to isolate the project
`mkvirtualenv projectAPI`
`pip install flask`
`pip install pep8`
`pip install pyflakes`
`pip install mongoengine`
`pip install flask_mongoengine`
`pip install flask-httpauth`

##Curl Examples
> * curl -i -u manito:proyectox http://localhost:5000/proyectox/v1/products
 * curl -i http://localhost:5000/proyectox/v1/products/5521bf3ee555c0249d496250
 * curl -i -H "Content-Type: application/json" -X POST -d '{"name":"product test","product_type":"product type test","description":"description product test","price": 1000}' http://localhost:5000/proyectox/v1/products
 * curl -i -H "Content-Type: application/json" -X PUT -d '{"name":"perro","product_type":"tipo de perro"}' http://localhost:5000/proyectox/v1/products/5521bf3ee555c0249d496250
 * curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/proyectox/v1/products/5521bf3ee555c0249d496250
