# Filesystem API

Flask app to display file information from a filesystem 

## Setup

* `cd` to root directory of project
* Run shell script to setup example filesystem for demonstration purpose

    `bash ./mk_skelfs.sh`
* Setup virtualenv to install necessary packages

    `virtualenv venv`

    `source venv/bin/activate`

    `pip3 install -r requirements.txt`
* Run flask app by setting up `docker-compose`

    `docker-compose up -d`
* Run tests to ensure it passes

    `pytest`

## Usage

```
Usage: filesystem.py [-h] path uri

positional arguments:
  path        Relative file path
  uri         Resource to request

optional arguments:
  -h, --help  show this help message and exit

python3 filesystem.py <relative path> <request uri>

```

## Examples

```
$> python3 filesystem.py /filesystem/foo /

{
  "data": [
    {
      "name": ".DS_Store",
      "owner": "root",
      "permissions": "644",
      "size": "6148 bytes",
      "type": "file"
    },
    {
      "name": "foo1",
      "owner": "root",
      "permissions": "644",
      "size": "10 bytes",
      "type": "file"
    },
    {
      "name": "bar",
      "owner": "root",
      "permissions": "755",
      "size": "160 bytes",
      "type": "dir"
    }
  ]
}


$> python3 filesystem.py /filesystem/foo /foo1

Hello foo

$> python3 filesystem.py /filesystem/foo /bar

{
  "data": [
    {
      "name": ".DS_Store",
      "owner": "root",
      "permissions": "644",
      "size": "6148 bytes",
      "type": "file"
    },
    {
      "name": "bar1",
      "owner": "root",
      "permissions": "644",
      "size": "10 bytes",
      "type": "file"
    },
    {
      "name": "baz",
      "owner": "root",
      "permissions": "755",
      "size": "96 bytes",
      "type": "dir"
    }
  ]

```

### Using Postman or Insomnia REST client

Request URI: `http://locahost:5000`

JSON parameters as input:

```
{ "path" : "/filesystem/foo" }
```
