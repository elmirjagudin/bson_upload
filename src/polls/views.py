from django.shortcuts import render

from django.http import HttpResponse
from django import http
import bson
from os import path
import os


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def somejson(request):
    file_desc = bson.loads(request.body)

    dest_file = path.join("uploaded", file_desc["filename"])

    print("filename: %s" % dest_file)
    os.makedirs("uploaded", exist_ok=True)

    open(dest_file, "wb").write(file_desc["bin"])

    return http.JsonResponse(dict(res="ok"))

