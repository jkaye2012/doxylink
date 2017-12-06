# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as stream:
    long_desc = stream.read()

requires = ['Sphinx>=0.6', 'pyparsing']

setup(
    name='sphinxcontrib-doxylink',
    version='1.5',
    url='http://sphinxcontrib-doxylink.readthedocs.io/en/stable/',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-doxylink',
    license='BSD',
    author='Matt Williams',
    author_email='matt@milliams.com',
    description='Sphinx extension for linking to Doxygen documentation.',
    long_description=long_desc,
    keywords=['sphinx', 'doxygen', 'documentation', 'c++'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    packages=find_packages(exclude=['doc', 'examples', 'html', 'tests']),
    install_requires=requires,
    python_requires='~=3.0',
    namespace_packages=['sphinxcontrib'],
)
