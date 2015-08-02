class sheet(object):
	""" sheet: Top level object.
		Models the entire music sheet """
	def __init__(self, name):
		super(sheet, self).__init__()
		self.name = name
		self.bars = list()

class bar(object):
	""" bar: Models a measure.
		Compose the sheet as the temporal layer
			=> Where the notes are displayed on the sheet """
	def __init__(self, time_signature=4):
		super(bar, self).__init__()
		self.time_signature = time_signature
		self.notes = list()

class note(object):
	""" note: Models the unit in music representation
		Drives visual representation
			=> What note must be displayed on the sheet """
	def __init__(self, pitch, duration=1):
		super(bote, self).__init__()
		self.pitch = pitch
		self.duration = duration
