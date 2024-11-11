#!/usr/bin/env python

from setuptools import setup, find_packages
import subprocess

setup(name="singer-python",
      version='6.1.0',
      description="Singer.io utility library",
      author="Stitch",
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      url="http://singer.io",
      install_requires=[
          'pytz>=2024.2',
          'jsonschema>=4.23.0,==4.*',
          'simplejson>=3.19.3,==3.*',
          'python-dateutil>=2.9.0,==2.*',
          'backoff>=2.2.1,==2.*',
          'ciso8601>=2.3.1,==2.*',
      ],
      extras_require={
          'dev': [
              'pylint',
              'ipython',
              'ipdb',
              'nose',
              'singer-tools'
          ]
      },
      packages=find_packages(),
      package_data = {
          'singer': [
              'logging.conf'
              ]
          },
)
