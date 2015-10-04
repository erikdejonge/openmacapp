# coding=utf-8
"""
openmacapp
-
author  : rabshakeh (erik@a8.nl)
project : openmacapp
created : 02-06-15 / 15:21
"""

from setuptools import setup
setup(name='openmacapp',
      version='21',
      description='Search and start a mac app from the commandline',
      url='https://github.com/erikdejonge/openmacapp',
      author='Erik de Jonge',
      author_email='erik@a8.nl',
      license='GPL',
      entry_points={
          'console_scripts': [
              'openmacapp=openmacapp:main',
          ],
      },
      packages=['openmacapp'],
      zip_safe=True,
      install_requires=['arguments', 'consoleprinter'],
      classifiers=[
          "Programming Language :: Python :: 3",
          "Development Status :: 4 - Beta ",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
          "Operating System :: POSIX",
          "Environment :: MacOS X",
          "Topic :: System",
      ])
