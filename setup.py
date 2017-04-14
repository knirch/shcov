# Copyright (C) 2008,  Simon Kagstrom
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

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
