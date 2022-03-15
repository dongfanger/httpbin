#!/usr/bin/python
# encoding=utf-8

""" 只能管理员编辑，只对外提供fixture。
"""

import os
import time

import pytest

# 项目目录路径
_project_dir = os.path.dirname(os.path.abspath(__file__))


# 设置缓存供tep使用
@pytest.fixture(scope="session", autouse=True)
def _project_cache(request):
    request.config.cache.set("project_dir", _project_dir)


# 自动导入fixtures
_fixtures_dir = os.path.join(_project_dir, "fixtures")
_fixtures_paths = []
for root, _, files in os.walk(_fixtures_dir):
    for file in files:
        if file.startswith("fixture_") and file.endswith(".py"):
            full_path = os.path.join(root, file)
            import_path = full_path.replace(_fixtures_dir, "").replace("\\", ".").replace("/", ".").replace(".py", "")
            _fixtures_paths.append("fixtures" + import_path)
pytest_plugins = _fixtures_paths


# pytest hook函数
# https://docs.pytest.org/en/latest/reference/reference.html#hooks
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    total = terminalreporter._numcollected
    passed = len(terminalreporter.stats.get('passed', []))
    failed = len(terminalreporter.stats.get('failed', []))
    error = len(terminalreporter.stats.get('error', []))
    skipped = len(terminalreporter.stats.get('skipped', []))
    duration = time.time() - terminalreporter._sessionstarttime
