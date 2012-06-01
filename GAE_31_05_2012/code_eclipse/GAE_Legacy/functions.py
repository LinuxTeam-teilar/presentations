import os, Cookie,db_model
from google.appengine.ext import db

def getThatCookie():
        user = ""
        signed = False
        female = False
        ### Check if you can grab a cookie ###
        cookie_string = os.environ.get('HTTP_COOKIE')
        if cookie_string is not None:
            cookie = Cookie.SimpleCookie()
            cookie.load(cookie_string)
            sid = cookie['LGSU'].value
            ### Check if the cookie mathes a Datastore entry ###
            accountQuery = db.GqlQuery("SELECT *  FROM Account  WHERE password = :1", sid)
            account = accountQuery.get() 
            if account is not None:
                for account in accountQuery:
                    user = account
                ### Determinate if the account is activated and the gender for later use ###
                #if user.activated :
                signed = True
                if user.gender == "Female":
                    female = True
                    
        return user,signed,female