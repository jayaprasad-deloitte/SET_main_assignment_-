from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By


class Flights_page():

    def __init__(self,driver):
        self.driver = driver
        self.f1=(By.XPATH,"//div[contains(text(),'Travel')]")
        self.round_trip = (By.XPATH,"// div[contains(text(),'Round Trip')]")
        self.dep_city= (By.XPATH,'//input[@name="0-departcity"]')
        self.arri_city = (By.XPATH,'//input[@name="0-arrivalcity"]')
        self.date_from = (By.XPATH,'//input[@name="0-datefrom"]')
        self.date_to = (By.XPATH,'//input[@name="0-dateto"]')
        self.on_flight = (By.XPATH,"//span[contains(text(),'Onward Flight - ')]/../span")
        self.off_flight = (By.XPATH, "//span[contains(text(),'Return Flight - ')]/../span")
        self.button = (By.XPATH, "//span[contains(text(),'SEARCH')]")
        self.str1 = '//span[contains(text(),"'
        self.str2 = '")]/../../../..//div[@class="_1AhVAh"]'
        self.total_cost = (By.XPATH,"//span[contains(text(),'Per Traveller')]/../span")

    def f_flights_icon (self ):
        return self.driver.find_element(*self.f1)
    def f_round_trip(self ):
        return self.driver.find_element(*self.round_trip)
    def f_dep_city (self ):
        return self.driver.find_element(*self.dep_city)
    def f_arri_city (self ):
        return self.driver.find_element(*self.arri_city)
    def f_search_button (self ):
        return self.driver.find_element(*self.button)


    def f_date_from (self ):
        return self.driver.find_element(*self.date_from)
    def f_date_to (self ):
        return self.driver.find_elements(*self.date_to)
    def f_on_flight (self ):
        return self.driver.find_elements(*self.on_flight)
    def f_off_flight (self ):
        return self.driver.find_elements(*self.off_flight)
    def f_spec(self,var):
        tem = self.driver.find_element(By.XPATH,self.str1 +var+self.str2)
        return tem
    def f_total_cost (self):
        return self.driver.find_elements(*self.total_cost)

