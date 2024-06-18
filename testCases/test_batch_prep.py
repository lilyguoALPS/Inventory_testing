import pytest
import time

from pageObjects.LoginPage import LoginPage
from pageObjects.BatchPrepPage import BatchPrepPage
from pageObjects.SuccessPage import SuccessPage
from pageObjects.ESignPage import ESignPage

from utilities.readProperties import ReadConfig
 
from Helpers.ReadExcel import ReadData
from Helpers.ReadDatabase import get_data

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_stock_material:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    batch_prep_file = ReadConfig.getFilePath("batch_prep_file")
    check_batch_recipe_history = ReadConfig.getFilePath("check_batch_recipe_history")
    check_extraction_history = ReadConfig.getFilePath("check_extraction_history")

    @pytest.mark.parametrize("batch_id,recipe_type,recipe,serving",ReadData(batch_prep_file))
    def test_stock_material_button(self,setup,batch_id,recipe_type,recipe,serving):
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

        self.op = BatchPrepPage(self.driver)
        self.op.set_click("(//div[contains(text(),'Batch Prep')])[1]")
    
        WebDriverWait(self.driver,10).until(EC.url_contains("Inventory/extract-item"))
        print(self.driver.current_url)
        assert "Inventory/extract-item" in self.driver.current_url

        
        # Set input value batch_id
        self.op.set_input_value("(//input[@class='ia_inputField text-field popup-not-draggable'])[1]",batch_id)

        # set radio button to select Meterial Receipe/Product Recipe
        if recipe_type == "material":
            self.op.select_radio_button("(//label[normalize-space()='Material Recipe'])[1]")
        else:
            self.op.select_radio_button("(//label[normalize-space()='Product Recipe'])[1]")
        
        # set dropdown to select recipe
        self.op.set_dropdown("(//div[@class='iaDropdownCommon_container iaDropdownCommon_placeholder-container ia_dropdown__placeholder'])[1]", recipe)
        
        # set input value serving: 1/2/...
        self.op.set_input_value("(//input[@class='ia_inputField ia-numeral-input popup-not-draggable'])[1]",str(serving))

      
        time.sleep(3)
        query = """select material_lot_id,balance_on_hand 
            from balance_summary 
            order BY material_lot_id desc"""
        database_list_before = get_data(query)
        
        if recipe_type == "material":
            # Click to save or proceed
            save_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "(//div)[181]"))
            )
            self.op.set_click("(//div)[181]")
        else:
            # Click to save or proceed
            save_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "(//div)[209]"))
            )
            save_button.click()


        self.sp = ESignPage(self.driver)

        time.sleep(5)
        self.sp.set_input_value("(//input[@type='text'])[4]",self.username)
        self.sp.set_input_value("(//input[@type='password'])[1]",self.password)
        if recipe_type == "material":
            self.sp.click_button("(//div)[201]")
        else:
            self.sp.click_button("(//div)[229]")
        self.sp.set_dropdown_value("(//div[@class='iaDropdownCommon_container iaDropdownCommon_placeholder-container ia_dropdown__placeholder'])[1]","Testing")
        self.sp.set_checkbox_click("//input[@id='checkbox-PE-sign.0:7:0']")
        if recipe_type == "material":
            self.sp.click_button("(//div)[221]")
        else:
            self.sp.click_button("(//div)[249]")
        time.sleep(5)
        #self.np = SuccessPage(self.driver)
        #self.np.set_submit("(//div)[136]")

        database_list_after = get_data("""select material_lot_id,balance_on_hand 
            from balance_summary 
            order BY material_lot_id desc""")
        
        query = """SELECT material_lot_id,extract_weigh
            FROM extraction_history
            WHERE batch_id = %s
            ORDER BY material_lot_id"""
        extract_record = get_data(query,(batch_id,))
        print(database_list_before)
        print(extract_record)
        print(database_list_after)

        #
        # Convert lists to dictionaries
        before_dict = self.op.list_to_dict(database_list_before)
        

        # Apply the extraction changes
        for id, value in extract_record:
            if id in before_dict:
                before_dict[id] -= value
            

        # Convert the modified before_dict back to a sorted list
        modified_before = self.op.dict_to_sorted_list(before_dict)
        print(modified_before)
        sorted_modified_before = sorted(modified_before)
        sorted_database_list_after = sorted(database_list_after)
        print(sorted_modified_before)
        print(sorted_database_list_after)
        # Assert if the modified before list equals the after list
        assert sorted_modified_before == sorted_database_list_after, "The before + extraction does not equal after"
        #

      
    def test_insert_batch_recipe_history(self):
        # check if batch_recipe_history table insert a record
        database_list = get_data("select batch_id, recipe_id,serving,planned_output,unit_id from batch_recipe_history order by created_on desc limit 1")
        print(database_list)
        batch_recipe_history_list = ReadData(self.check_batch_recipe_history)
        print(batch_recipe_history_list)
    
    def test_extraction_history(self):
        # check if extraction_history table insert records
        extraction_history_list = ReadData(self.check_extraction_history)
        print(extraction_history_list)
       

        batch_id = str(extraction_history_list[0][0])
        
        print(batch_id)
        query = """select batch_id,material_lot_id,extract_weigh,unit_id from extraction_history where batch_id = %s """
        database_list = get_data(query,(batch_id,))
        print(database_list)
        
        assert(database_list == extraction_history_list)

