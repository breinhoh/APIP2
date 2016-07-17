import webapp2
from google.appengine.api import oauth

app = webapp2.WSGIApplication([
	('/man', 'man.Man'),
], debug=True)
app.router.add(webapp2.Route(r'/man/search', 'man.ManSearch'))
app.router.add(webapp2.Route(r'/scooter', 'scooter.Scooter'))
app.router.add(webapp2.Route(r'/scooter/search', 'scooter.ScooterSearch'))
app.router.add(webapp2.Route(r'/scooter/<sid:[0-9]+><:/?>', 'scooter.Scooter'))
app.router.add(webapp2.Route(r'/scooter/<sid:[0-9]+>/engine/<engine:[0-9]+><:/?>', 'scooter.Scooter'))
app.router.add(webapp2.Route(r'/scooter/<sid:[0-9]+>/year/<year:[0-9]+><:/?>', 'scooter.Scooter'))
app.router.add(webapp2.Route(r'/scooter/<sid:[0-9]+>/man/<mid:[0-9]+><:/?>', 'scooter.Scooter'))
app.router.add(webapp2.Route(r'/scooter/<sid:[0-9]+>/engine/<engine:[0-9]+>/year/<year:[0-9]+><:/?>', 'scooter.Scooter'))
app.router.add(webapp2.Route(r'/scooter/<sid:[0-9]+>/engine/<engine:[0-9]+>/man/<mid:[0-9]+><:/?>', 'scooter.Scooter'))
app.router.add(webapp2.Route(r'/scooter/<sid:[0-9]+>/year/<year:[0-9]+>/man/<mid:[0-9]+><:/?>', 'scooter.Scooter'))
app.router.add(webapp2.Route(r'/scooter/<sid:[0-9]+>/engine/<engine:[0-9]+>/year/<year:[0-9]+>/man/<mid:[0-9]+><:/?>', 'scooter.Scooter'))