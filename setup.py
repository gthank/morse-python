# -*- python; coding: utf-8 -*-
from distutils.core import setup

setup(
    name='python-morse',
    version='1.1',
    packages=['python-morse', 'python-morse.test'],
    scripts=['bin/cycle.sh', 'bin/example.bat', 'bin/rndwords.bat'],
    license='GPLv2',
    description='A Python library for Morse code.',
    long_description=open('README.md').read(),
    author='Christian Höltje',
    author_email='docwhat@gerf.org',
    url='https://github.com/docwhat/morse-python'
)

