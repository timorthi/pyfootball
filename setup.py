from setuptools import setup, find_packages


setup(
    name='pyfootball',
    version='1.0.0-alpha',
    description='A Python API wrapper for football-data.org',
    url='https://github.com/xozzo/pyfootball',
    author='Timothy Ng',
    author_email='hello@timothyng.xyz',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
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
