from hypothesis import given
from hypothesis.strategies import lists, integers

from utils import sort, add_element

# property test for sorting
@given(lists(integers()))
def test_sorting_preserves_size(lst):
    sorted_lst = sort(lst)
    assert len(lst) == len(sorted_lst)

# property test for adding element
@given(lists(integers()), integers())
def test_adding_element_preserves_size(lst, element):
    new_lst = add_element(lst, element)
    assert len(new_lst) >= len(lst)  # adding should not decrease size