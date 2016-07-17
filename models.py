from google.appengine.ext import ndb

class Model(ndb.Model):
	def to_dict(self):
		d = super(Model, self).to_dict()
		d['key'] = self.key.id()
		return d

class Man(Model):
	mname = ndb.StringProperty(required=True)
	country = ndb.StringProperty()

class Scooter(Model):
	name = ndb.StringProperty(required=True)
	engine = ndb.IntegerProperty()
	year = ndb.IntegerProperty()
	man = ndb.KeyProperty()

	def to_dict(self):
		d = super(Scooter, self).to_dict()
		d['man'] = self.key.id()
		return d