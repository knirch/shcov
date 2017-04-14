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

import cPickle as pickle
import os
import stat
import hashlib


class File(object):
    def __init__(self, path, source_path=None):
        self.path = path
        if source_path is None:
            self.source_path = path
        else:
            self.source_path = source_path
        self.basename = os.path.basename(path)
        self.lines = {}

        m = hashlib.md5()
        with open(self.source_path) as f:
            m.update(f.read())

        st = os.lstat(self.source_path)
        self.ctime = st[stat.ST_CTIME]

        self.digest = m.digest()

    def save(self, path):
        with open(path, 'wb') as outfile:
            pickle.dump(self, outfile, 2)

    def merge_object(self, obj):
        """Merge another object into this """

        for k, v in obj.lines.iteritems():
            # Add the line numbering from the other
            if k in self.lines:
                self.lines[k] = self.lines[k] + v
            else:
                self.lines[k] = v

    def add_to_line(self, line_nr):
        line_nr = int(line_nr)
        try:
            self.lines[line_nr] = self.lines[line_nr] + 1
        except KeyError:
            self.lines[line_nr] = 1


def load(path, script_base=''):
    with open(path, 'rb') as p:
        sourcefile = pickle.load(p)

    with open(script_base + sourcefile.path) as f:
        m = hashlib.md5()
        m.update(f.read())
        digest = m.digest()

    # File has changed
    if digest != sourcefile.digest:
        sourcefile = File(sourcefile.path, source_path=script_base + sourcefile.path)

    sourcefile.source_path = script_base + sourcefile.path
    return sourcefile
