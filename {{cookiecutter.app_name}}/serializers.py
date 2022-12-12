#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : {{ cookiecutter.author_name }}
# @Email    : {{ cookiecutter.author_email }}
# @Time     : {{ cookiecutter.timestamp }}
# @File     : serializers.py {{ cookiecutter.python_version}}
# @Software : {{ cookiecutter.product_name}} {{ cookiecutter.project_name }}
# @Desc     : TODO

from rest_framework import serializers

from .models import {{ cookiecutter.app_name | title }}


class {{ cookiecutter.app_name | title }}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {{ cookiecutter.app_name | title }}
        fields = "__all__"
