import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "SelectScript_ODE",
    version = "1",
    author = "Andr"+unichr(233)+" Dietrich",
    author_email = "dietrich@ivs.cs.uni-magdeburg.de",
    description = ("Implementation of the query-language SelectScript for ODE-Python."),
    license = "BSD",
    keywords = "ode, pyode, query, language, SelectScript",
    url = "https://pypi.python.org/pypi/SelectScript_ODE/1",
    packages=['SelectScript_ODE', 'SelectScript_ODE.examples'],
    long_description=read('README.md'),
    install_requires=['antlr_python_runtime','SelectScript'],
    #dependency_links = [],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
