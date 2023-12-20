from flask_restful import reqparse

product_request_parser = reqparse.RequestParser()

product_request_parser.add_argument('name', type=str, required=True, help='Name field is required')
product_request_parser.add_argument('image', type=str)
product_request_parser.add_argument('description', type=str)
product_request_parser.add_argument('price', type=float, required=True, help='Price field is required')
product_request_parser.add_argument('in_stock', type=bool)
product_request_parser.add_argument('cat_id', type=int)
