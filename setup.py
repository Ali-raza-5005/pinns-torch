#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="pinnstorch",
    version="0.0.1",
    description="An implementaion of PINNs using Lightning and Hydra.",
    author="",
    author_email="reza.akbarianbafghi@coloardo.edu",
    url="https://github.com/rezaakb/pinns-torch",
    install_requires=["lightning", "hydra-core", "scipy", "PyDOE"],
    packages=find_packages(),
    # use this to customize global commands available in the terminal after installing the package
    entry_points={
        "console_scripts": [
            "train_command = src.train:main",
            "eval_command = src.eval:main",
        ]
    },
)