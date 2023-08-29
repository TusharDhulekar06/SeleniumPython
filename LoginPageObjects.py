
from selenium.webdriver.common.by import By


class LoginPage:
    #Locators
    txtbox_username_id="//input[@id='Email']"
    txtbox_username_pwd="//input[@id='Password']"
    button_login_xpath="//button[normalize-space()='Log in']"
    #Constructor
    def __init__(self,driver):
        self.driver=driver
    #actions
    def setUserName(self,username):
        usernametxt=self.driver.find_element(By.XPATH,self.txtbox_username_id)
        usernametxt.clear()
        usernametxt.send_keys(username)
    def setPassword(self,userpwd):
        userpwdtxt=self.driver.find_element(By.XPATH,self.txtbox_username_pwd)
        userpwdtxt.clear()
        userpwdtxt.send_keys(userpwd)
    def Clickbutton(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()
