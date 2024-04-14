from hypothesis import given
from hypothesis.strategies import integers

from utils import pack_color, unpack_color, Color

# property test for packing/unpacking
@given(integers(min_value=0, max_value=255), integers(min_value=0, max_value=255), integers(min_value=0, max_value=255))
def test_packing_unpacking_inverses(red, green, blue):
    color = Color(red, green, blue)
    packed_color = pack_color(color)
    unpacked_color = unpack_color(packed_color)
    assert unpacked_color == color
