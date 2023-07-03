from flask import Blueprint, request
from app.models import Product, db, User, Image, Comment
from flask_login import login_required, current_user
from app.forms import ProductForm

product_routes = Blueprint("product", __name__)

# Get all Products
# Any user
@product_routes.route('')
def get_all_products():
    """
    Query for all products and returns them in a list of dictionaries
    """
    # May need to update to include the data associated with the foreign keys
    all_products = Product.query.all()
    response = [product.to_dict() for product in all_products]
    print('--------------------------All Products--------------------------------')
    # print('--------------------------response: ', response)
    # print('all_products: ', all_products)

    testresponse = []
    # for product in all_products:
    #     images = Image.query.filter(Image.product_id == product.to_dict()["id"]).all()
    #     # print("-------------------------product: ", product.to_dict()["id"])
    #     placeholder = product.to_dict()
    #     placeholder["images"] = [image.to_dict() for image in images]
    #     # print("------------------product add: ", placeholder)
    #     testresponse.append(placeholder)

    for product in response:
        print("-----------------------------product: ", product)
        # product["test"] = ["test"]
        images = Image.query.filter(Image.product_id == product["id"]).all()
        images = [image.to_dict() for image in images]
        product["images"] = images

    # print("---------------------response: ", response)
    # print("---------------------testresponse: ", testresponse)
    return {'products': response}


# Get a Product by id
# Any user
@product_routes.route('/<int:id>')
def get_single_product(id):
    """
    Query to get a signle product by id
    """
    print('-----------------------------Single Product--------------------------------')
    single_product = Product.query.get(id)

    if not single_product:
        # print("-------------------no single product--------------------")
        return {"No product", 400}

    response = single_product.to_dict()

    images = Image.query.filter(Image.product_id == id).all()
    comments = Comment.query.filter(Comment.product_id == id).all()

    print("-------------images: ", images)

    imageKey = 0
    response["images"] = {}
    for image in images:
        response["images"].update({imageKey: image.to_dict()})
        imageKey += 1

    # commentKey = 0
    # response["comments"] = {}
    # for comment in comments:
    #     response["comments"].update({commentKey: comment.to_dict()})
    #     commentKey += 1


    # print('-------single_product------ ', single_product.to_dict())
    return {'product': response}


# Add a Product
# Authorized user: logged in
@product_routes.route('/create', methods=['POST'])
@login_required
# def create_product(payload):
def create_product():
    """
    Create a product
    """
    print('-----------------------------Add Product--------------------------------')
    form = ProductForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    # print form.data to see what the form is receiving
    # print("-------------------------------------", form.data)
    # pint("--------------------------------------", request.method)
    if form.validate_on_submit():
        data = form.data
        new_product = Product(
            # SKU = data['SKU'],
            name = data['name'],
            price = data['price'],
            inventory = data['inventory'],
            desc=data['desc'],
            owner_id = data['owner_id']
        )
        db.session.add(new_product)
        db.session.commit()
        # print('--------------------------------------------new_product: ')
        print('-------------------------------before success return--------------------------')
        return {
            "product": new_product.to_dict()
        }
    else:
        print('----------------------------before error return--------------------------------')
        return {
            "errors": form.errors
        }


# Edit a Product by Id
# Authorized user: logged in and owner of product
@product_routes.route('/<int:id>/update', methods=['PUT'])
@login_required
def edit_product(id):
    """
    Edit a product by id
    """
    print("--------------------------Edit Product-----------------------------")

    form = ProductForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    print("------------------------------form data: ", form.data)


    if form.validate_on_submit():
        product = Product.query.get(id)

        # Can only be edited by onwer of the product
        if current_user.id != product.owner_id:
            return {"errors": "Not an authorized route"}

        # product.SKU = form.data["SKU"]
        product.name = form.data['name']
        product.price = form.data['price']
        product.inventory = form.data['inventory']
        product.desc = form.data['desc']
        db.session.commit()
        return {
            "product": product.to_dict()
            }

    else:
        return {"errors": form.errors}

# Delete a Product
# Authorized user: logged in and owner of product
@product_routes.route('/<int:id>', methods=["DELETE"])
@login_required
def delete_one_product(id):
    """
    Delete a product by id
    """
    product = Product.query.get(id)
    if current_user.id != product.owner_id:
        return {"errors": "This is not an authorized route."}
    else:
        db.session.delete(product)
        db.session.commit()
        return {"product": "Product deleted"}
