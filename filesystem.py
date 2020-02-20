import requests
import sys
import argparse
import os
import json

parser = argparse.ArgumentParser()
parser.add_argument('uri', type=str, default = '/', help='Resource to request')
parser.add_argument('path', type=str, help='Relative file path')
parser.add_argument('base_path',
        type=str,
        nargs='?',
        default = os.environ['HOME'],
        help='Base filepath (default: Home)'
        )

args = parser.parse_args()

BASE_URL = 'http://127.0.0.1:5000'
uri = '{}/{}'.format(BASE_URL, args.uri)
data = { 'path' : args.path, 'base_path' : args.base_path }
response = requests.get(uri, data)

try:
    pretty_json = json.loads(response.text)
    print(json.dumps(pretty_json, indent=2))
except json.decoder.JSONDecodeError:
    print(response.text)
