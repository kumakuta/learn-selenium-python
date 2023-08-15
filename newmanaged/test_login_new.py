import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from opensauce_login import *
from driver_preparation import driver_setting

class OpenSauceLogin(unittest.TestCase):
    def setUp(self):
        driver_setting(self)

    def test_normal_login(self): #As user with valid credentials, I can login to Saucedemo site
        #validaccount(self) #import valid credentials
        username_fetcher(self, "valid") #fetch legit username
        password_fetcher(self, "valid") #fetch legit password
        loginutils(self) #import login steps
        self.assertIn("/inventory.html", self.driver.current_url) #Assert url contains "inventory.html" which indicates user successfully login and redirected to inventory page

    def test_invalid_username_login(self): #As user with invalid username, I can not login to Saucedemo site
        #invalidaccount_password(self) #import valid username but invalid password
        username_fetcher(self, "invalid") #fetch invalid username
        password_fetcher(self, "valid") #fetch legit password
        loginutils(self) #import login steps
        error_message = self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3') #keeping error message as variable to be compared
        self.assertIn("Username and password do not match any user in this service", error_message.text) #assert that the page contains error message as provided

    def test_invalid_password_login(self):
        username_fetcher(self, "valid")
        password_fetcher(self, "invalid")
        loginutils(self)
        error_message = self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        self.assertIn("Username and password do not match any user in this service", error_message.text)
    
    def tearDown(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.driver.get_screenshot_as_file('report/screenshot-%s.png' % now)
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main()