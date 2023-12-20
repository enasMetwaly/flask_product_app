from flask_restful import Resource, marshal_with
from app.models import Category, db
from app.categories.serializer import category_serializers
from app.categories.parser import category_request_parser

class CategoryListResource(Resource):
    @marshal_with(category_serializers)
    def get(self):
        categories = Category.get_all_objs()
        return categories, 200

    @marshal_with(category_serializers)
    def post(self):
        data = category_request_parser.parse_args()
        category = Category.save_category(data)
        return category, 201

class CategoryResource(Resource):
    @marshal_with(category_serializers)
    def get(self, cat_id):
        category = Category.get_specific_obj(cat_id)
        return category, 200

    @marshal_with(category_serializers)
    def put(self, cat_id):
        category = Category.get_specific_obj(cat_id)

        data = category_request_parser.parse_args()

        if 'name' in data:
            category.name = data['name']
        if 'image' in data:
            category.image = data['image']

        db.session.commit()

        return category, 200

    def delete(self, cat_id):
        category = Category.get_specific_obj(cat_id)

        db.session.delete(category)
        db.session.commit()
        return '', 204
