import datetime

from google.appengine.ext import db

class Weapon(db.Model):
    name = db.StringProperty()
    damage = db.IntegerProperty()

class WeaponMethods:
    def __init__(self):
        pass

    def create_weapon(name, damage):
        w = Weapon()
        w.name = name
        w.damage = damage
        w.put()
        return w

    def get_weapons(weapon_id):
        q = "SELECT * FROM Weapon WHERE id = "+weapon_id
        pass
