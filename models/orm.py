import datetime

from google.appengine.ext import db

from Hero import *
from Weapon import *

class PeriscopeDB:
    def __init__(self):
        self.hm = HeroMethods()
        pass

    def create_hero(self, name, father, quote):
        return self.hm.create_hero(name, father, quote)

    def get_all_heroes(self):
        return self.hm.get_all_heroes()

    def delete_all_heroes(self):
        return self.hm.delete_all_heroes()
