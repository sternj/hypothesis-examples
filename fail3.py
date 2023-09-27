from hypothesis import given
from hypothesis.strategies import text

def reverse_string(s):
    return s[::-1]

def remove_spaces(s):
    return s.replace(" ", "")

@given(text())
def test_string_manipulation(s):
    reversed_s = reverse_string(s)
    assert reversed_s != s  # This check will fail if the string is not reversed.

    stripped_s = remove_spaces(s)
    assert stripped_s != s  # This check will fail if spaces are not removed.

    assert s == s.lower()  # This check will fail if the string is not in lowercase.


test_string_manipulation()
