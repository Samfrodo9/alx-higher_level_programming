#!/usr/bin/python3

"""A module with class that returns a dict description"""


def class_to_json(obj):
    """A function that returns the dictionary description
    with simple data structure
     (list, dictionary, string, integer and boolean)
     for JSON serialization of an object"""

#    Check if the input object is an instance of a class
    if not hasattr(obj, '__dict__'):
        raise ValueError("Input is not an instance of a class.")

    # Initialize an empty dictionary to store the serialized data
    json_dict = {}

    # Iterate through the object's attributes
    for attr_name, attr_value in obj.__dict__.items():
        # Check if the attribute is serializable
        if (
            isinstance(attr_value, (list, dict, str, int, bool)) or
            (attr_value is None)
        ):
            # Add the attribute to the dictionary
            json_dict[attr_name] = attr_value

    return json_dict
