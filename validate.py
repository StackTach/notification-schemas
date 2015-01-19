# Quick and dirty validator to check the schemas against the json-schema
# meta-schemas
import argparse
import json
from jsonschema import Draft4Validator
from jsonschema import exceptions as schemaexc
import sys


META_SCHEMA = 'json-schema.json'


def read_schema_file(schema_file):
    schema_str = ''
    with open(schema_file, 'r') as f:
        for line in f:
            # Comments aren't valid json, so remove them
            # Rather hacky, only works for single-line comments
            if not line.strip().startswith('//'):
                schema_str += line

    return schema_str


def main():
    parser = argparse.ArgumentParser(
        description='Validate a given schema against the json-schema '
                    'draft 4 meta-schema.')
    parser.add_argument('schema', metavar='schema_path',type=str,
                       help='Schema file to be validated.')
    parser.add_argument('-v', '--verbose', action='store_true',
                        dest='verbose',
                        help='Display all messages, not just errors.')
    args = parser.parse_args()
    schema_file = args.schema
    verbose = args.verbose

    if schema_file:
        schema_txt = read_schema_file(schema_file)
        schema = json.loads(schema_txt)
        try:
            Draft4Validator.check_schema(schema)
            if verbose:
                print("Schema %s: Passed" % schema_file)
        except schemaexc.SchemaError as e:
            print("Validation error: %s" % e.message)
            return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
