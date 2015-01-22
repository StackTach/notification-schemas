import argparse
import jsonschema
import json
import os
import sys


def read_json_file(json_file):
    json_str = ''
    with open(json_file, 'r') as f:
        for line in f:
            # Comments aren't valid json, so remove them
            # Rather hacky, only works for single-line comments
            if not line.strip().startswith('//'):
                json_str += line

    return json.loads(json_str)


def main():
    parser = argparse.ArgumentParser(
        description='Validate a given payload against the given schema.')
    parser.add_argument('--schema', metavar='SCHEMA_PATH', type=str,
                       help='Schema file to validate against.')
    parser.add_argument('--payload', metavar='PAYLOAD_PATH', type=str,
                        help='Payload file to validate.')
    args = parser.parse_args()
    schema_file = args.schema
    payload_file = args.payload
    errors = 0

    if schema_file is not None and payload_file is not None:
        project_path = os.path.dirname(os.path.abspath(schema_file)) + os.sep
        schema = read_json_file(schema_file)
        payload = read_json_file(payload_file)
        validator = jsonschema.Draft4Validator(schema)
        validator.resolver = jsonschema.RefResolver(
            base_uri='file://%s' % project_path,
            referrer=None)
        for error in validator.iter_errors(payload):
            print(str(error))
            errors += 1
            break

    return errors

if __name__ == '__main__':
    sys.exit(main())

