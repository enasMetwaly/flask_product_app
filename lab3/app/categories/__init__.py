from flask import  Blueprint

catgory_blueprint = Blueprint('categories', __name__, url_prefix='/categories')

from app.categories import  views

