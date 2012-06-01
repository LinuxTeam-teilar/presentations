import webapp2

class MainPage(webapp2.RequestHandler):
  def get(self):
      self.response.out.write("""<html>
				  <body>
				    <h1>hello,</h1>
				    <p>world</p>
				  </body>
				 </html>""")

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)