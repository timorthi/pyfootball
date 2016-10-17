from setuptools import setup, find_packages
import os


if os.path.exists('README.rst'):
    readme_path = 'README.rst'
else:
    readme_path = 'README.md'

setup(
    name='pyfootball',
    version='1.0.0',
    description='A client library for the football-data.org REST API',
    long_description=open(readme_path).read(),
    url='https://github.com/xozzo/pyfootball',
    author='Timothy Ng',
    author_email='hello@timothyng.xyz',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5'
    ],

    keywords='api wrapper client library football data',

    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'venv']),

    install_requires=['requests'],

    test_suite='tests',

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['sphinx', 'sphinx-autobuild'],
        'test': ['coverage']
    }
)
