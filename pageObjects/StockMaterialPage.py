from Helpers import SeleniumHelpers as SH
import sys
import os
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
import time
from selenium.webdriver.common.keys import Keys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
print(SCRIPT_DIR)
sys.path.append(os.path.dirname(SCRIPT_DIR))

class StockMaterialPage():
    def __init__(self,driver):
        self.driver = driver
       
    def set_input_value(self,value_xpath,value):
         SH.getXpath(self.driver,value_xpath).click()
         pyautogui.typewrite(value, interval=0.1)

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
        datepicker_element.click()
        
        #datepicker_element.send_keys("2025-01-10")
        #pyautogui.typewrite(time_value, interval=0.1)
        # Use JavaScript to set the value and trigger change and input events
        self.driver.execute_script("""
            var element = arguments[0];
            var value = arguments[1];
            element.value = value;
            element.dispatchEvent(new Event('input', { bubbles: true }));
            element.dispatchEvent(new Event('change', { bubbles: true }));
        """, datepicker_element, time_value)
       
        # Add a short wait to ensure value is set
        WebDriverWait(self.driver, 2).until(
            lambda driver: datepicker_element.get_attribute('value') == time_value
        )

        # If value is not set, retry with a different approach
        if datepicker_element.get_attribute('value') != time_value:
            datepicker_element.clear()
            for char in time_value:
                datepicker_element.send_keys(char)
                WebDriverWait(self.driver, 0.1)
            datepicker_element.send_keys(Keys.TAB)

            # Verify again
            WebDriverWait(self.driver, 2).until(
                lambda driver: datepicker_element.get_attribute('value') == time_value
            )
        
        time.sleep(1)
    '''
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
        datepicker_element.click()

        # Split the time_value into year, month, and day
        year, month, day = time_value.split('-')

        # Open the year picker and select the year
        year_picker = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[contains(@class, 'year-picker')]"))
        )
        year_picker.click()
        year_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//option[@value='{year}']"))
        )
        year_option.click()

        # Open the month picker and select the month
        month_picker = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[contains(@class, 'month-picker')]"))
        )
        month_picker.click()
        month_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//option[@value='{int(month)-1}']"))  # Assuming month is 0-indexed
        )
        month_option.click()

        # Select the day
        day_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//td[text()='{int(day)}']"))
        )
        day_element.click()

        # Verify the value is set
        WebDriverWait(self.driver, 2).until(
            lambda driver: datepicker_element.get_attribute('value') == time_value
        )
    '''
    