
class note(object):
	"""docstring for note"""
	def __init__(self, name, start=0, lenght=1):
		super(note, self).__init__()
		self.name = name
		self.start = start
		self.lenght = lenght


class bar(object):
	"""docstring for bar"""
	def __init__(self, lenght = 4):
		super(bar, self).__init__()
		self.lenght = lenght
		self.notes = list()

	def add_note(note):
		self.notes.append(note)
		
class stave(object):
	"""docstring for stave"""
	def __init__(self, name):
		super(stave, self).__init__()
		self.name = name
		self.bars = list()

	def add_bar(bar):
		self.bars.append(bar)
		
class tab(object):
	"""docstring for tab"""
	def __init__(self, name):
		super(tab, self).__init__()
		self.name
		self.bars = list()

	def add_bar(bar):
		self.bars.append(bar)

		