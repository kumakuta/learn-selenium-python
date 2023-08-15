from selenium import webdriver
from selenium.webdriver.common.by import By

def driver_setting(self):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(30)
    self.driver.maximize_window()
    self.driver.get("https://saucedemo.com/")

def access_cart(self):
    l = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    self.driver.execute_script("arguments[0].click();", l)