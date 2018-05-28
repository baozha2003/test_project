from time import sleep
import unittest, random, sys
from . import myunit, function
from .login_page import LoginPage
from .mail_page import MailPage

sys.path.append('./model')
sys.path.append('./page_obj')


class LoginTest(myunit.MyTest):

    def test_login_user_pwd_null(self):
        """用户名、密码为空登录"""

        po = LoginPage(self.driver)
        po.open()
        user = "13727086330"
        po.login_action(user, "qwe123")
        sleep(2)
        # po2 = MailPage(self.driver)
        # print(po2.login_success_user())
        # self.assertEqual()
        function.insert_img(self.driver, "success.jpg")