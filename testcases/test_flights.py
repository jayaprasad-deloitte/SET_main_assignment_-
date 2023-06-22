from utilities.BaseClass import BaseClass
from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
from pageobjects.Home_page import Homepage
from pageobjects.Flights import Flights_page
from pageobjects.compare_macbooks import macbook_page
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from testcases.conftest import log


class Test_three(BaseClass):

    def test_compare(self, setup):
        homepage = Homepage(self.driver)
        log.info("##################################### Start of the flow ################################")
        a = homepage.get_closer()
        a.click()
        time.sleep(1)



        actions = ActionChains(self.driver)


        flight = Flights_page(self.driver)
        navigate_to_flights = flight.f_flights_icon()
        navigate_to_flights.click()

        time.sleep(4)
        round_trip = flight.f_round_trip()
        round_trip.click()
        actions.click(round_trip).perform()
        time.sleep(5)


        dep = flight.f_dep_city()
        actions.click(dep).perform()
        actions.send_keys("HYD").perform()
        time.sleep(1)
        actions.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(1)
        actions.send_keys(Keys.ENTER).perform()

        time.sleep(4)

        arri = flight.f_arri_city()
        actions.click(arri).perform()
        actions.send_keys("BOM").perform()
        time.sleep(1)
        actions.send_keys(Keys.ARROW_DOWN).perform()
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(1)


        search_bt = flight.f_search_button()
        actions.move_to_element(search_bt).click(search_bt).perform()
        search_bt.click()

        on_b = flight.f_on_flight()
        boarding = on_b[1].text

        off_b = flight.f_off_flight()

        return_flight = off_b[1].text

        cost_first_fight = flight.f_spec(boarding)
        cost_second_fight = flight.f_spec(return_flight)
        cost_second_fight = cost_second_fight.text
        cost_first_fight = cost_first_fight.text
        cost_second_fight = cost_second_fight[1:]

        cost_first_fight = cost_first_fight[1:]


        total=flight.f_total_cost()
        total = total[1].text
        total = total[1:]
        total = int(total.replace(',',""))
        cost_second_fight=int(cost_second_fight.replace(',', ""))
        cost_first_fight=int(cost_first_fight.replace(',', ""))

        assert total ==cost_first_fight+cost_second_fight



        time.sleep(10)


