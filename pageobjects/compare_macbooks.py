from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By


class macbook_page:

    def __init__(self,driver):
        self.driver = driver
        self.search_bar = (By.XPATH,'//input[@title="Search for products, brands and more"]') #searchbar
        self.text = "mac book pro 2023"
        self.laptops =(By.XPATH,'//div[@class="_2kHMtA"]') #latops
        self.checkboxes =(By.XPATH,'//label[@class="_2iDkf8"]') #checkbox
        self.compare_btn = (By.XPATH,"// span[contains(text(), 'COMPARE')]")
        self.price = (By.XPATH,'// div[ @class ="_30jeq3"]') #price
        self.highlights = (By.XPATH,'//div[@class="_2YNwCa"]')   #highlights

    def f_search_bar(self):
        return self.driver.find_element(*self.search_bar)
    def f_laptops(self):
        return self.driver.find_element(*self.laptops)
    def f_checkboxes(self):
        return self.driver.find_elements(*self.checkboxes)
    def f_compare_bt(self):
        return self.driver.find_element(*self.compare_btn)
    def f_price(self):
        return self.driver.find_elements(*self.price)
    def f_highlights(self):
        return self.driver.find_elements(*self.highlights)
