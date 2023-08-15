import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from opensauce_login import *
from driver_preparation import driver_setting, access_cart

class OpenSauceCart(unittest.TestCase):
    def setUp(self):
        driver_setting(self)
        username_fetcher(self, "valid") #fetch legit username
        password_fetcher(self, "valid") #fetch legit password
        loginutils(self) #import login steps

    def test_visit_cart(self):
        access_cart(self)
        self.page_title = self.driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
        self.assertIn("Your Cart", self.page_title.text)

    def test_add_to_cart(self):
        product_name = self.driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
        product_name_check = product_name.text
        atc_button = self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
        self.driver.execute_script("arguments[0].click();", atc_button)
        access_cart(self)
        item_name = self.driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
        self.assertIn(item_name.text, product_name_check)

    def tearDown(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.driver.get_screenshot_as_file('report/screenshot-%s.png' % now)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()