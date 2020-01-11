#!/usr/bin/env python3

from setuptools import setup

requirements = [
    "pronouncing==0.2.0",
]

packages = [
    "lyrand",
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    description="lyrics generator",
    install_requires=requirements,
    license="UNLICENSE",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="lyrand",
    packages=packages,
    python_requires=">=3.6",
    scripts=[],
    url="https://github.com/radiand/lyrand",
    version="0.0.1",
)
