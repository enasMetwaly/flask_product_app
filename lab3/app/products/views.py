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

from  app.products.forms import *




app = Flask(__name__)
app.secret_key = '1'




@product_blueprint.route('/hello', endpoint='hello')
def sayhello():
    return '<h1 style="color:red; text-align:center">  Hello world from Flask MVT</h1'

UPLOAD_FOLDER = '../static/products/uploads'  # Relative path to the root of your project
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





@product_blueprint.route('/create', endpoint='create', methods=['GET', 'POST'])
def create():
    categories=Category.get_all_objs()
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        in_stock = bool(request.form.get('in_stock'))
        image = request.files['image']
        cat_id = request.form.get('category_id')  # Get the selected category ID



        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image.save(app.config['UPLOAD_FOLDER'] + '/' + filename)
        else:
            flash('Invalid or unsupported image file format')
            return redirect(request.url)

        product_data = {
            'name': name,
            'description': description,
            'price': price,
            'in_stock': in_stock,
            'image': filename,
            'cat_id': cat_id,  # Associate the product with the selected category

        }

        # Create and save a new product using the class method from the model
        new_product = Product.save_product(product_data)
        flash(f"Product '{new_product.name}' has been created successfully!")
        return redirect(url_for('products.index'))

    return render_template('products/create.html',categories=categories)
# @product_blueprint.route('/create', endpoint='create', methods=['POST'])
# def create():
#     if request.method == 'POST':
#         product=Product.save_product(request_data=request.form)
#         return redirect('products.index')
#     return render_template('products/create.html', product=product)




@product_blueprint.route('', endpoint='index', methods=['GET'])
def index():
    products=Product.get_all_objs()
    return render_template('products/index.html', products=products)


@product_blueprint.route('<int:id>', endpoint='show', methods=['GET'])
def show(id):
    product=Product.get_specific_obj(id)
    return render_template('products/show.html', product=product)

@product_blueprint.route('/<int:id>/delete', endpoint='delete', methods=['GET'])
def delete(id):
    product=Product.get_specific_obj(id)
    print(product)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('products.index'))  # Use url_for with the endpoint name


@product_blueprint.route('/update/<int:id>', methods=['GET', 'POST'], endpoint='update')
def update(id):
    product = Product.get_specific_obj(id)

    if product is None:
        flash('Product not found')
        return redirect(url_for('products.index'))

    if request.method == 'POST':
        product.name = request.form.get('name')
        product.description = request.form.get('description')
        product.price = float(request.form.get('price'))
        product.in_stock = bool(request.form.get('in_stock'))

        cat_id = request.form.get('category_id')  # Get the selected category ID
        product.cat_id = cat_id  # Update the associated category

        if 'image' in request.files:
            image = request.files['image']
            if image.filename != '' and allowed_file(image.filename):
                filename = secure_filename(image.filename)
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                product.image = filename  # Update the product's image

        db.session.commit()
        flash('Product updated successfully')
        return redirect(url_for('products.index'))

    categories = Category.get_all_objs()
    return render_template('products/update.html', product=product, categories=categories)



# @product_blueprint.route('/forms_create', endpoint='forms_create', methods=['GET', 'POST'])
# def add_product():
#     form = ProductForm(request.form)
#     form_data=dict(request.form)
#
#     # Query categories from the database to populate the choices for the cat_id field
#
#     form.cat_id.choices = [(category.id, category.name) for category in Category.query.all()]
#
#     if request.method == 'POST' :
#         if form.validate_on_submit():
#             del form_data['csrf_token']
#
#             product = Product.save_product(request_data=request.form)
#             return redirect(url_for('products.index'))  # Use url_for with the endpoint name
#         else:
#             return "invalid input"
#     return redirect(url_for('success_page'))  #    return render_template('products/create_form.html', form=form)
#
#
# @product_blueprint.route('/forms_create', endpoint='forms_create', methods=['GET', 'POST'])
# def add_product():
#     form = ProductForm()
#
#     # Query categories from the database to populate the choices for the cat_id field
#     form.cat_id.choices = [(category.id, category.name) for category in Category.query.all()]
#
#     if request.method == 'POST':
#         if form.validate_on_submit():
#             product = Product(
#                 name=form.name.data,
#                 image=form.image.data,
#                 description=form.description.data,
#                 price=form.price.data,
#                 in_stock=form.in_stock.data,
#                 cat_id=form.cat_id.data
#             )
#             db.session.add(product)
#             db.session.commit()
#             return redirect(url_for('products.index'))  # Redirect to the product listing page
#         else:
#             return "Invalid input"  # Handle form validation errors
#
#     return render_template('products/create_form.html', form=form)

##modelform
@product_blueprint.route('/forms_create', endpoint='forms_create', methods=['GET', 'POST'])
def add_product():
    form = ProductModelForm(request.form)
    form_data=dict(request.form)

    # Query categories from the database to populate the choices for the cat_id field

    form.cat_id.choices = [(category.id, category.name) for category in Category.query.all()]

    if request.method == 'POST' :
        if form.validate_on_submit():

            product = Product.save_product(request_data=request.form)
            return redirect(url_for('products.index'))  # Use url_for with the endpoint name
        else:
            return "invalid input"
    return redirect(url_for('success_page'))  #    return render_template('products/create_form.html', form=form)
