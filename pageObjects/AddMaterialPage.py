from Helpers import SeleniumHelpers as SH
import sys
import os
import pyautogui

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
print(SCRIPT_DIR)
sys.path.append(os.path.dirname(SCRIPT_DIR))

class AddMaterialPage():
    def __init__(self,driver):
        self.driver = driver

    def get_navbar(self,nav_path): 
        SH.getXpath(self.driver,nav_path).click()
       
    def set_input_value(self,value_xpath,value):
         SH.getXpath(self.driver,value_xpath).click()
         pyautogui.typewrite(value, interval=0.1)

    def set_click(self,element_xpath):
        SH.getXpath(self.driver,element_xpath).click()

    def set_dropdown(self,element_xpath,value):
        SH.dropdown_by_xpath(self.driver,element_xpath,value)

    def set_unitdropdown(self,element_xpath,value):
        SH.dropdown_by_xpath(self.driver,element_xpath,value)