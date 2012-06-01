import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("""
          <html>
            <body>
              <form action="/submit" method="post">
                  <div>
                      <textarea name="content"></textarea>
                  </div>
                  <div>
                      <input type="submit" value="Sign Guestbook">
                  </div>
              </form>
            </body>
          </html>""")


class SubmitPage(webapp2.RequestHandler):
    def post(self):
        self.response.out.write('<html><body>You wrote:<p>')
        self.response.out.write(self.request.get('content'))
        self.response.out.write('</p></body></html>')

app = webapp2.WSGIApplication([('/', MainPage),('/submit', SubmitPage)],
                              debug=True)