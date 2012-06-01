import processes,webpages
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

        
application = webapp.WSGIApplication( [
                                       ('/', webpages.MainPage), 
                                       ('/registration', webpages.RegisterPage),
                                       ('/check', processes.CheckProccess),
                                       ('/sign', processes.RegistrationProccess),
                                       ('/login', processes.LoginProccess),
                                       ('/logout', processes.LogoutProccess),
                                       ('/user/.*', webpages.UserPage),
                                       ('/edit/.*', webpages.EditPage),
                                       ('/change', processes.EditProccess),
                                       ('/.*', webpages.ErrorPage),
                                       ], debug=True)
    
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()