#!/usr/bin/env python

import os.path
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='p2p-sip',
      version='2.2.0',
      description='A pure python SIP implementation and P2P SIP client.',
      author='Kundan Singh',
      author_email='kundan10@gmail.com',
      url='https://github.com/descent/p2p-sip',
      install_requires=('multitask',),
      packages=find_packages(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ])
