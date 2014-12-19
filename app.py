import webapp2
import os
import json

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        with open(os.path.join(os.getcwd(), 'index.html')) as fin:
            self.response.write(fin.read())

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=False)
