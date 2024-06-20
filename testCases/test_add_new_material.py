import pytest
import time

from pageObjects.LoginPage import LoginPage
from pageObjects.AddMaterialPage import AddMaterialPage
from pageObjects.SuccessPage import SuccessPage

from utilities.readProperties import ReadConfig
 
from Helpers.ReadExcel import ReadData
from Helpers.ReadDatabase import get_data

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from selenium.common.exceptions import NoSuchElementException

class Test_add_new_material:

    baseURL = ReadConfig.getApplicationURL()
    #username = ReadConfig.getUseremail()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(curr_dir)
    add_material_file = ReadConfig.getFilePath("add_material_file")

    add_material_file = os.path.join(parent_dir,add_material_file)


    @pytest.mark.parametrize("name,type,unit,description",ReadData(add_material_file))
    def test_add_material_button(self,setup,name,type,unit,description):
        
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(1)
        
        self.cp = LoginPage(self.driver)        
        self.cp.clickSignIn()
        self.cp.setUserName(self.username)
        self.cp.clickContinue()
        self.cp.setPassword(self.password)
        self.cp.clickContinue()
        time.sleep(1)
       
        print(self.driver.current_url)
        assert "Inventory" in self.driver.current_url

        self.fp = AddMaterialPage(self.driver)
        self.fp.set_click("(//div[contains(text(),'Add New Material')])[1]")
     
        WebDriverWait(self.driver,10).until(EC.url_contains("Inventory/add-new-material"))
        print(self.driver.current_url)
        assert "Inventory/add-new-material" in self.driver.current_url
        
        time.sleep(5)

        # Set input values
        #input_1 = WebDriverWait(self.driver, 10).until(
        #    EC.element_to_be_clickable((By.XPATH, "(//input[@id='ItmVl'])[1]"))
        #)
        self.fp.set_input_value("(//input[@id='ItmVl'])[1]", name)

        # Add a wait to ensure the second dropdown is interactable
        dropdown_2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='iaDropdownCommon_container iaDropdownCommon_placeholder-container ia_dropdown__placeholder'])[2]"))
        )
        self.fp.set_dropdown("(//div[@class='iaDropdownCommon_container iaDropdownCommon_placeholder-container ia_dropdown__placeholder'])[2]", unit)

    

        # Interact with the first dropdown
        dropdown_1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='iaDropdownCommon_container iaDropdownCommon_placeholder-container ia_dropdown__placeholder'])[1]"))
        )
        self.fp.set_dropdown("(//div[@class='iaDropdownCommon_container iaDropdownCommon_placeholder-container ia_dropdown__placeholder'])[1]", type)
        self.driver.find_element(By.XPATH, "//body").click()

        input_2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@id='ItmVl'])[2]"))
        )
        self.fp.set_input_value("(//input[@id='ItmVl'])[2]", description)


        self.fp.set_click("(//div)[104]")
        time.sleep(3)

        
        self.np = SuccessPage(self.driver)
        try:
            if self.driver.find_element(By.XPATH,"(//div)[114]"):
                print('to click')
                self.np.set_submit("(//div)[114]")
            else:
                if self.driver.find_element(By.XPATH,"(//div)[120]"):
                    print('else')
                    self.np.set_submit("(//div)[120]")
                
                    # test if insert into database correctly
                    query = """SELECT material.NAME AS 'name',type.name AS 'type', unit.name AS 'unit',DESCRIPTION FROM material JOIN TYPE ON TYPE.id= type_id JOIN unit ON unit_id = unit.id WHERE material.NAME = %s"""
                    database_list = get_data(query,(name,))
                    material_list = ReadData(self.add_material_file)
                    assert database_list == material_list
        except NoSuchElementException as e:
            print(f'Error: {e}')
            print('Neither element (//div)[120] nor (//div)[114] were found.')


