from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By


class moblies_page:

    def __init__(self,driver):
        self.driver = driver
        self.apple_selector_checkbox = (By.XPATH,"//label//div[contains(text(),'APPLE')]")
        self.prod_selector = (By.XPATH,'//div[@class="_13oc-S"]')
        self.prod_name_grab = (By.XPATH,"//h1/span")
        self.add_to_cart = (By.XPATH,'//li[1]/button')
        self.cart = (By.XPATH, "// a / span[contains(text(), 'Cart')]")


    def get_brand(self):
        return self.driver.find_element(*self.apple_selector_checkbox)


    def ret_list(self):
        return [1,2]



    def f_iphones_selector(self):
        slection = self.driver.find_elements(*self.prod_selector)
        return slection

    def f_iphones_name_grab(self):
        return self.driver.find_element(*self.prod_name_grab)

    def f_add_to_cart(self):
        return self.driver.find_element(*self.add_to_cart)

    def f_cart(self):
        return self.driver.find_element(*self.cart)


