from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    # return Response("Hello World!")
    val_a = 3
    val_b = 2 
    total = val_a+val_b
    return Response(total)

if __name__ == '__main__':
    with Configurator() as config:
    	config.add_route('hello', '/3+2')
    	config.add_view(hello_world, route_name='hello')
    	app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8000, app)
    server.serve_forever()