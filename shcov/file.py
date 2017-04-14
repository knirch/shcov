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

import pickle, os, stat

import hashlib


class File:
    def __init__(self, path, source_path = None):
        self.path = path
        if source_path == None:
            self.source_path = path
        else:
            self.source_path = source_path
        self.basename = os.path.basename(path)
        self.lines = {}

        m = hashlib.md5()
        with open(self.source_path) as f:
            m.update(f.read())

        st = os.lstat(self.source_path)
        self.source_file_ctime = st[stat.ST_CTIME]

        self.digest = m.digest()

    def get_source_ctime(self):
        """Return the creation time of the script"""
        return self.source_file_ctime

    def set_source_path(self, path):
        self.source_path = path

    def get_source_path(self):
        return self.source_path

    def save(self, path):
        outfile = open(path, 'wb')

        pickle.dump(self, outfile)
        outfile.close()

    def merge_object(self, obj):
        """Merge another object into this """

        for k,v in obj.lines.items():
            # Add the line numbering from the other
            if self.lines.has_key(k):
                self.lines[k] = self.lines[k] + v
            else:
                self.lines[k] = v

    def add_to_line(self, line_nr):
        line_nr = int(line_nr)
        try:
            self.lines[line_nr] = self.lines[line_nr] + 1
        except KeyError, e:
            self.lines[line_nr] = 1


def load(path, script_base = ''):
    file = pickle.load(open(path))
    with open(script_base + file.path) as f:
        m = hashlib.md5()
        m.update(f.read())
        digest = m.digest()

    # File has changed
    if digest != file.digest:
        file = File(file.path, source_path = script_base + file.path)

    file.set_source_path(script_base + file.path)
    return file
