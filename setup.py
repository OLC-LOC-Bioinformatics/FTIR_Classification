#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="ftir",
    version="0.0.1",
    packages=find_packages(),
    author="Andrew Low",
    author_email="andrew.low@canada.ca",
    url="https://github.com/lowandrew/FTIR_Classification",
    install_requires=['keras',
                      'numpy',
                      'pandas',
                      'tensorflow',
                      'matplotlib',
                      'scipy',
                      'scikit-learn']
)
