class sheet(object):
	""" sheet: Top level object. 
		Models the entire music sheet """
	def __init__(self, name):
		super(sheet, self).__init__()
		self.name = name
		self.bars = list()
		
	def add_bar(bar):
		self.bars.append(bar)

class stave(sheet):
	""" stave: sheet that is displayed in music theory representation"""
	def __init__(self):
		super(stave, self).__init__()


class tab(sheet):
	""" tab: sheet that is displayed with tab representation"""
	def __init__(self):
		super(tab, self).__init__()


class bar(object):
	""" bar: Models a measure.
		Compose the sheet as the temporal layer
			=> Where the notes are displayed on the sheet """
	def __init__(self, cycle=4):
		super(bar, self).__init__()
		self.cycle = cycle
		self.notes = dict()

	def add_note(self, note, start_time):
		"""
		note : note : note instance
		start_time : int : start time inside the measure
		"""
		self.notes[note] = start_time

class note(object):
	""" note: Models the unit in music representation 
		Drives visual representation
			=> What note must be displayed on the sheet
		"""
	def __init__(self, pitch, duration=1):
		super(bote, self).__init__()
		self.pitch = pitch
		self.duration = duration