# coding: utf-8
"""Basic integration tests for tabtranslator package"""

def test_initialization():
    """Check the test suite runs by affirming 2+2=4"""
    assert 2+2 == 4

def test_import():
    """Ensure the test suite can import our module"""
    try:
        import tabtranslator
    except ImportError:
        assert False, "Was not able to import the tabtranslator module"
