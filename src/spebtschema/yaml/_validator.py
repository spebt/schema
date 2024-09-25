import sys
import json as _json

from jsonschema import Draft7Validator
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT7

if sys.version_info < (3, 10):
    from importlib_resources import files as _files
else:
    from importlib.resources import files as _files


def __get_schema_registry(version: str = "v1"):
    # Load the schema
    _schema_dir = _files(f"spebtschema.{version}")
    _basenames = ["main", "detector", "relation", "FOV", "transformation_data"]

    schema_registry = Registry()
    for _basename in _basenames:
        loaded = Resource(
            contents=_json.load(open(f"{str(_schema_dir)}/{_basename}.json", "r")),
            specification=DRAFT7,
        )

        schema_registry = loaded @ schema_registry
    return schema_registry


def validate(input: dict, name: str, version: str = "v1"):
    """
    Validates the given JSON data against the provided schema.
    """
    # Get the schema registry
    schema_registry = __get_schema_registry()

    # Validate the JSON data
    validator = Draft7Validator(
        schema_registry[f"/{version}/{name}.json"].contents, registry=schema_registry
    )

    try:
        validator.validate(input)
    except Exception as e:
        raise e
