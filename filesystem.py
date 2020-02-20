import requests
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('path', type=str, help='Relative file path')
parser.add_argument('uri', type=str, default = '/', help='Resource to request')

args = parser.parse_args()

BASE_URL = 'http://127.0.0.1:5000'
uri = '{}/{}'.format(BASE_URL, args.uri)
data = { 'path' : args.path }
response = requests.get(uri, data)

try:
    pretty_json = json.loads(response.text)
    print(json.dumps(pretty_json, indent=2))
except json.decoder.JSONDecodeError:
    print(response.text)
