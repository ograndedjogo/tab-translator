# coding: utf-8
from bottle import SimpleTemplate

class LilypondManager():
	"""Generates lilypong files from a sheet, thanks to a template engine"""
	def __init__():
		self.staff_type = None

	def __new_lilypond_sheet(self, staff_type):
		text = "\\version 2.18.2{\n\\new {{name}} << \n"
		text += "  \\new text {"	
		template = SimpleTemplate(text)
		return template.render(name = staff_type)

	def __end_lilypond_sheet(self):
		text = "}\n"
		text += ">>\n}\n"
		return text

	def __new_voice(self):
		pass

	def __print_note(self, note):
		self.get_note_representation()
		return text

def write_lilypond(sheet):
	txt = """\\version 2.18.2{\n\\new {{name}} << 
	  \\new Staff <<"""

	  


	txt+= ">>"
	#r8 r16 g e8. f16 g8[ c,] f e16 d
	#d16 c d8~ d16 b c8~ c16 b c8~ c16 b8.

def write_voice(voice, voicename):
	txt = """\\new Voice
	    { \\{} {{notes}} }""".format(voicename)

	 template = SimpleTemplate(txt)
	return template.render(notes = voice)
