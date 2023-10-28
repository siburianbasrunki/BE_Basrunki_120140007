from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from .model.myModel import Product

def main(global_config, **settings):
    config = Configurator(settings=settings)
    
    
    engine = engine_from_config(settings, 'sqlalchemy.')
    config.include('pyramid_sqlalchemy')
    config.registry['dbsession'] = session_factory(engine)
    

    return config.make_wsgi_app()
