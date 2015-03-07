#!/usr/bin/env python

from distutils.core import setup

import glob
import os
import sys

SRC_DIR = 'src/'

d2p = lambda d: d[len(SRC_DIR):].replace('/', '.')
PACKAGES = [d2p(d) for d, dd, ff in os.walk(SRC_DIR) if '__init__.py' in ff]

DATA_FILES = [
    ('/opt/passant/bin', glob.glob('bin/*')),
    ('/usr/share/applications', ['data/passant.desktop']),

    ('/opt/passant/icons', glob.glob('data/*.png')),
    ('/opt/passant/icons', glob.glob('data/*.svg')),

    ('/opt/passant/qml', glob.glob('data/ui/qml/*.qml')),
    ('/opt/passant/qml/pieces/white', glob.glob('data/ui/qml/pieces/white/*.svg')),
    ('/opt/passant/qml/pieces/black', glob.glob('data/ui/qml/pieces/black/*.svg')),
]

sys.path.insert(0, SRC_DIR)
import passant

setup(
        name='passant',
        version=passant.__version__,
        description='Chess game',
        author='Jens Persson',
        author_email='xerxes2@gmail.com',
        url='http://github.org/xerxes2/passant',
        packages=PACKAGES,
        package_dir={ '': SRC_DIR },
        data_files=DATA_FILES,
)
