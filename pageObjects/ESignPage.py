from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
from Helpers import SeleniumHelpers as SH
import sys
import os
from selenium.webdriver.common.action_chains import ActionChains
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

class ESignPage():

    def __init__(self,driver):
        self.driver=driver

    def set_input_value(self,input_xpath,item):
       SH.getXpath(self.driver,input_xpath).click()
       pyautogui.typewrite(item, interval=0.1)

    #def click_button(self,submit_xpath):
     #   SH.getXpath(self.driver,submit_xpath).click()

    def click_button(self, submit_xpath):
        # Find the button element using the provided XPath
        button = SH.getXpath(self.driver, submit_xpath)
        # Create an instance of ActionChains
        actions = ActionChains(self.driver)
        # Move the cursor to the button and click it
        actions.move_to_element(button).click().perform()

    def set_dropdown_value(self,drp_xpath,item):
        SH.dropdown_by_xpath(self.driver,drp_xpath,item)
    
    def set_checkbox_click(self,checkbox_xpath):
        # Wait for the checkbox to be clickable
        checkbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//label[contains(text(),'I certified using the following electronic signatu')])[1]"))
        )

        # Click the checkbox
        checkbox.click()

   

    
        
      
       
       
        
       
    


    
