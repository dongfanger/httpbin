#!/usr/bin/python
# encoding=utf-8

from tep.fixture import *


@pytest.fixture(scope="session")
def env_vars(config):
    class Clazz(TepVars):
        env = config["env"]

        """变量定义开始"""
        # 环境变量
        mapping = {
            "http": {  # http环境
                "domain": "http://httpbin.org",
            },
            "https": {  # https环境
                "domain": "https://httpbin.org",
            }
            # 继续添加
        }
        # 定义类属性，敲代码时会自动补全
        domain = mapping[env]["domain"]
        """变量定义结束"""

    return Clazz()
