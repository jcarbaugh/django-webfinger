#!/usr/bin/env python
from setuptools import setup

setup(
    name='django-webfinger',
    packages=['webfinger'],
    version='0.2',
    requires=['django_wellknown', 'python_xrd']
)
