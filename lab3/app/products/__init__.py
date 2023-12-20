### use flask blueprint

from flask import  Blueprint

product_blueprint=  Blueprint('products', __name__ , url_prefix='/products')

from app.products import  views

from app.products import errors