# coding: utf-8
from tabtranslator.model import Sheet, Bar, Note

def test_Sheet():
    s = Sheet("Can't stop")
    assert s.name == "Can't stop"

def test_Bar():
    b = Bar()
    assert b.time_signature is not None, "No time_signature defined"
    assert iter(b.voices), "Notes in bar should be iterables"

def test_Note():
    n = Note(440)
    assert n.pitch == 440, "Pitch not defined"

    n = Note(421.678, duration=2)
    assert n.pitch == 421.678
    assert n.duration == 2


