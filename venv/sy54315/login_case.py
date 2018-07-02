from time import sleep
import sys
from .model import function
from venv.sy54315.model import myunit
from .page_object.login_page import LoginPage

sys.path.append('./model')
sys.path.append('./page_object')


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
        self.assertEqual()
        # function.insert_img(self.driver, "success.jpg")
