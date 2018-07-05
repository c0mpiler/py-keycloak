# -*- coding: utf-8 -*-

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='py-keycloak',
    version='0.0.1.3',
    url='https://github.com/c0mpiler/py-keycloak',
    license='Apache License 2.0',
    author='c0mpiler',
    author_email='c0mpiler@outlook.com',
    keywords='keycloak openid',
    long_description=long_description,
    long_description_content_type="text/markdown",
    description=u'py-keycloak is a Python package providing access to the Keycloak API.',
    packages=['keycloak', 'keycloak.authorization', 'keycloak.tests'],
    install_requires=['requests==2.18.4', 'httmock==1.2.5', 'python-jose==1.4.0'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 3 - Alpha',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Utilities'
    ]
)
