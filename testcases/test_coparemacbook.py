from utilities.BaseClass import BaseClass
from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
from pageobjects.Home_page import Homepage
from pageobjects.compare_macbooks import macbook_page
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from testcases.conftest import log
import codecs




class Test_two(BaseClass):

    def test_compare(self, setup):
        homepage = Homepage(self.driver)
        log.info("##################################### Start of the flow ################################")
        a = homepage.get_closer()

        a.click()
        mac =macbook_page(self.driver)
        a=self.driver.find_element(By.XPATH,'//input[@title="Search for products, brands and more"]')
        actions = ActionChains(self.driver)


        actions.move_to_element(a).click(a).perform()
        actions.send_keys("mac book pro 2023",).perform()

        actions.move_by_offset(0,40).click().perform()
        actions.move_to_element(a).perform()

        laptops = mac.f_laptops()

        checkboexes = mac.f_checkboxes()
        checkboexes[0].click()
        checkboexes[1].click()

        com = mac.f_compare_bt()
        com.click()

        prices = mac.f_price()


        lights = mac.f_highlights()
        print(lights[0].text,lights[1].text)


        prices_1 = prices[0].text
        prices_1 = int(prices_1[1:].replace(',',""))

        prices_2 = prices[1].text
        prices_2 = int(prices_2[1:].replace(',', ""))

        h_lights_1 = (lights[0].text).splitlines()
        h_lights_2 = (lights[1].text).splitlines()

        assert prices_1 == prices_2
        assert h_lights_1 == h_lights_2


