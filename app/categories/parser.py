from flask_restful import reqparse

category_request_parser = reqparse.RequestParser()

category_request_parser.add_argument('name', type=str, required=True, help='Name field is required')
category_request_parser.add_argument('image', type=str)
