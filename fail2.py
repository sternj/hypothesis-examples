from hypothesis import given
from hypothesis.strategies import integers

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

@given(integers(), integers())
def test_divide(a, b):
    result = divide(a, b)
    assert result == a / b

test_divide()
