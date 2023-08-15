import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
#from opensauce_login import *

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def loginutils(self, account):
        self.login_form = self.driver.find_element(By.XPATH, '//*[@id="user-name"]') #Tap on user name 
        self.login_form.send_keys(account.username)
        self.login_form = self.driver.find_element(By.XPATH, '//*[@id="password"]') #Tap on password 
        self.login_form.send_keys(account.password)
        self.login_form.submit() #Submit login form

class OpenSauceLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('https://saucedemo.com')

    def test_normal_login(self): #As user with valid credentials, I can login to Saucedemo site
        validAccount = Account("standard_user", "secret_sauce")
        Account.loginutils(self, validAccount)
        self.assertIn("/inventory.html", self.driver.current_url) #Assert url contains "inventory.html" which indicates user successfully login and redirected to inventory page

    def test_invalid_username_login(self): #As user with invalid username, I can not login to Saucedemo site
        #invalidaccount_password(self) #import valid username but invalid password\
        invalidAccount = Account("")
        Account.loginutils(self,invalidAccount) #import login steps
        error_message = self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3') #keeping error message as variable to be compared
        self.assertIn("Username and password do not match any user in this service", error_message.text) #assert that the page contains error message as provided

    '''def test_invalid_password_login(self):
        self.login_form = self.driver.find_element(By.XPATH, '//*[@id="user-name"]')
        self.login_form.send_keys("standard_user")
        self.login_form = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        self.login_form.send_keys("not_a_password")
        self.login_form.submit()
        error_message = self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        self.assertIn("Username and password do not match any user in this service", error_message.text)'''
    
    def tearDown(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.driver.get_screenshot_as_file('report/screenshot-%s.png' % now)
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main()