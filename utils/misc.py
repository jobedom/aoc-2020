import os

def init(filename):
   abspath = os.path.abspath(filename)
   dname = os.path.dirname(abspath)
   os.chdir(dname)
