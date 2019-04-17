# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Sample package description',
    long_description=readme,
    author='<author_name>',
    author_email='author@example.com',
    url='',
    license=license,
    packages=find_packages(exclude=())
)
