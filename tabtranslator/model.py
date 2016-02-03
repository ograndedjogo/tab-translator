# coding: utf-8

class Sheet(object):
	""" sheet: Top level object.
		Models the entire music sheet """
	def __init__(self, name):
		super(Sheet, self).__init__()
		self.name = name
		self.bars = list()

class Bar(object):
	""" bar: Models a measure.
		Compose the sheet as the temporal layer
			=> Where the notes are displayed on the sheet """
	def __init__(self, time_signature=4):
		super(Bar, self).__init__()
		self.time_signature = time_signature
		self.voices = list()

class Note(object):
	""" note: Models the unit in music representation"""
	def __init__(self, pitch, duration=1):
		super(Note, self).__init__()
		self.pitch = pitch
		self.duration = duration
