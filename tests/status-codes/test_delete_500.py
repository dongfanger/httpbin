import allure
from tep.client import request


@allure.title("delete返回状态码500")
def test(env_vars):
    # 描述
    # 数据
    # 请求
    response = request(
        "delete",
        url=env_vars.domain + "/status/500",
        headers={'Host': 'httpbin.org', 'Proxy-Connection': 'keep-alive', 'accept': 'text/plain',
                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
                 'Origin': 'http://httpbin.org', 'Referer': 'http://httpbin.org/', 'Accept-Encoding': 'gzip, deflate',
                 'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
                 'Cookie': 'stale_after=never; fake=fake_value'},
        json={}
    )
    # 提取
    # 断言
    assert response.status_code == 500
