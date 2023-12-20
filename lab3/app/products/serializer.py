from flask_restful import fields

category_serializers = {
    'id': fields.Integer,
    'name': fields.String,
    'image': fields.String,
}

product_serializers = {
    'id': fields.Integer,
    'name': fields.String,
    'image': fields.String,
    'description': fields.String,
    'price': fields.Float,
    'in_stock': fields.Boolean,
    'cat_id': fields.Integer,
}
