from selenium.webdriver.common.by import By

def username_fetcher(self, a):
    if a == "valid":
        self.username = "standard_user"
    elif a == "invalid":
        self.username = "not_a_username"

def password_fetcher(self, a=""):
    if a == "valid":
        self.password = "secret_sauce"
    elif a == "invalid":
        self.password = "not_a_password"

def loginutils(self):
    self.login_form = self.driver.find_element(By.XPATH, '//*[@id="user-name"]') #Tap on user name 
    self.login_form.send_keys(self.username) #Input user name
    self.login_form = self.driver.find_element(By.XPATH, '//*[@id="password"]') #Tap on password 
    self.login_form.send_keys(self.password) #Input password
    self.login_form.submit() #Submit login form
    