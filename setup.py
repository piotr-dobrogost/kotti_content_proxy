# -*- coding: utf-8 -*-

"""
Created on 2014-09-23
:author: Andreas Kaiser (disko)
"""

import os

from setuptools import find_packages
from setuptools import setup

version = '0.1dev'
project = 'kotti_content_proxy'

install_requires = [
    'Kotti',
],

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

setup(
    name=project,
    version=version,
    description="A content type that proxies other content in a Kotti site",  # noqa
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "License :: Repoze Public License",
    ],
    keywords='kotti addon',
    author='Andreas Kaiser',
    author_email='disko@binary-punks.com',
    url='https://github.com/Kotti',
    license='bsd',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=[],
    entry_points={
        'fanstatic.libraries': [
            'kotti_content_proxy = kotti_content_proxy.fanstatic:library',
        ],
    },
    extras_require={},
    message_extractors={
        'kotti_content_proxy': [
            ('**.py', 'lingua_python', None),
            ('**.zcml', 'lingua_xml', None),
            ('**.pt', 'lingua_xml', None),
        ]
    },
)