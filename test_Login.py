import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from LoginPageObjects import LoginPage
class TestLogin:
    def test_login(self):
        service=ChromeService(executable_path=ChromeDriverManager().install())
        self.driver=webdriver.Chrome(service=service)
        self.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp=LoginPage(self.driver)
        self.lp.setUserName("admin@yourstore.com")
        self.lp.setPassword("admin")
        self.lp.Clickbutton()
        self.title=self.driver.title
        self.driver.close()
        assert self.title=="Dashboard / nopCommerce administration"


