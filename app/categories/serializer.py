from flask_restful import fields

category_serializers = {
    'id': fields.Integer,
    'name': fields.String,
    'image': fields.String,
    'created_on': fields.DateTime(dt_format='iso8601'),
    'updated_on': fields.DateTime(dt_format='iso8601'),
}
