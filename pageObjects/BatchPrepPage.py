from Helpers import SeleniumHelpers as SH
import sys
import os
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import selenium
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
print(SCRIPT_DIR)
sys.path.append(os.path.dirname(SCRIPT_DIR))

class BatchPrepPage():
    def __init__(self,driver):
        self.driver = driver
       
    def set_input_value(self,value_xpath,value):
         SH.getXpath(self.driver,value_xpath).click()
         pyautogui.typewrite(value, interval=0.1)
         pyautogui.press('enter')

    def set_click(self,submit_xpath):
        
        button = SH.getXpath(self.driver, submit_xpath)
        # Create an instance of ActionChains
        actions = ActionChains(self.driver)
        # Move the cursor to the button and click it
        actions.move_to_element(button).click().perform()

    def set_dropdown(self,element_xpath,value):
        SH.dropdown_by_xpath(self.driver,element_xpath,value)
  
    def select_radio_button(self,radio_button_xpath):
        radio_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, radio_button_xpath))
            )
        radio_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, radio_button_xpath))
            )
        radio_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, radio_button_xpath)))
        actions = ActionChains(self.driver)
        actions.move_to_element(radio_button).perform
        actions.click(radio_button).perform()
        #radio_button.click()
       
    def is_radio_button_selected(self, radio_button_xpath):
        """
        Check if the radio button is selected.

        :param radio_button_xpath: XPath to locate the radio button.
        :return: True if the radio button is selected, False otherwise.
        """
        radio_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, radio_button_xpath))
        )
        return radio_button.is_selected()
    
    def list_to_dict(self,lst):
        return {item[0]: item[1] for item in lst}

    def dict_to_sorted_list(self,dct):       
        return sorted(dct.items())