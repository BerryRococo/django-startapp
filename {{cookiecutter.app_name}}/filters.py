#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : {{ cookiecutter.author_name }}
# @Email    : {{ cookiecutter.author_email }}
# @Time     : {{ cookiecutter.timestamp }}
# @File     : filters.py {{ cookiecutter.python_version}}
# @Software : {{ cookiecutter.product_name}} {{ cookiecutter.project_name }}
# @Desc     : TODO

import django_filters

class {{ cookiecutter.app_name | title }}Filter(django_filters.Filter):
    ...
