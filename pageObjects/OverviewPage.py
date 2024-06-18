from selenium.webdriver.common.by import By
from Helpers import SeleniumHelpers as SH
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import sys
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

class OverviewPage():
  
  

    def __init__(self,driver):
        self.driver=driver
    #@pytest.mark.parametrize("roomNum",[1])
    def clickBee(self,svg_bee_icon):
       element= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,svg_bee_icon)))
       action = ActionChains(self.driver)
       action.click(on_element=element)
       action.perform()


        #WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.text_lot_path))).send_keys("123456789")

    

      
       
       
        
       
    


    
