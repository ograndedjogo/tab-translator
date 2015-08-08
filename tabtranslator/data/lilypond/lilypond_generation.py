
# char2notes = { 
#   ' ':("a4 a4 ", "r2 "),
#   'a':("<c a>2 ", "<e' a'>2 "),
#   'b':("e2 ", "e'4 <e' g'> "),
#   'c':("g2 ", "d'4 e' "),
#   'd':("e2 ", "e'4 a' "),
#   'e':("<c g>2 ", "a'4 <a' c'> "),
#   'f':("a2 ", "<g' a'>4 c'' "),
#   'g':("a2 ", "<g' a'>4 a' "),
#   'h':("r4 g ", " r4 g' "),
#   'i':("<c e>2 ", "d'4 g' "),
#   'j':("a4 a ", "g'4 g' "),
#   'k':("a2 ", "<g' a'>4 g' "),
#   'l':("e4 g ", "a'4 a' "),
#   'm':("c4 e ", "a'4 g' "),
#   'n':("e4 c ", "a'4 g' "),
#   'o':("<c a g>2  ", "a'2 "),
#   'p':("a2 ", "e'4 <e' g'> "),
#   'q':("a2 ", "a'4 a' "),
#   'r':("g4 e ", "a'4 a' "),
#   's':("a2 ", "g'4 a' "),
#   't':("g2 ", "e'4 c' "),
#   'u':("<c e g>2  ", "<a' g'>2"),
#   'v':("e4 e ", "a'4 c' "),
#   'w':("e4 a ", "a'4 c' "),
#   'x':("r4 <c d> ", "g' a' "),
#   'y':("<c g>2  ", "<a' g'>2"),
#   'z':("<e a>2 ", "g'4 a' "),
#   '\n':("r1 r1 ", "r1 r1 "),
#   ',':("r2 ", "r2"),
#   '.':("<c e a>2 ", "<a c' e'>2")
# }
def unwrap_chord(chord):
  try:
      chord = chord.replace("<", "")
      chord = chord.replace(">", "")
  except:
    pass  # Do something

def build_lily_chord(chord, char2notes):
  notes = chord.split(" ")
  staff = ""
  for note in notes:
    staff += char2notes[note]
  print staff  
  staff = ''.join([i for i in staff if not i.isdigit()])
  print staff
  staff = "<" + staff + ">4 "
  print staff
  return staff

def __init_stave():
  staff = "\\version 2.18.2{\n\\new PianoStaff << \n"
  staff += "  \\new Staff {"
  # staff += "  \\new Staff { \clef bass " + lower_staff + "}\n"  
  return staff

def __end_stave():
  staff = "}\n"
  staff += ">>\n}\n"
  return staff

def __init_tab():
  staff = "\\new TabStaff{ \n"
  # staff += "  \\new Staff { \clef bass " + lower_staff + "}\n"  
  return staff

def __end_tab():
  staff = "}\n"
  return staff

def writte_ly_staff(txt, char2notes):
  first_staff = ""
  for i in txt:
    if len(i) is not 1: # if chord
      first_staff += build_lily_chord(i, char2notes)
    else:
      first_staff += char2notes[i]
  return first_staff

# Define note pitch and tempo
char2notes = {
  'A':"a4 ",
  'B':"b4 ",
  'C':'c\'4 ',
  'D':'d4 ',
  'E':'e4 ',
  'F':'f4 ',
  'G':'g4 ',
}



# Set of note and chords to be printed
txt = ["A", "B", "F", "A D B", "F", "B"] 

# writte with .ly syntax
first_staff = writte_ly_staff(txt, char2notes)

staff = __init_stave()
staff += first_staff  
staff += __end_stave()

tab_staff = __init_tab()
tab_staff += first_staff  
tab_staff += __end_tab()





# title = """\header {
#   title = "song1"
#   composer = "Lamaw"
# }"""

print tab_staff + "\n" + staff  # title +