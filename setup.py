#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="ftir_classify",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
       'console_scripts': [
            'ftir_classify = ftir_classify.ftir_classify.main',
       ],
    },
    author="Andrew Low",
    author_email="andrew.low@canada.ca",
    url="https://github.com/lowandrew/FTIR_Classification",
    install_requires=['keras',
                      'numpy']
)
