from time import sleep
import sys
from venv.PageObjects.model import function, myunit
from venv.PageObjects.page_obj.login_page import LoginPage

sys.path.append('./model')
sys.path.append('./page_obj')


class LoginTest(myunit.MyTest):

    def test_login_user_pwd_success(self):
        po = LoginPage(self.driver)
        po.open()
        user = "13727086330"
        po.login_action(user, "qwe123")
        sleep(2)
        function.insert_img(self.driver, "success.png")
