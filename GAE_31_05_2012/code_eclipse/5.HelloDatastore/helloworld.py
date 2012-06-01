import webapp2
from google.appengine.ext import db

class MyData(db.Model):
    content = db.StringProperty(multiline=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("""
          <html>
            <body>
              <form action="/submit" method="post">
                <div><textarea name="content"></textarea></div>
                <div><input type="submit" value="Sign Guestbook"></div>
              </form>
            </body>
          </html>""")
        
class SubmitPage(webapp2.RequestHandler):
    def post(self):
        user = MyData()
        user.content = self.request.get('content')
        user.put()
        self.redirect('/submit')
    def get(self):
        query = db.GqlQuery("SELECT *  FROM MyData")
        for contents in query:
            self.response.out.write('<html><body>You wrote:<pre>')
            self.response.out.write(contents.content)
            self.response.out.write('</pre></body></html>')

app = webapp2.WSGIApplication([('/', MainPage),
                              ('/submit', SubmitPage)],
                              debug=True)