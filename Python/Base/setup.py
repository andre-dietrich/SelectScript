import os
from setuptools import setup

setup(
    name = "SelectScript",
    version = "0.2",
    author = "Andr"+unichr(233)+" Dietrich",
    author_email = "dietrich@ivs.cs.uni-magdeburg.de",
    description = ("Base implementation of the query-language SelectScript for Python."),
    license = "BSD",
    keywords = "query, language",
    url = "https://pypi.python.org/pypi/SelectScript/0.2",
    packages=['SelectScript'],
    long_description=open('README.md').read(),
    install_requires=['antlr_python_runtime'],
    #dependency_links = [],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
