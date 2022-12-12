#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : {{ cookiecutter.author_name }}
# @Email    : {{ cookiecutter.author_email }}
# @Time     : {{ cookiecutter.timestamp }}
# @File     : views.py {{ cookiecutter.python_version}}
# @Software : {{ cookiecutter.product_name}} {{ cookiecutter.project_name }}
# @Desc     : TODO

from rest_framework.viewsets import ModelViewSet

from .models import {{ cookiecutter.app_name | title }}
from .serializers import {{ cookiecutter.app_name | title }}Serializer


class {{ cookiecutter.app_name | title }}Views(ModelViewSet):
    queryset = {{ cookiecutter.app_name | title }}.objects.all()
    serializer_class = {{ cookiecutter.app_name | title }}Serializer
