from pyramid.config import Configurator

def includeme(config):
    config.add_route('add_product', '/products/add')
