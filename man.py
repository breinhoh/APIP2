import webapp2
from google.appengine.ext import ndb
import models
import json

class Man(webapp2.RequestHandler):
	#Add a manufacturer to the database
	def post(self):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports JSON"
			return
		new_Man = models.Man()
		mname = self.request.get('mname', default_value=None)
		country = self.request.get('country', default_value=None)
		if mname:
			new_Man.mname = mname
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request"
		if country:
			new_Man.country = country
		key = new_Man.put()
		out = new_Man.to_dict()
		self.response.write(json.dumps(out))
		return

	#Get all the manufacturers from the database
	def get(self):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports JSON"
			return
		q = models.Man.query()
		for each in q:
			out = each.to_dict()
			self.response.write(json.dumps(out))
		return

class ManSearch(webapp2.RequestHandler):
	#Search for a manufacturer by name and get the ID for it
	def post(self):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports JSON"
			return
		q = models.Man.query()
		if self.request.get('mname', None):
			q = q.filter(models.Man.mname == self.request.get('mname'))
		if self.request.get('country', None):
			q = q.filter(models.Man.country == self.request.get('country'))
		keys = q.fetch(keys_only=True)
		results = { 'keys' : [x.id() for x in keys]}
		self.response.write(json.dumps(results))
		return