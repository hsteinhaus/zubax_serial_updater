#!/usr/bin/env python3
#
# Copyright (C) 2014 Pavel Kirienko <pavel.kirienko@zubax.com>
#

import sys
import glob
from distutils.core import setup
from cx_Freeze import setup, Executable

base = 'Win32GUI' if sys.platform == 'win32' else None

binaries = glob.glob('*.bin')
if len(binaries) == 0:
    raise Exception('Could not find binaries')

build_exe_options = {
    'packages': ['serial', 'tkinter'],
    'include_msvcr': True,
    'include_files': binaries
}

bdist_msi_options = {
    'initial_target_dir': r'[ProgramFilesFolder]\Zubax\serial_updater',
}

setup(
    name='zubax_serial_updater',
    version='1.0',
    description='Zubax serial firmware updater',
    requires=['serial'],
    author='Pavel Kirienko',
    author_email='pavel.kirienko@zubax.com',
    url='http://zubax.com',
    license='MIT',
    options={
        'build_exe': build_exe_options,
        'bdist_msi': bdist_msi_options
    },
    executables=[Executable('zubax_serial_updater',
                            base=base,
                            icon='icon.ico',
                            shortcutName='Zubax Serial Updater',
                            shortcutDir='ProgramMenuFolder')]
)
