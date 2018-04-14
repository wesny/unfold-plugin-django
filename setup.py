#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages


setup(name='unfold-plugin-django',
      version='0.1.0',
      description='Unfold plugin to support payments in Django backends',
      keywords='unfold-django-plugin',
      author='Sweyn Venderbush',
      author_email='sweyn.venderbush@yale.edu',
      url='https://github.com/wesny/unfold-plugin-django',
      license='3-clause BSD',
      long_description=open('README.md').read(),
      zip_safe=False,
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Development Status :: 1 - Planning',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   ],
      packages=find_packages(exclude=('tests',)),
      include_package_data=True,
      install_requires=[
            "requests==2.18.4",
            "django==2.0"
      ],
      python_requires='>=3',
      )
