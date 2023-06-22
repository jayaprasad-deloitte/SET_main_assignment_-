from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By


class wheels_page:
    def __init__(self, driver):
        self.driver = driver
        self.menu_Two_Wheelers =(By.XPATH,'//img[@alt = "Two Wheelers"]')
        self.menu_Petrol =(By.XPATH,"// a[contains(text(), 'Petrol Vehicles')]")
        self.menu_Petrols =(By.XPATH,'// div[@class ="_3YgSsQ"]')
        self.prod_name_grab = (By.XPATH, "//h1/span")
        self.add_to_cart = (By.XPATH, '//li[1]/button')
        self.cart = (By.XPATH, "// a / span[contains(text(), 'Cart')]")
        self.tile=(By.XPATH,'//img[@title="Flipkart"]')

    def f_get_menu_wheels(self):
        return self.driver.find_element(*self.menu_Two_Wheelers)

    def f_get_menu_wheels2(self):
        return self.driver.find_element(*self.menu_Petrol)

    def f_get_wheels_prod(self):
        return self.driver.find_elements(*self.menu_Petrols)

    def f_get_menu_elec(self):
        return self.driver.find_element(*self.prod_name_grabb)

    def f_get_menu_elec(self):
        return self.driver.find_element(*self.cart)

    def f_get_menu_elec(self):
        return self.driver.find_element(*self.tile)
