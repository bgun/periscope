import datetime

from google.appengine.ext import db


class Hero(db.Model):
    name = db.StringProperty()
    father = db.StringProperty()
    quote = db.StringProperty()
    dob = db.DateTimeProperty(auto_now_add=True)

class HeroMethods:
    def __init__(self):
        pass

    def create_hero(self, name, father, quote):
        h = Hero()
        h.name = name
        h.father = father
        h.quote = quote
        h.put() 
        return h

    def get_all_heroes(self):
        results = db.GqlQuery("SELECT * FROM Hero")
        heroes = []
        if results.count() > 0:
			for h in results:
				heroes.append({
                    "name": h.name,
                    "father": h.father,
                    "quote": h.quote
                })
        return heroes

    def delete_all_heroes(self):
        db.delete(Hero.all())
