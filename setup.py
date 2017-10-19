#!/usr/bin/env python3
import setuptools

setuptools.setup(
    name = "bson_upload",
    install_requires = {
        "django==2.0b1",
        "bson==0.5.0",
        "requests==2.18.4",
    },
)
