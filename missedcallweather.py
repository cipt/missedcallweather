from webapp2 import WSGIApplication,RequestHandler
from sendSMS import send


class MyRequestHandler(RequestHandler):

    def get(self):
        number = self.request.get('msisdn')
        if (number == ''):
            self.response.out.write("Error")
        else:
            self.response.out.write("Received")


    def post(self):
        number = self.request.get('msisdn')


class MainPage(RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('')
        
application = WSGIApplication([('/', MyRequestHandler),], debug=True)
