from flask import Flask, abort
from flask_restful import Resource, Api, reqparse
import os
import pwd
import stat

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('path', type=str, help='Filepath to browse contents')
parser.add_argument('base_path', type=str, help='Base filepath')

@app.route('/', defaults={'rel_path': ''}, methods=['GET'])
@app.route('/<path:rel_path>')
def index(rel_path):
    """Parses a filepath and returns its contents

    Takes a filepath and returns its contents whether directory or file

    Args:
        rel_path (str): filepath
    """
    args = parser.parse_args()
    abs_path = os.path.join(args['base_path'], args['path'], rel_path)
    if not os.path.exists(abs_path):
        return abort(404)

    if os.path.isfile(abs_path):
        return send_file(abs_path)

    files = os.listdir(abs_path)
    return directory_contents(abs_path)

def directory_contents(path):
    """Returns directory contents in form of json 

    Lists directory contents in a JSON body

    Args:
        path (str): directory path
    """
    json_body = { 'data' : [] }
    files = os.listdir(path)
    for file in files:
        file_attr = {}
        file_path = '{}/{}'.format(path, file)
        file_attr['name'] = os.path.basename(file_path)
        file_attr['owner'] = get_owner(file_path)
        file_attr['size'] = '{} bytes'.format(os.path.getsize(file_path))
        file_attr['permissions'] = get_permissions(file_path)
        if os.path.isfile(file_path):
            file_attr['type'] = 'file'
        else:
            file_attr['type'] = 'dir'
        json_body['data'].append(file_attr)
    return json_body

def send_file(path):
    """Returns text file content

    Reads a text file and returns its content

    Args:
        path (str): file path
    """
    file = open(path, 'r')
    return file.read()

def get_owner(path):
    """Get owner of file or directory

    Args:
        path (str): file path
    """
    stat = os.stat(path)
    return pwd.getpwuid(stat.st_uid)[0]

def get_permissions(path):
    """Get permission of file or directory in octal

    Args:
        path (str): file path
    """
    return oct(stat.S_IMODE(os.stat(path).st_mode))[-3:]

if __name__ == "__main__":
    app.run(debug=True)
