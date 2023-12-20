#function to start app
from flask import Flask,render_template

from app.categories.api_views import CategoryResource, CategoryListResource
from app.config import  project_config as App_Config
from app.models import db
from flask_migrate import Migrate

from app.models import db
from app.products.views import  *
from app.products import  product_blueprint
from app.categories import  catgory_blueprint
from  flask_restful import Api
from app.products.api_views import ProductListResource, ProductResource





def create_app(config_name='dev'):
    app = Flask(__name__)
    Current_App_Config = App_Config[config_name]
    app.config["SQLALCHEMY_DATABASE_URI"]= Current_App_Config.SQLALCHEMY_DATABASE_URI
    app.config.from_object(Current_App_Config)
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)

    # Add the ProductListResource to the URL map
    api.add_resource(ProductListResource, '/api/products')
    api.add_resource(ProductResource, '/api/product/<int:pro_id>')
    api.add_resource(CategoryListResource, '/api/categories')
    api.add_resource(CategoryResource, '/api/category/<int:cat_id>')


    UPLOAD_FOLDER = 'uploads'

    # app.secret_key = '1'
    #
    # Construct the absolute path to the upload directory
    upload_dir = os.path.join(app.root_path, UPLOAD_FOLDER)
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    app.config['UPLOAD_FOLDER'] = upload_dir

    app.register_blueprint(product_blueprint)
    app.register_blueprint(catgory_blueprint)



    return  app