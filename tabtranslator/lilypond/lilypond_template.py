SHEET_TEMPLATE = """\version "2.18.2"
\header { }

\score {
  {{staffs}}
  \layout { }
  \midi { }
}
"""


STAFF_TEMPLATE = """\new Staff {
  \relative {
    \clef {{clef}}
    \time {{time_signature}}
    << {{notes}} >>
  }
}

"""

TAB_TEMPLATE = """\new TabStaff {
  \relative {
    \time {{time_signature}}
    << {{notes}} >>
  }
}
"""
