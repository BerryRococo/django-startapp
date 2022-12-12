#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : {{ cookiecutter.author_name }}
# @Email    : {{ cookiecutter.author_email }}
# @Time     : {{ cookiecutter.timestamp }}
# @File     : apps.py {{ cookiecutter.python_version}}
# @Software : {{ cookiecutter.product_name}} {{ cookiecutter.project_name }}
# @Desc     : TODO


from django.apps import AppConfig


class {{ cookiecutter.app_name | title }}Config(AppConfig):
    name = "{{ cookiecutter.app_name }}"
    verbose_name = "{{ cookiecutter.verbose_name }}"
