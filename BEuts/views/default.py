from pyramid.view import view_config
from pyramid.response import Response
from ..model.myModel import Product

@view_config(route_name='add_product', request_method='POST')
def add_product(request):
    session = request.dbsession
    data = request.json
    product = Product(name=data['name'], price=data['price'], image=data['image'])
    session.add(product)
    session.flush()
    return Response('Product added')
