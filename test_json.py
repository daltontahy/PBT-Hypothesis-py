from hypothesis import given
from hypothesis.strategies import dictionaries, text

from utils import serialize, deserialize

# property test for serialization/deserialization
@given(dictionaries(text(), text()))
def test_serialization_deserialization_inverses(data):
    serialized_data = serialize(data)
    deserialized_data = deserialize(serialized_data)
    assert deserialized_data == data
