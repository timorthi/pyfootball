#Contributing to pyfootball  

## Table of Contents
[**Before You Contribute**](#before-you-contribute)  
- [About pyfootball](#about-pyfootball)  
- [Setting Up](#setting-up)  
- [Issue Tracker](#issue-tracker)

[**Making Changes**](#making-changes)  
- [Coding Style](#coding-style)  
- [Tests](#tests)  
- [Documentation](#documentation)

[**Pull Requests**](#pull-requests)


## Before You Contribute  

### About pyfootball

pyfootball is a wrapper around the [football-data.org](http://football-data.org/) API. It is highly recommended that you familiarize yourself with its structure before using or working on pyfootball. To use or contribute to pyfootball, you're first going to need an API key for football-data; you can request for one [here](http://api.football-data.org/register).

### Setting Up

* Fork and clone the repository.  
* (Optional) Set up an isolated Python 3 environment with [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/). Do this if you don't want to pollute your global `site-packages` directory.
* Install the package and its dependencies: `pip install -e .[dev]`  

To verify that your installation works as expected, set up an envvar with your API key:  
` $ export PYFOOTBALL_API_KEY='your_api_key'`  
and then run the tests from the project's root directory:  
` $ python -m unittest`  
There is only one unit test that sends an actual request to football-data. Don't worry about exceeding your request limit.

### Issue Tracker  

The pyfootball issue tracker is located in the repository itself at [https://github.com/xozzo/pyfootball/issues](https://github.com/xozzo/pyfootball/issues). If you see something you'd like to work on, leave a comment on it so that other contributors will know. If there's something like you'd like to work on but it's not on the issue list, feel free to create an issue!

## Making Changes
### Coding Style
This project follows closely with the [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide, including but not limited to these rules:

* Set indentations to use 4 spaces
* Do not exceed 80 characters per line
* Use underscores as word separators in variable and method names: `my_var` instead of `myVar`
* Use CamelCase (first letter capitalized) for class names  

### Tests  
If you made any minor changes to the code base, be sure that the tests still pass. If you made any major changes (API-breaking changes or new functions/classes) to the code base, please overwrite an existing test or write a new test respectively.  

### Documentation  
If any changes were made to the code base, at the very least they should be reflected, in a descriptive manner, on the changelog page in the documentation. Classify the changes with either **[FEATURE]** for new features, **[FIX]** for bug fixes, **[DEV]** for changes to the dev environment, or **[OTHER]** for anything else. Do not worry about versioning; this will be decided by main contributors when you make a pull request.  

pyfootball uses the Sphinx tool to generate API documentation. Sphinx does this by parsing docstrings written in reStructuredText format. Have a look at the Sphinx [rST primer](http://www.sphinx-doc.org/en/stable/rest.html) and [autodoc page](http://www.sphinx-doc.org/en/1.4.8/ext/autodoc.html) for more information.


## Pull Requests  
Once you're done with testing your changes, submit a pull request to the **dev branch** of the [main repository](https://github.com/xozzo/pyfootball). If everything looks good, your pull request will be merged. If you were working on something listed in the issue tracker, be sure to reference the pull request in the respective issue.
