#! /usr/bin/env python

import os
import sys
import textwrap

from setuptools import setup

if __name__ == "__main__":
	
	setup(
	    name='botgameline',
	    version='0.0.1',
	    install_requires=[
	        'requests',
	        'humanize',
			'six',
			'rsa',
			'bs4',
			'schematics',
			'humanfriendly',
			'gtts',
			'googletrans',
			'wikiapi',
	        'importlib-metadata; python_version >= "3.8"',
	    ],
	)