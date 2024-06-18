import pytest
from selenium import webdriver
import sys
import os
import time


from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


from pageObjects.LoginPage import LoginPage
#from pageObjects.OverviewPage import OverviewPage

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

class Test_001_Login:
    #baseURL = ReadConfig.getApplicationURL()
    #username = ReadConfig.getUseremail()
    #password = ReadConfig.getPassword()
    baseURL='http://localhost:8088/data/perspective/client/Inventory'
    username='admin' 
    password=1
    logger=LogGen.loggen()

    def test_login(self,setup):

        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(5)
        self.lp=LoginPage(self.driver)
        self.lp.clickSignIn()
        self.lp.setUserName(self.username)
        self.lp.clickContinue()
        self.lp.setPassword(self.password)
        self.lp.clickContinue()
        time.sleep(5)
        get_url = self.driver.current_url
        self.driver.close()
           
        assert get_url == 'http://localhost:8088/data/perspective/client/Inventory'
        """
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            self.logger.info("****Login test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
        """
    





