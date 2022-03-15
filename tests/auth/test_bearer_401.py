import allure
from tep.client import request


@allure.title("Authorization没有Bearer，返回401未授权")
def test(env_vars):
    # 描述
    # 数据
    # 请求
    response = request(
        "get",
        url=env_vars.domain + "/bearer",
        headers={'Host': 'httpbin.org', 'Proxy-Connection': 'keep-alive', 'accept': 'application/json',
                 'Authorization': 'ZG9uZ2ZhbmdlcjoxMjM0NTY=',  # 替换token
                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
                 'Referer': 'http://httpbin.org/', 'Accept-Encoding': 'gzip, deflate',
                 'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'},
        params={}
    )
    # 提取
    # 断言
    assert response.status_code == 401
