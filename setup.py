# -*- coding: utf-8 -*-

VERSION = (0, 0, 1)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

from setuptools import setup, find_packages

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="thread-genius",
    description='Thread Genius API Python Client',
    version=__versionstr__,
    author='Thread Genius',
    maintainer='Andrew Shum',
    maintainer_email='andrew@threadgenius.co',
    url='https://github.com/threadgenius/thread-genius-python',
    author_email='founders@threadgenius.co',
    install_requires=['future==0.15.2',
                       'requests==2.13.0',
                       'configparser==3.5.0',
                       'jsonschema==2.5.1',],
    packages=find_packages(),
    license="Apache 2.0"
)