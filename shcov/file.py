######################################################################
##
## Copyright (C) 2008,  Simon Kagstrom
##
## Filename:      shcov_file.py
## Author:        Simon Kagstrom <simon.kagstrom@gmail.com>
## Description:   The shcov file class
##
## $Id:$
##
######################################################################
import pickle, os, stat

try:
    import hashlib
    has_hashlib = True
except:
    import md5
    has_hashlib = False

from utils import *

def md5_new():
    if has_hashlib:
        return hashlib.md5()
    return md5.new()

class File:
    def __init__(self, path, source_path = None):
        self.path = path
        if source_path == None:
            self.source_path = path
        else:
            self.source_path = source_path
        self.basename = os.path.basename(path)
        self.lines = {}

        m = md5_new()
        m.update(read_file(self.source_path))

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
    source_file = read_file(script_base + file.path)

    m = md5_new()
    m.update(source_file)
    digest = m.digest()

    # File has changed
    if digest != file.digest:
        file = File(file.path, source_path = script_base + file.path)

    file.set_source_path(script_base + file.path)
    return file
