import allure
from tep.client import request


@allure.title("返回所有数据--带参数")
def test(env_vars):
    # 描述
    # 数据
    # 请求
    response = request(
        "delete",
        url=env_vars.domain + "/anything/%7Banything%7D",
        headers={'Host': 'httpbin.org', 'Proxy-Connection': 'keep-alive', 'accept': 'application/json',
                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
                 'Origin': '', 'Referer': '/', 'Accept-Encoding': 'gzip, deflate',
                 'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
                 'Cookie': 'stale_after=never; fake=fake_value; freeform=3; name=dongfanger'},
        json={}
    )
    # 提取
    # 断言
    assert response.status_code < 400

    # 描述
    # 数据
    # 请求
    response = request(
        "get",
        url=env_vars.domain + "/anything/%7Banything%7D",
        headers={'Host': 'httpbin.org', 'Proxy-Connection': 'keep-alive', 'accept': 'application/json',
                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
                 'Referer': '/', 'Accept-Encoding': 'gzip, deflate',
                 'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
                 'Cookie': 'stale_after=never; fake=fake_value; freeform=3; name=dongfanger'},
        params={}
    )
    # 提取
    # 断言
    assert response.status_code < 400

    # 描述
    # 数据
    # 请求
    response = request(
        "patch",
        url=env_vars.domain + "/anything/%7Banything%7D",
        headers={'Host': 'httpbin.org', 'Proxy-Connection': 'keep-alive', 'accept': 'application/json',
                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
                 'Origin': '', 'Referer': '/', 'Accept-Encoding': 'gzip, deflate',
                 'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
                 'Cookie': 'stale_after=never; fake=fake_value; freeform=3; name=dongfanger'},
        json={}
    )
    # 提取
    # 断言
    assert response.status_code < 400

    # 描述
    # 数据
    # 请求
    response = request(
        "post",
        url=env_vars.domain + "/anything/%7Banything%7D",
        headers={'Host': 'httpbin.org', 'Proxy-Connection': 'keep-alive', 'Content-Length': '0',
                 'accept': 'application/json',
                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
                 'Origin': '', 'Referer': '/', 'Accept-Encoding': 'gzip, deflate',
                 'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
                 'Cookie': 'stale_after=never; fake=fake_value; freeform=3; name=dongfanger'},
        json={}
    )
    # 提取
    # 断言
    assert response.status_code < 400

    # 描述
    # 数据
    # 请求
    response = request(
        "put",
        url=env_vars.domain + "/anything/%7Banything%7D",
        headers={'Host': 'httpbin.org', 'Proxy-Connection': 'keep-alive', 'Content-Length': '0',
                 'accept': 'application/json',
                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
                 'Origin': '', 'Referer': '/', 'Accept-Encoding': 'gzip, deflate',
                 'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
                 'Cookie': 'stale_after=never; fake=fake_value; freeform=3; name=dongfanger'},
        json={}
    )
    # 提取
    # 断言
    assert response.status_code < 400
