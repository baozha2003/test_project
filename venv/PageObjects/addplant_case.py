from time import sleep
import sys
from venv.PageObjects.model import function, myunit
from venv.PageObjects.page_obj.login_page import LoginPage
from venv.PageObjects.page_obj.plant_page import PlantPage
from venv.PageObjects.page_obj.addplant_page import AddPlantPage

sys.path.append('./model')
sys.path.append('./page_obj')


class AddPlanttest(myunit.MyTest):
    def test_addplant(self):
        '''新建种植计划'''
        po = LoginPage(self.driver)
        po.open()
        po.login_action(13727086330, "qwe123")
        sleep(1)
        po2 = PlantPage(self.driver)
        po2.to_plant_page()
        sleep(1)
        po2.add_plant_click()
        po3 = AddPlantPage(self.driver)
        po3.add_plant('三七')
        self.assertEqual(po3.tishi_text(), "新建计划成功！")
        function.insert_img(self.driver, 'addplantsuccess.png')
