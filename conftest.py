'''
@author: wuweixi
Created on 2021年2月23日
'''
import json
from aspire import HttpHelper as http
from aspire import Config as cf
import pytest

@pytest.fixture(scope="session")
def get_cookie():
    """全局调用登录获取cookie固件"""
    url = "http://test.auth.aplusunion.com/v1/openapi/user/login"
    post_data = "username=&" \
                "password=" \
                "logintype=username&" \
                "grant_type=password&" \
                "client_id=weboop&client_secret=password&" \
                "redirect_url=http%3A%2F%2Ftest.flz.aplusunion.com%2F%23%2Fuser-center%2Fmine%3F"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    rs = http.post(url,post_data,headers)[1]
    rs_js = json.loads(rs)
    return str(rs_js['data']['accessToken'])