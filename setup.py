#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'click>=6.7',
]

setup(
    name='rmount',
    py_modules=['rmount'],
    version='0.1',
    description="A wrapper to mount(/unmount) filesystems using sshfs.",
    long_description=readme,
    author="Simon Mutch",
    author_email='smutch.astro@gmail.com',
    url='https://github.com/smutch/rmount',
    entry_points={
        'console_scripts': [
            'rmount=rmount:rmount'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=True,
    keywords=['rmount', 'sshfs'],
    classifiers=[
        'Development Status :: 3 - Alpha'
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
)
