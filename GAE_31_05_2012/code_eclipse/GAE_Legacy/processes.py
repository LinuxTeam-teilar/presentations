import datetime, hashlib, Cookie, db_model,functions
from google.appengine.ext import db
from google.appengine.ext import webapp
import registration_form

class RegistrationProccess (webapp.RequestHandler):
    def post (self):
        ### Get nessaisary info and create an account ###
        username = self.request.get ("username")
        password = hashlib.sha1(username+self.request.get ("password")).hexdigest()
        email = self.request.get ("email")
        question = self.request.get ("secretQ")
        answer = hashlib.sha1(self.request.get ("answer")).hexdigest()
        account = db_model.Account(username=username,password=password,email=email,question=question,answer=answer,activated=True)
        ### Get unimportant information and add the account in the database ###
        if self.request.get("firstname") != "":
            account.firstname = self.request.get ("firstname")
        if self.request.get("lastname") != "":
            account.lastname = self.request.get ("lastname")
        if self.request.get("gender") != "":
            account.gender = self.request.get("gender")
        if self.request.get("country") != "":
            account.country = self.request.get ("country")
        day = self.request.get ("bDay")
        month = self.request.get ("bMonth")
        year = self.request.get ("bYear")
        if day+'/'+month+'/'+year != "//":
            birthday = datetime.datetime.strptime (day + '/' + month + '/' + year, "%d/%m/%Y")
            account.birthday = birthday.date()
        if self.request.get("website") != "":
            account.website = self.request.get ("website")
        account.put ()
        self.redirect('/')
        
class CheckProccess (webapp.RequestHandler):  #    TESTING
    def post (self):
        username = self.request.get ("username")
        account = db.GqlQuery("SELECT * FROM Account WHERE username = :1", username).get()
      
        if account is None:
            return 1
        else:
            return 2 
        
class LoginProccess (webapp.RequestHandler):
    def post (self):
        ### check if the account exists in the datastore based on username & password ###
        username = self.request.get ("username")
        password = hashlib.sha1(username+self.request.get ("password")).hexdigest()
        account = db.GqlQuery("SELECT * FROM Account WHERE username = :1 AND password = :2", username, password).get()

        if account is None:
            self.redirect('/registration')
        else:
            cookie = Cookie.SimpleCookie()
            cookie["LGSU"] = password
            cookie["LGSU"]["expires"] = 12 * 30 * 24 * 60 * 60
            self.response.headers.add_header("Set-Cookie", cookie.output(header=''))
            self.redirect('/')
            
class LogoutProccess (webapp.RequestHandler):
    def get (self):
        ### Expire the cookie ###
        cookie = Cookie.SimpleCookie()
        cookie["LGSU"] = ""
        cookie["LGSU"]["expires"] = -1
        self.response.headers.add_header("Set-Cookie", cookie.output(header=''))
        self.redirect('/')

class EditProccess (webapp.RequestHandler):
    def post (self):
        user,signed,female = functions.getThatCookie()
        
        if self.request.get("firstname") != "":
            user.firstname = self.request.get("firstname")
        else:
            user.firstname = None
        if self.request.get("lastname") != "":
            user.lastname = self.request.get("lastname")
        else:
            user.lastname = None
        if self.request.get("gender") != "":
            user.gender = self.request.get("gender")
        else:
            user.gender = None
        if self.request.get("country") != "":
            user.country = self.request.get("country")
        else:
            user.country = None
        day = self.request.get ("bDay")
        month = self.request.get ("bMonth")
        year = self.request.get ("bYear")
        if day+'/'+month+'/'+year != "//":
            birthday = datetime.datetime.strptime (day + '/' + month + '/' + year, "%d/%m/%Y")
            user.birthday = birthday.date()
        else:
            user.birthday = None
        if self.request.get("website") != "":
            user.website = self.request.get("website")
        else:
            user.website = None
        user.put()  
        self.redirect('/user/'+user.username)