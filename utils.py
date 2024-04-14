# problem 1: sorting and adding elements to a list
def sort(collection):
    return sorted(collection)

def add_element(collection, element):
    if element not in collection:
        collection.append(element)
    return collection



# problem 2: json serialization/de-serialization
import json

def serialize(data):
    return json.dumps(data)

def deserialize(json_data):
    return json.loads(json_data)



# problem 3: color representation / conversion
from typing import NamedTuple

class Color(NamedTuple):
    red: int
    green: int
    blue: int

def pack_color(color: Color) -> list:
    return [color.red, color.green, color.blue]

def unpack_color(packed_color: list) -> Color:
    return Color(*packed_color)
