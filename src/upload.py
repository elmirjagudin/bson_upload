#!/usr/bin/env python3

import requests
import bson
import sys
from os import path


def get_filename():
    if len(sys.argv) < 2:
        print("I need a file name")
        sys.exit(1)

    return sys.argv[1]

#data = bson.dumps(dict(b="son", ft="w"))
#r = requests.post("http://127.0.0.1:8000/polls/somejson", data=data)
#print("heead")

file_name = get_filename()

data = dict(filename=path.basename(file_name))
data["bin"] = open(file_name, mode="rb").read()

r = requests.post(
    "http://127.0.0.1:8000/polls/somejson",
    data=bson.dumps(data))

print("%s\n%s" % (r.status_code, r.text))