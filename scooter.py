import webapp2
from google.appengine.ext import ndb
import models
import json

class Scooter(webapp2.RequestHandler):
	#Add a scooter to the database
	def post(self):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports JSON"
			return
		new_Scoot = models.Scooter()
		name = self.request.get('name', default_value=None)
		engine = self.request.get('engine', default_value=None)
		year = self.request.get('year', default_value=None)
		man = self.request.get('man', default_value=None)
		if name:
			new_Scoot.name = name
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request"
		if engine:
			new_Scoot.engine = int(engine)
		if year:
			new_Scoot.year = int(year)
		if man:
			new_Scoot.man = (ndb.Key(models.Man, int(man)))
		key = new_Scoot.put()
		out = new_Scoot.to_dict()
		self.response.write(json.dumps(out))
		return

	#Get all the scooters from the database
	def get(self):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports JSON"
			return
		q = models.Scooter.query()
		for each in q:
			out = each.to_dict()
			self.response.write(json.dumps(out))
		return

	#Update the data of a scooter on the database
	def put(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports JSON"
			return
		if 'engine' in kwargs:
			engine = int(kwargs['engine'])
		if 'year' in kwargs:
			year = int(kwargs['year'])
		if 'mid' in kwargs:
			man = kwargs['mid']
			if not man:
				self.response.status = 404
				self.response.status_message = "man not found, p"
				return
		if 'sid' in kwargs:
			scooter = ndb.Key(models.Scooter, int(kwargs['sid'])).get()
			if not scooter:
				self.response.status = 404
				self.response.status_message = "scooter not found, p"
				return
			if engine:
				scooter.engine = engine
			if year:
				scooter.year = year
			if man:
				scooter.man = (ndb.Key(models.Scooter, int(man)))
			scooter.put()
			self.response.write('scooter id:' + kwargs['sid'] + ' has been updated.')
		return

	#Delete a scooter from the database
	def delete(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports JSON"
			return
		if 'sid' in kwargs:
			scooter = ndb.Key(models.Scooter, int(kwargs['sid']))
			if not scooter:
				self.response.status = 404
				self.response.status_message = "scooter not found, d"
				return
			scooter.delete()
			self.response.write('scooter id:' + kwargs['sid'] + ' has been deleted.')
		return

class ScooterSearch(webapp2.RequestHandler):
	#Search for a manufacturer by name and get the ID for it
	def post(self):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports JSON"
			return
		q = models.Scooter.query()
		if self.request.get('name', None):
			q = q.filter(models.Scooter.name == self.request.get('name'))
		keys = q.fetch(keys_only=True)
		results = { 'keys' : [x.id() for x in keys]}
		self.response.write(json.dumps(results))
		return