from app.categories import  catgory_blueprint
from  ..models import  Category
from flask import render_template, request, flash, redirect, url_for, app, Flask
from flask import Blueprint, render_template, request, flash, redirect, url_for, app, Flask
from ..models  import Product, db
from ..models  import Category

from werkzeug.utils import secure_filename
import os
from app.products import  product_blueprint
#
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from flask import current_app



@catgory_blueprint.route('', endpoint='index', methods=['GET'])
def index():
    categories=Category.get_all_objs()
    return render_template('categories/index.html',categories=categories)


app = Flask(__name__)
UPLOAD_FOLDER = '../static/categories/uploads'  # Relative path to the root of your project
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.secret_key = '1'

# Construct the absolute path to the upload directory
upload_dir = os.path.join(app.root_path, UPLOAD_FOLDER)
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

app.config['UPLOAD_FOLDER'] = upload_dir


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#





@catgory_blueprint.route('/create', endpoint='create', methods=['POST', 'GET'])
def create():
    categories = Category.get_all_objs()

    if request.method == 'POST':
        name = request.form.get('name')
        image = request.files['image']

        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image.save(app.config['UPLOAD_FOLDER'] + '/' + filename)
        else:
            flash('Invalid or unsupported image file format')
            return redirect(request.url)

        category_data = {
            'name': name,
            'image': filename
        }

        new_category = Category.save_category(request_data=category_data)
        flash(f"Category '{new_category.name}' has been created successfully!")

        return render_template('categories/index.html', categories=categories)
    return render_template('categories/create.html', categories=categories)


@catgory_blueprint.route('<int:id>', endpoint='show', methods=['GET'])
def show(id):
    category=Category.get_specific_obj(id)
    return render_template('categories/show.html', category=category)

@catgory_blueprint.route('/<int:id>/delete', endpoint='delete', methods=['GET'])
def delete(id):
    catgory=Category.get_specific_obj(id)
    print(catgory)
    db.session.delete(catgory)
    db.session.commit()
    return redirect(url_for('categories.index'))  # Use url_for with the endpoint name
