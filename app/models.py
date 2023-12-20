from flask_sqlalchemy import  SQLAlchemy
# from flask_sqlalchemy import func
from sqlalchemy import func

from flask import request, redirect, url_for
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func


from datetime import datetime

import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename


db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String, nullable=True)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    in_stock = db.Column(db.Boolean, default=False)
    created_on = db.Column(db.DateTime, default=func.current_timestamp())
    updated_on = db.Column(db.DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())
    cat_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True)  # Define the foreign key column
    category = db.relationship("Category", foreign_keys=[cat_id])  # Define the relationship with the Category model


    def __str__(self):
        return f"{self.name}"

    def get_image_url(self):
        return  url_for("static",filename=f'/products/images{self.image}')

    @classmethod
    def save_product(cls, request_data):
        product = cls(**request_data)
        db.session.add(product)
        db.session.commit()
        return  product


    @classmethod
    def get_all_objs(cls):
        return cls.query.all()

    @classmethod
    def get_specific_obj(cls,id):
        return cls.query.get_or_404(id)

    @property
    def show_url(self):
        return url_for('products.show',id=self.id)

    def delete_url(self):
        return url_for('products.delete',id=self.id)
    def update_url(self):
        return url_for('products.update',id=self.id)



    def delete_obj(self):
        db.session.delete(self)
        db.session.commit()


class Category(db.Model):
     __tablename__ = 'categories'
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String, unique=True)
     image = db.Column(db.String, nullable=True)
     created_on = db.Column(db.DateTime, default=func.current_timestamp())
     updated_on = db.Column(db.DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())
     products=db.relationship(Product,backref='catgory')

     @classmethod
     def save_category(cls, request_data):
         catgory = cls(**request_data)
         db.session.add(catgory)
         db.session.commit()
         return catgory

     @classmethod
     def get_all_objs(cls):
         return cls.query.all()

     @classmethod
     def get_specific_obj(cls, id):
         return cls.query.get_or_404(id)

     @property
     def show_url(self):
        return url_for('categories.show',id=self.id)

     def delete_url(self):
        return url_for('categories.delete', id=self.id)



