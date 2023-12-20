from flask import render_template
from app.products import product_blueprint
# @product_blueprint.errorhandler(404)
# def page_not_found(error):
#     return render_template('errors/page_not_found.html')