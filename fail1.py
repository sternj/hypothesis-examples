from hypothesis import given
from hypothesis.strategies import lists, integers

def my_sort(lst):
    # Incorrect sorting implementation
    return lst[::-1]

@given(lists(integers()))
def test_sorting(lst):
    sorted_lst = my_sort(lst)
    assert sorted_lst == sorted(lst)

# This test will fail because 'my_sort' sorts the list in reverse order.

test_sorting()
