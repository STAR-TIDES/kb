'''Tests for objects in the availability.py file.'''

from .availability import Availability

def test_all_values_present():
    got = {e.name for e in list(Availability)}
    want = {'UNSPECIFIED', 'UNAVAILABLE', 'AVAILABLE'}
    assert got == want
