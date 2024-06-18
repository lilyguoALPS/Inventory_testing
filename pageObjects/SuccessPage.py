
from Helpers import SeleniumHelpers as SH
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

class SuccessPage():

    def __init__(self,driver):
        self.driver=driver
   
    def set_submit(self,button_xpath):
        SH.getXpath(self.driver,button_xpath).click()  