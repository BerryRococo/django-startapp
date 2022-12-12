#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : {{ cookiecutter.author_name }}
# @Email    : {{ cookiecutter.author_email }}
# @Time     : {{ cookiecutter.timestamp }}
# @File     : routers.py {{ cookiecutter.python_version}}
# @Software : {{ cookiecutter.product_name}} {{ cookiecutter.project_name }}
# @Desc     : TODO

from rest_framework import routers

from .views import {{ cookiecutter.app_name | title }}Views

router = routers.SimpleRouter()

# router.register("{{ cookiecutter.app_name }}", {{ cookiecutter.app_name | title }}Views)

router_list = [
    ("{{ cookiecutter.app_name }}", {{ cookiecutter.app_name | title }}Views)
]

for i in router_list:
    router.register(*i)

urlpatterns = router.urls
