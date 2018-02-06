# django-registration-invite

[![Build Status](https://travis-ci.org/rpkilby/django-registration-invite.svg?branch=master)](https://travis-ci.org/rpkilby/django-registration-invite)
[![Codecov](https://codecov.io/gh/rpkilby/django-registration-invite/branch/master/graph/badge.svg)](https://codecov.io/gh/rpkilby/django-registration-invite)
[![Version](https://img.shields.io/pypi/v/django-registration-invite.svg)](https://pypi.python.org/pypi/django-registration-invite)
[![License](https://img.shields.io/pypi/l/django-registration-invite.svg)](https://pypi.python.org/pypi/django-registration-invite)


## Installation:

- Include `registration_invite` in your `INSTALLED_APPS` setting.
- Include the activation URLS in your URL conf `url(r'^', include('registration_invite.urls.activation')),`
- If using the user-based invitation workflow, you may instead include `url(r'^', include('registration_invite.urls.activation')),`
- Override the invitation templates. Basic examples are provided, but will most likely be insufficient.
    - registration/invite/email/body.txt
    - registration/invite/email/subject.txt
    - registration/invite/activation_complete.html
    - registration/invite/activation_form.html
    - registration/invite/invitation_complete.html
    - registration/invite/invitation_form.html

## Features:

- automatically registers the user model with the admin
- workflows for both admin-based and user-based invitations

## TODO:

- re-invite for expired users
- tests


## Release Process

- Update package version in `setup.py`
- Create git tag for version
- Upload release to PyPI
    ```bash
    $ pip install -U setuptools wheel
    $ rm -rf dist/ build/
    $ python setup.py sdist bdist_wheel upload
    ```


## Copyright & License

Copyright &copy; 2017 NC State University. See LICENSE for details.
