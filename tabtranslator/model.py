class sheet(object):
	"""docstring for sheet"""
	def __init__(self, name):
		super(sheet, self).__init__()
		self.name = name
		self.bars = list()
		
	def add_bar(bar):
		self.bars.append(bar)

class Stave(sheet):
	"""docstring for stave"""
	def __init__(self):
		super(Stave, self).__init__()


class Tab(sheet):
	"""docstring for tab"""
	def __init__(self):
		super(Tab, self).__init__()


class Bar(object):
	"""docstring for bar"""
	def __init__(self, cycle = 4):
		super(Bar, self).__init__()
		self.cycle = cycle
		self.notes = dict()

	def add_note(note, start_time):
		self.notes[note] = start_time

class Note(object):
	"""docstring for note"""
	def __init__(self, pitch, duration=1):
		super(Note, self).__init__()
		self.pitch = pitch
		self.duration = duration