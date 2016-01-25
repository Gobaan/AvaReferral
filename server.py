import cherrypy
import json


class Root(object):
    @cherrypy.expose
    def index(self):
        with open("index.html") as fp:
            return fp.readlines()

    @cherrypy.expose
    def email(self, address):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        return json.dumps({'name': address.split('@')[0]})

if __name__ == '__main__':
    cherrypy.quickstart(Root(), '/', 'prod.conf')
