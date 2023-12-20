from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, BooleanField, SelectField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from  app.models import  Category , Product
from wtforms_sqlalchemy.orm import model_form

def get_all_categories():
    return Category.query.all()

class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image = StringField('Image')
    description = TextAreaField('Description', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    in_stock = BooleanField('In Stock')
    cat_id = QuerySelectField('Category', query_factory=get_all_categories, allow_blank=True, get_label='name')

# class ProductForm(FlaskForm):
#     name = StringField('Name', validators=[DataRequired()])
#     image = StringField('Image')
#     description = TextAreaField('Description', validators=[DataRequired()])
#     price = FloatField('Price', validators=[DataRequired()])
#     in_stock = BooleanField('In Stock')
#     cat_id = SelectField('Category', coerce=int)


ProductModelForm=model_form(Product)


# class ProductModelForm(model_form():
#     class Meta: