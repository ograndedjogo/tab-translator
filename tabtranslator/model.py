class Note(object):
	"""docstring for note"""
	def __init__(self, name, start=0, lenght=1):
		super(Note, self).__init__()
		self.name = name
		self.start = start
		self.lenght = lenght

class Bar(object):
	"""docstring for bar"""
	def __init__(self, lenght = 4):
		super(Bar, self).__init__()
		self.lenght = lenght
		self.notes = list()

	def add_note(note):
		self.notes.append(note)

class Stave(object):
	"""docstring for stave"""
	def __init__(self, name):
		super(Stave, self).__init__()
		self.name = name
		self.bars = list()

	def add_bar(bar):
		self.bars.append(bar)

class Tab(object):
	"""docstring for tab"""
	def __init__(self, name):
		super(Tab, self).__init__()
		self.name
		self.bars = list()

	def add_bar(bar):
		self.bars.append(bar)


