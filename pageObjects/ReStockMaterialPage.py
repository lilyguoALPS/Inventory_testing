from Helpers import SeleniumHelpers as SH
import sys
import os
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
print(SCRIPT_DIR)
sys.path.append(os.path.dirname(SCRIPT_DIR))

class ReStockMaterialPage():
    def __init__(self,driver):
        self.driver = driver
       
    def set_input_value(self,value_xpath,value):
         SH.getXpath(self.driver,value_xpath).click()
         pyautogui.typewrite(value, interval=0.1)
         pyautogui.press('enter')

    def set_click(self,element_xpath):
        SH.getXpath(self.driver,element_xpath).click()

    def set_dropdown(self,element_xpath,value):
        SH.dropdown_by_xpath(self.driver,element_xpath,value)

    def set_timepicker_value(self, timepicker_xpath, time_value):
        """
        Set the value of the TimePicker component.

        :param timepicker_xpath: XPath to locate the TimePicker component.
        :param time_value: Time value to set, in the format expected by the TimePicker.
        """
        # Wait until the timepicker is clickable and click it to focus
        datepicker_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, timepicker_xpath))
        )
        datepicker_element.send_keys(time_value)