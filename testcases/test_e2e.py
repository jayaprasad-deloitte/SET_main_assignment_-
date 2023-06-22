from pageobjects.Home_page import Homepage
from pageobjects.mobiles_page import moblies_page
from pageobjects.camera_page import ccamera_page
from pageobjects.two_wheels import wheels_page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utilities.BaseClass import BaseClass
from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from testcases.conftest import log

import time
class Testone(BaseClass):

    def test_e2e(self, setup):


        homepage = Homepage(self.driver)
        log.info("##################################### Start of the flow ################################")



        home_add_closer = homepage.get_closer()
        home_add_closer.click()


        homepage.get_mobile().click()
        mobpage = moblies_page(self.driver)
        mobile_brand = mobpage.get_brand()
        mobile_brand.click()
        #time.sleep(2)
        product_selector =mobpage.f_iphones_selector()
        product_selector[0].click()
        #time.sleep(2)

        tab = self.driver.current_window_handle
        parent = self.driver.window_handles[1]
        chld = self.driver.window_handles[1]
        self.driver.close()
        self.driver.switch_to.window(chld)
        #time.sleep(4)

        name_grab =  mobpage.f_iphones_name_grab()
        product_1_name= name_grab.text
        #time.sleep(2)

        adding_to_the_cart =mobpage.f_add_to_cart()
        adding_to_the_cart.click()


        #time.sleep(2)
        return_home = homepage.f_get_title()
        return_home.click()
        #time.sleep(2)

        home_add_closer = homepage.get_closer()
        #time.sleep(3)
        home_add_closer.click()
        cam_page = ccamera_page(self.driver)


        menu_electronics =cam_page.f_get_menu_elec()

        actions = ActionChains(self.driver)
        #time.sleep(5)
        actions.move_to_element(menu_electronics).perform()
        actions.move_by_offset(-30,180).context_click().perform()
        actions.move_by_offset(100,0).click().perform()



        prud_choice= cam_page.f_prod_selector()
        prud_choice[0].click()

        tab = self.driver.current_window_handle
        parent = self.driver.window_handles[0]
        chld = self.driver.window_handles[1]
        self.driver.close()
        self.driver.switch_to.window(chld)


        name = cam_page.f_prod_name_grab()
        product_2_name = name.text



        adding_to_the_cart = cam_page.f_add_to_cart()

        #time.sleep(4)
        adding_to_the_cart.click()
        #time.sleep(4)
            
        return_home = homepage.f_get_title()
        #time.sleep(4)
        return_home.click()
        


        #time.sleep(3)

        wheels = wheels_page(self.driver)

        menu_wheels = wheels.f_get_menu_wheels()

        actions = ActionChains(self.driver)
        #time.sleep(5)
        actions.move_to_element(menu_wheels).perform()
        actions.move_by_offset(0, 100).context_click().perform()
        actions.move_by_offset(1, 0).click().perform()
        time.sleep(3)

        product_3_select = wheels.f_get_wheels_prod()
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(product_3_select[0])).click()


        tab = self.driver.current_window_handle
        parent = self.driver.window_handles[0]
        chld = self.driver.window_handles[1]
        self.driver.close()
        self.driver.switch_to.window(chld)

        product_3_name = cam_page.f_prod_name_grab()
        product_3_name = product_3_name.text


        adding_to_the_cart = cam_page.f_add_to_cart()

        #time.sleep(4)
        adding_to_the_cart.click()
        #time.sleep(4)
        prod_list = homepage.f_final_checker()
        
        list_prods = [product_3_name,product_2_name,product_1_name]
        prod_1 =  prod_list[0].text
        prod_2 =  prod_list[1].text
        prod_3 =  prod_list[2].text

        try:
            assert prod_1 in product_3_name
        except AssertionError:
            pytest.fail("wrong product")


        try:
            assert prod_2 in product_2_name
        except AssertionError:
            pytest.fail("wrong product")

        try:
            assert prod_3 in product_1_name
        except AssertionError:
            pytest.fail("wrong product")











