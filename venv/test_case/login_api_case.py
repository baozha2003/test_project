import requests
import unittest


class TestLoginApi(unittest.TestCase):
    """登陆接口测试"""

    def test_login_api(self):
        url = "http://sytest.54315.com/login"
        querystring = {"mobile": "13727086330", "password": "qwe123"}
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "167d7ea0-c440-4bfb-9f40-08d7169599e1"
        }
        response = requests.request("POST", url, headers=headers, params=querystring).json()
        print(response)
        self.assertEqual(response['code'], '100')
        self.assertEqual(response['message'], "登录成功")


if __name__ == '__main__':
    unittest.main()
