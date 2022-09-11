from os.path import isfile
from os.path import dirname

version_file = f'{dirname(__file__)}/version.txt'

if isfile(version_file):
    with open(version_file) as version_file:
        __version__ = version_file.read().strip()
