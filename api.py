from flask import Flask, abort
from flask_restful import Resource, Api, reqparse
import os

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('path', type=str, help='Filepath to browse contents')

@app.route('/', defaults={'rel_path': ''}, methods=['GET'])
@app.route('/<path:rel_path>')
def index(rel_path):
    args = parser.parse_args()
    abs_path = os.path.join(os.getcwd(), args['path'], rel_path)
    if not os.path.exists(abs_path):
        return abort(404)

    if os.path.isfile(abs_path):
        return send_file(abs_path)

    files = os.listdir(abs_path)
    return directory_contents(abs_path)

def directory_contents(path):
    json_body = { 'data' : [] }
    files = os.listdir(path)
    for file in files:
        file_attr = {}
        file_path = '{}/{}'.format(path, file)
        if os.path.isfile(file_path):
            file_attr['name'] = os.path.basename(file_path)
            file_attr['type'] = 'file'
            file_attr['size'] = '{} bytes'.format(os.path.getsize(file_path))
        else:
            file_attr['name'] = file
            file_attr['type'] = 'dir'
        json_body['data'].append(file_attr)
    return json_body

def send_file(path):
    file = open(path, 'r')
    return file.read()

if __name__ == "__main__":
    app.run(debug=True)
