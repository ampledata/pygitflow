#!/usr/bin/env python
"""Pythonic Setup for Git Flow."""


import setuptools

import gflib


setuptools.setup(
    version='1.0.0',
    name='pygitflow',
    description='Pythonic Installer for Git Flow.',
    author='Greg Albrecht',
    author_email='gba@splunk.com',
    license='Apache License 2.0',
    url='https://github.com/ampledata/pygitflow',
    scripts=gflib.get_gitflow(),
    setup_requires=['nose'],
    tests_require=['nose', 'coverage', 'nose-cov'],
)
