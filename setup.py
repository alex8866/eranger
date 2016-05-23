#!/usr/bin/env python
# This file is part of ranger, the console file manager.
# License: GNU GPL version 3, see the file "AUTHORS" for details.

import distutils.core
import os.path
import ranger

def _findall(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) \
            if os.path.isfile(os.path.join(directory, f))]

if __name__ == '__main__':
    distutils.core.setup(
        name='eranger',
        description='Extend for ranger, mainly add directory diff feature to it',
        long_description=ranger.__doc__,
        version=ranger.__version__,
        author=ranger.__author__,
        author_email=ranger.__email__,
        license=ranger.__license__,
        url='http://ranger.nongnu.org',
        AutoReqProv=False,
        scripts=['scripts/eranger', 'scripts/rifle'],
        data_files=[
            ('share/applications',
                ['doc/ranger.desktop']),
            ('share/doc/ranger',
                ['README.md',
                 'CHANGELOG.md',
                 'HACKING.md',
                 'doc/colorschemes.txt']),
            ('share/doc/ranger/config/colorschemes',
                _findall('doc/config/colorschemes')),
            ('share/doc/ranger/config', _findall('doc/config')),
            ('share/doc/ranger/tools', _findall('doc/tools')),
            ('share/doc/ranger/examples', _findall('examples')),
        ],
        package_data={'ranger': ['data/*', 'config/rc.conf',
            'config/rifle.conf']},
        packages=('ranger',
                  'ranger.api',
                  'ranger.colorschemes',
                  'ranger.container',
                  'ranger.core',
                  'ranger.config',
                  'ranger.ext',
                  'ranger.diff',
                  'ranger.gui',
                  'ranger.gui.widgets',
                  'ranger.ext.vcs'))
