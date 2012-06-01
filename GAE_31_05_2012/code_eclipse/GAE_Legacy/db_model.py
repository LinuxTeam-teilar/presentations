from google.appengine.ext import db

class Account(db.Model):
    username = db.StringProperty(required = True)
    password = db.StringProperty(required = True)
    email    = db.EmailProperty(required = True)
    question = db.StringProperty(required = True)
    answer   = db.StringProperty(required = True)
    activated = db.BooleanProperty(required = True)
    
    firstname = db.StringProperty(required = False)
    lastname  = db.StringProperty(required = False)
    gender    = db.StringProperty(required = False)
    country   = db.StringProperty(required = False)
    birthday  = db.DateProperty(required = False)
    website   = db.StringProperty(required = False)