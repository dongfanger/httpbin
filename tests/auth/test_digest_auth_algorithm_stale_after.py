import allure
from tep.client import request


@allure.title("摘要认证--MD5--never")
def test(env_vars):
    # 描述
    # 数据
    # 请求
    response = request(
        "get",
        url=env_vars.domain + "/digest-auth/1qaz/dongfanger/123456/MD5/never",
        headers={'Host': 'httpbin.org', 'Proxy-Connection': 'keep-alive',
                 'Authorization': 'Digest username="dongfanger", realm="me@kennethreitz.com", nonce="ba92e322c28f1e29d1a9d9768efcca25", uri="/digest-auth/1qaz/dongfanger/123456/MD5/never", algorithm=MD5, response="9059ba0a23966f926bf5c573d432f714", opaque="1ca878de9082752b128264c30ebab4d6", qop=auth, nc=00000003, cnonce="0afdbcb747146267"',
                 'accept': 'application/json',
                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
                 'Referer': 'http://httpbin.org/', 'Accept-Encoding': 'gzip, deflate',
                 'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
                 'Cookie': 'stale_after=never; fake=fake_value'},
        params={}
    )
    # 提取
    # 断言
    assert response.status_code < 400
