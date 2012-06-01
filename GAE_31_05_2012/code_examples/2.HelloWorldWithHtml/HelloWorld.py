import webapp2

class MainPage(webapp2.RequestHandler):
  def get(self):
      self.response.out.write("""
          <html>
            <body>
	      <h1>Hello</p>
	      <p>World !!!</p>
            </body>
          </html>
      """)

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True) 
 
