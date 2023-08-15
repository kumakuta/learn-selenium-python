import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime


class OpenSauceCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://saucedemo.com/")
        self.login_form = self.driver.find_element(By.XPATH, '//*[@id="user-name"]')
        self.login_form.send_keys("standard_user")
        self.login_form = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        self.login_form.send_keys("secret_sauce")
        self.login_form.submit()

    def test_visit_cart(self): #As User with Valid Credentials I can access Cart Page
        l = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
        self.driver.execute_script("arguments[0].click();", l)
        self.page_title = self.driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
        """header_container = self.driver.find_element(By.ID, 'header_container')
        page_title = header_container.find_element(By.CLASS_NAME, 'title')"""
        self.assertIn("Your Cart", self.page_title.text)
        """sleep(1)
        self.driver.get_screenshot_as_file("screenshot.png")"""

    def test_add_to_cart(self):
        product_name = self.driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
        product_name_check = product_name.text
        atc_button = self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
        self.driver.execute_script("arguments[0].click();", atc_button)
        l = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
        self.driver.execute_script("arguments[0].click();", l)
        self.page_title = self.driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
        """header_container = self.driver.find_element(By.ID, 'header_container')
        page_title = header_container.find_element(By.CLASS_NAME, 'title')"""
        self.assertIn("Your Cart", self.page_title.text)
        item_name = self.driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
        self.assertIn(item_name.text, product_name_check)
        """sleep(1)
        self.driver.get_screenshot_as_file("screenshot2.png")"""

    def tearDown(self):
        # close the browser window
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.driver.get_screenshot_as_file('report/screenshot-%s.png' % now)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()