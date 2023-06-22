from selenium.webdriver.common.by import By



class Homepage:

    def __init__(self,driver):
        self.driver = driver
        self.close_add =(By.XPATH,'//button[contains(text(),"✕")]')
        self.menu_mobiles =(By.XPATH,'//img[@alt="Mobiles"]')
        self.menu_Two_Wheelers =(By.XPATH,'//img[@alt = "Two Wheelers"]')
        self.menu_Petrol =(By.XPATH,"// a[contains(text(), 'Petrol Vehicles')]")
        self.menu_Petrols =(By.XPATH,'// div[@class ="_3YgSsQ"]')
        self.prod_name_grab = (By.XPATH, "//h1/span")
        self.add_to_cart = (By.XPATH, '//li[1]/button')
        self.cart = (By.XPATH, "// a / span[contains(text(), 'Cart')]")
        self.tile=(By.XPATH,'//img[@title="Flipkart"]')
        self.final_checker =(By.XPATH,'//div[@class="zab8Yh _10k93p"]//a[@class="_2Kn22P gBNbID"]')

    def get_closer(self):
        return self.driver.find_element(*self.close_add)
    def get_mobile(self):
        return self.driver.find_element(*self.menu_mobiles)
    def f_get_title(self):
        return self.driver.find_element(*self.tile)
    def f_final_checker(self):
        return self.driver.find_elements(*self.final_checker)