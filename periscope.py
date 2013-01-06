import cgi
import datetime
import jinja2
import os
import urllib
import webapp2

from google.appengine.ext import db
from google.appengine.api import users

from models.orm import *

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Index(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'

        orm = PeriscopeDB()
        heroes = orm.get_all_heroes()

        template_data = {
            "title": "All the heroes!",
            "heroes": heroes
        }
        template = jinja_environment.get_template('/templates/index.tmpl.html')
        self.response.write(template.render(template_data))

class MakeData(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'

        orm = PeriscopeDB()
        orm.delete_all_heroes()
        orm.create_hero("Aragorn","Arathorn","I love Gondor!");
        orm.create_hero("Boromir","Denethor","I love Gondor more but I'm dead now.");

        self.response.write('Done');

app = webapp2.WSGIApplication([
    ('/',         Index),
    ('/makedata', MakeData)
], debug=True)
