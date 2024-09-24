import sys

from jsonschema import Draft7Validator
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT7

if sys.version_info < (3, 10):
    from importlib_resources import files as _files
else:
    from importlib.resources import files as _files


def __get_schema_registry():
    # Load the schema
    # _schema_dir = _resources.files(_schema)
    _schema_dir = _files("")
    _schema_version = "v1"
    _basenames = ["main", "detector", "relation", "FOV", "transformation_data"]

    schema_registry = Registry()
    for _basename in _basenames:
        loaded = Resource(
            contents=_json.load(
                open(_schema_dir / _schema_version / f"{_basename}.json", "r")
            ),
            specification=DRAFT7,
        )

        schema_registry = loaded @ schema_registry
    return schema_registry
