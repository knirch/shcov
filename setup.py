######################################################################
##
## Copyright (C) 2008,  Simon Kagstrom
##
## Filename:      setup.py
## Author:        Simon Kagstrom <simon.kagstrom@gmail.se>
## Description:   Installation script (from Dissy)
##
## $Id:$
##
######################################################################
import sys
from distutils.core import setup

setup(name='shcov',
      version='5',
      description="A gcov and lcov coverage test tool for bourne shell / bash scripts",
      author="Simon Kagstrom",
      url="http://shcov.googlecode.com",
      author_email="simon.kagstrom@gmail.se",

      packages = ['shcov'],
      scripts = ['scripts/shlcov'],
      package_data = {'shcov' : ['data/gcov.css', 'data/*.png']},

      data_files=[('share/doc/shcov/', ['README']),
                  ('share/doc/shcov/', ['COPYING']),
                  ('share/man/man1/', ['shcov.1', 'shlcov.1']),
                  ],
      )
