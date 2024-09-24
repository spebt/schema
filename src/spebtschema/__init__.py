"""
==================
SPEBT Schema Module 
===================

JSON Schema validator module for the SPEBT detector configuration YAML file.

The validator is used to validate the YAML files against the predefined JSON schema. 
It checks the structure and data types of the JSON data to ensure they match the schema. 
If the JSON data is not valid according to the schema, the validator will raise an exception.

Functions:
- validate(json_data, schema): Validates the given JSON data against the provided schema.
"""

__all__ = ["yaml"]

import yaml
