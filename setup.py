import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Dwell in you richly",
    version = "0.0.1",
    author = "Miguel Alex Cantu",
    author_email = "miguel.can2@gmail.com	",
    description = ("An interactive program that hollows out text files"
                   "with verses, references, and ministry excerpts."),
    license = "BSD",
    keywords = "Study Bible, Memorize Bible",
    packages=['diyr'],
    long_description=read('README.md'),
    entry_points = {
        'console_scripts': [
            'diyr = diyr.main:main'
        ]
    }
    
)
