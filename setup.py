import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "EmpireAPIWrapper",
    version = "0.0.1",
    author = "Scott Fraser",
    author_email = "quincy.fraser@gmail.com",
    description = ("A Python wrapper for the Empire API"),
    license = "Apache v2.0",
    keywords = "Powershell Empire",
    url = "https://github.com/radioboyQ/EmpireAPIWrapper",
    packages=['requests'],
    long_description=read('README.md'),
)
