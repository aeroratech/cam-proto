import os
import subprocess
import sys

from distutils.command.build import build
from distutils.spawn import find_executable
from setuptools import setup

def parse_requirements(filename):
    """
    Helper which parses requirement_?.*.txt files

    :param filename: relative path, e.g. `./requirements.txt`
    :returns: List of requirements
    """

    # Get absolute filepath
    filepath = os.path.join(os.getcwd(), filename)

    # Check if file exists
    if not os.path.exists(filepath):
        print("[!] File {} not found".format(filename))
        return []

    # Parse install requirements
    with open(filepath, encoding="utf-8") as f:
        return [requires.strip() for requires in f.readlines()]

setup(
    name="protoc-gen-mavcam",
    version="0.1.1",
    description="Protoc plugin used to generate MAVCAM bindings",
    url="https://github.com/mavlink/MAVSDK-Proto",
    maintainer="Jonas Vautherin, Julian Oes",
    maintainer_email="jonas.vautherin@gmail.com, julian@oes.ch",

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
    ],

    packages=["protoc_gen_mavcam"],
    install_requires=parse_requirements("requirements.txt"),
    entry_points={
        "console_scripts": [
            "protoc-gen-mavcam= protoc_gen_mavcam.__main__:main"
        ]
    }
)
