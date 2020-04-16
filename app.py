from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    val_a = 3
    val_b = 2 
    total = val_a+val_b
    return Response(str(total))
    # return Response("Hello World!")

if __name__ == '__main__':
    with Configurator() as config:
    	config.add_route('hello', '/3+2')
    	config.add_view(hello_world, route_name='hello')
    	app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8000, app)
    server.serve_forever()