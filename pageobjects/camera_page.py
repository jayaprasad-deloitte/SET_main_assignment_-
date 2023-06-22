from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By


class ccamera_page:
    def __init__(self, driver):
        self.driver = driver
        self.menu_electronics = (By.XPATH, '//img[@alt = "Electronics"]')  # // div[contains(text(), 'Electronics')
        self.menu_Cameras_Accessories = (By.XPATH, "// a[contains(text(), 'Cameras & Accessories')]")
        self.menu_DSLR = (By.XPATH, "// a[contains(text(), 'DSLR & Mirrorless')]")
        self.prod_selector = (By.XPATH, '//div[@class="_13oc-S"]')
        self.prod_name_grab = (By.XPATH, "//h1/span")
        self.add_to_cart = (By.XPATH, '//li[1]/button')
        self.cart = (By.XPATH, "// a / span[contains(text(), 'Cart')]")

    def f_get_menu_elec(self):
        return self.driver.find_element(*self.menu_electronics)


    def f_menu_Cameras_Accessories(self):
        return self.menu_Cameras_Accessories

    def f_menu_DSLR(self):
        return self.driver.find_element(*self.menu_DSLR)

    def f_prod_selector(self):
        return self.driver.find_elements(*self.prod_selector)

    def f_prod_name_grab(self):
        return self.driver.find_element(*self.prod_name_grab)


    def f_add_to_cart(self):
        return self.driver.find_element(*self.add_to_cart)

    def f_cart(self):
        return self.driver.find_element(*self.cart)




