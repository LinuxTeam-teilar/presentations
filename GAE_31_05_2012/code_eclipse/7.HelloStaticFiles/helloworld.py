import webapp2
from google.appengine.ext import db
import jinja2,os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MyData(db.Model):
    content = db.StringProperty(multiline=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = jinja_environment.get_template('templates/index.html')
        self.response.out.write(template.render(template_values))
        
class SubmitPage(webapp2.RequestHandler):
    def post(self):
        user = MyData()
        user.content = self.request.get('content')
        user.put()
        self.redirect('/submit')
        
    def get(self):
        query = db.GqlQuery("SELECT *  FROM MyData")
        template_values = { 'query':query }
        template = jinja_environment.get_template('templates/submit.html')
        self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([('/', MainPage),
                              ('/submit', SubmitPage)],
                              debug=True)