# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

version = '0.0.2'


setup(
    name='pickleclip',
    packages=find_packages(exclude=['tests']),
    package_data={
        'pickleclip': [],
    },
    install_requires=[
        'pyperclip>=1.5.27',
        'six>=1.10.0',
        'dill>=0.2.6'
    ],
    zip_safe=False,
    version=version,
    description='Simple clipboard tool for Python pickled objects.',
    author='Victor Ferraz',
    author_email='victorfsf.dev@gmail.com',
    url='https://github.com/victorfsf/pickleclip',
    keywords=[
        'pickle',
        'pickleclip',
        'clipboard',
        'clip',
        'python',
        'python2',
        'python3',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
