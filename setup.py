import os
from setuptools import setup, find_packages

from redirects import VERSION

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
    
requirements = [
    "Django >= 1.2",
]

setup(
    name = "Django Redirect Middleware",
    version = ".".join(map(str, VERSION)),
    description = "Remake of standart Django redirect middleware",
    long_description = read('README.rst'),
    url = '',
    license = 'BSD',
    author = 'Dmitry Sobolev',
    author_email = 'dmitry.sobolev@redsolution.ru',
    packages = find_packages(exclude=['tests']),
    install_requires = requirements,
)
