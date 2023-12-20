from  flask_restful import Resource,marshal_with
from app.models import Product, db
from app.products.serializer import product_serializers
from  flask import  request
from  app.products.parser import product_request_parser
class ProductListResource(Resource):
    @marshal_with(product_serializers)
    def get(self):
        products=Product.get_all_objs()
        return  products,200

    # @marshal_with(product_serializers)
    # def post(self):
    #     # Parse request params
    #     data = product_request_parser.parse_args()
    #     print(data)
    #     img = data['image']
    #     print(img)
    #
    #     # Define a list of allowed extensions
    #     allowed_extensions = {'jpg', 'jpeg', 'png', 'gif'}
    #
    #     if img:
    #         # Split the image file name and get the extension
    #         img_extension = img.filename.rsplit('.', 1)[1].lower()
    #
    #         if img_extension in allowed_extensions:
    #             # Create a new Product instance and assign field values from data
    #             product = Product(
    #                 name=data['name'],
    #                 image=data['image'],
    #                 description=data['description'],
    #                 price=data['price'],
    #                 in_stock=data['in_stock'],
    #                 cat_id=data['cat_id']
    #             )
    #
    #             # Save the product to the database
    #             db.session.add(product)
    #             db.session.commit()
    #
    #             return product, 201
    #     return {"message": "Invalid image file"}, 400
    @marshal_with(product_serializers)
    def post(self):
        # Parse request params
        data = product_request_parser.parse_args()
        print(data)

        product = Product(
                name=data['name'],
                image=data['image'],
                description=data['description'],
                price=data['price'],
                in_stock=data['in_stock'],
                cat_id=data['cat_id']
        )

        # Save the product to the database
        db.session.add(product)
        db.session.commit()

        return product, 201

class ProductResource(Resource):
    @marshal_with(product_serializers)

    def get(self,pro_id):
        product=Product.get_specific_obj(pro_id)
        return  product,200

    @marshal_with(product_serializers)
    def put(self,pro_id):
        product=Product.get_specific_obj(pro_id)

        data=product_request_parser.parse_args()
        print(data)
        if  data["name"]:
            product.name = data["name"]
        if data['image']:
            product.image = data['image']
        if data['description']:
            product.description = data['description']
        if  data['price']:
            product.price = data['price']
        if data['in_stock']:
            product.in_stock = data['in_stock']
        if data["cat_id"]:
            product.cat_id = data.get("cat_id", product.cat_id)
        db.session.add(product)

        db.session.commit()


        return product,201

    @marshal_with(product_serializers)
    def delete(self,pro_id):
        product=Product.get_specific_obj(pro_id)

        db.session.delete(product)
        db.session.commit()
        return 'delet',204
