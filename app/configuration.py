# -*- encoding: utf-8 -*-

class Config(object):
	"""
	Configuration base, for all environments.
	"""
	DEBUG = False
	TESTING = False
	#element to be used to look for train ticket
	USER_DETAILS = {'nom': 'maxime',
                    'prenom': 'lhoumeau',
                    'age': '25',
                    'user-id': '311900723',
                    'cards-id': ['13653993'],
                    'token': 'MA6GdheENfAnQjoHGyC3'
                    }
	DEPARTURE = "Paris"
	ARRIVAL = "Bordeaux"
	DATE = ""
	#mail to notify
	SENDER_EMAIL = 'lhokhofr@gmail.com'
	SENDER_PASSWORD = 'porcolhokho'
	USER_NOTIFICATIONS = 'lhoumeau.maxime@gmail.com'

class ProductionConfig(Config):
	DEBUG = True

class DevelopmentConfig(Config):
	DEBUG = True

class TestingConfig(Config):
	TESTING = True
