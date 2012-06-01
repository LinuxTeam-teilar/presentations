import os, datetime, functions
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
import registration_form

class MainPage(webapp.RequestHandler):
    def get(self):
        user,signed,female = functions.getThatCookie()

        template_values = {
                           "user":user,
                           "signed":signed,
                           "female":female,
                           }
        path = os.path.join(os.path.dirname(__file__), "templates/index.html")
        self.response.out.write(template.render(path, template_values))
        
class RegisterPage(webapp.RequestHandler):
    def get(self):
        user,signed,female = functions.getThatCookie()
        # GET CURRENT YEAR AND LIST OF YEARS    
        currentYear = datetime.datetime.now().year
        firstYear = currentYear-100
        yearList = list()
        i=0
        for year in range(firstYear,currentYear+1):
            yearList.insert(i, year)
            i += 1
        yearList.reverse()
        
        
        template_values = {
                           "user":user,
                           "signed":signed,
                           "female":female,
                           "currentYear" : currentYear,
                           "years" : yearList,
                           "registration":registration_form.Registration_form(),
                           }
        path = os.path.join(os.path.dirname(__file__), "templates/register.html")
        self.response.out.write(template.render(path, template_values))     
                       
class UserPage(webapp.RequestHandler):
    def get(self):
        user,signed,female = functions.getThatCookie()
        ### if the user has not logged in redirect him ###
        if  signed:
            ### find the owner of the page ### 
            url_get = self.request.url
            username_pos = url_get.find("/user/")+5
            i = 0
            name = ""
            for c in url_get:
                if i > username_pos:
                    name = name+c
                i += 1
                
            owner = db.GqlQuery("SELECT * FROM Account WHERE username = :1", name).get()
            myPage = False
            femaleAcc = False
    
            if  owner is not None:
                ### get the data of the owner of the page ### 
                if owner.gender == "Female":
                    femaleAcc = True
                age = None
                birthday = owner.birthday
                if birthday != None:
                    now = datetime.datetime.now()
                    age = now.year - birthday.year
                    
                if user.username == owner.username:
                    myPage = True
                
                template_values = {
                    "user":user,
                    "signed":signed,
                    "female":female,
                    "owner":owner,
                    "femaleAcc":femaleAcc,
                    "age":age,
                    "myPage":myPage,
                    }
                path = os.path.join(os.path.dirname(__file__), "templates/user.html")
                self.response.out.write(template.render(path, template_values))
            else:
                ### if there is not such an account ###
                self.redirect('/error')     
        else:
            self.redirect("/registration")       
class EditPage(webapp.RequestHandler):
    def get(self):
        user,signed,female = functions.getThatCookie()
        ### Check if the user wants to edit the right page ###
        url_get = self.request.url
        username_pos = url_get.find("/edit/")+5
        i = 0
        name = ""
        for c in url_get:
            if i > username_pos:
                name = name+c
            i += 1
        
        if signed:
            if user.username != name:
                self.redirect('/error')   
            else:
                ### Get the data of the user ###
                day = None
                month = None
                year = None
                birthday = user.birthday
                if birthday != None:
                    day   = birthday.day
                    month = birthday.month
                    year  = birthday.year               
                ### Get current year and list of years ###  
                currentYear = datetime.datetime.now().year
                firstYear = currentYear-100
                yearList = list()
                i= 0
                for years in range(firstYear,currentYear+1):
                    yearList.insert(i, years)
                    i +=1
                yearList.reverse()
            
                template_values = {
                   "user":user,
                   "signed":signed,
                   "female":female,
                   "bDay":day,
                   "bMonth":month,
                   "bYear":year,
                   "years":yearList,
                   }
                path = os.path.join(os.path.dirname(__file__), "templates/edit.html")
                self.response.out.write(template.render(path, template_values))
        else:
            self.redirect("/registration")
    
class ErrorPage(webapp.RequestHandler):
    def get(self):
        user,signed,female = functions.getThatCookie()

        template_values = {
                           "user":user,
                           "signed":signed,
                           "female":female,
                           }
        path = os.path.join(os.path.dirname(__file__), "templates/error.html")
        self.response.out.write(template.render(path, template_values))