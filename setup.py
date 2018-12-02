"""
falcon-jinja
------------
Jinja2 support for Falcon web framework
"""

import falcon_jinja
from setuptools import setup

setup(
    name='falcon_jinja',
    version=falcon_jinja.__version__,
    url='https://github.com/MichaelYusko/falcon-jinja',
    license=falcon_jinja.__license__,
    author=falcon_jinja.__author__,
    author_email='mikeiceman1221@gmail.com',
    description='Jinja2 support for Falcon',
    long_description=__doc__,
    packages=['falcon_jinja'],
    platforms='any',
    install_requires=[
        'jinja2',
        'falcon2'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]

)
