#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : CoderChaos
# @Email    : CoderChaos@yeah.net
# @Time     : 2022/11/27 11:46
# @File     : main.py python3.9
# @Software : PyCharm django-startapp
# @Desc     : TODO

from datetime import datetime

from cookiecutter.main import cookiecutter

import argparse

github_path = ""


def run_cookiecutter(path):
    cookiecutter(
        path,
        extra_context={
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    )


def run(env="local"):
    path_list = {
        "local": ".",
        "github": "https://github.com",
    }

    # 定义命令行解析器对象
    parser = argparse.ArgumentParser(description="local or github")

    # 添加命令行参数
    parser.add_argument("--env", type=str, default="local")

    # 从命令行中解析参数
    args = parser.parse_args()

    env = args.env

    path = path_list[env]

    run_cookiecutter(path)


if __name__ == '__main__':
    run()

# python main.py --env=local
