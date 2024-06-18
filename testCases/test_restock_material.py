import pytest
import time

from pageObjects.LoginPage import LoginPage
from pageObjects.ReStockMaterialPage import ReStockMaterialPage
from pageObjects.SuccessPage import SuccessPage

from utilities.readProperties import ReadConfig
 
from Helpers.ReadExcel import ReadData
from Helpers.ReadDatabase import get_data

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_restock_material:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    restock_material_file = ReadConfig.getFilePath("restock_material_file")
    old_balance_on_hand = 0

    @pytest.mark.parametrize("material,lot_number,quantity",ReadData(restock_material_file))
    def test_restock_material_button(self,setup,material,lot_number,quantity):
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

        self.op = ReStockMaterialPage(self.driver)
        self.op.set_click("(//div[contains(text(),'Re-STOCK material')])[1]")
    
        WebDriverWait(self.driver,10).until(EC.url_contains("Inventory/re-stock-material"))
        print(self.driver.current_url)
        assert "Inventory/re-stock-material" in self.driver.current_url
        
        
        self.op.set_dropdown("(//div[@class='iaDropdownCommon_container iaDropdownCommon_placeholder-container ia_dropdown__placeholder'])[1]",material)
        time.sleep(3)
        self.op.set_dropdown("(//div[@class='iaDropdownCommon_container iaDropdownCommon_placeholder-container ia_dropdown__placeholder'])[1]",lot_number)
        # Set input values
        self.op.set_input_value("(//input[contains(@class,'ia_inputField ia-numeral-input popup-not-draggable')])[1]",str(quantity))
        
        query = """Select balance_on_hand from balance_summary join material_lot on material_lot_id = material_lot.id join material on material_id = material.id where lot_number = %s """ 
        database_list = get_data(query,(lot_number))
        print(database_list)
        self.old_balance_on_hand = database_list[0][0]
        print(self.old_balance_on_hand)

        # Click to save or proceed
        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div)[131]"))
        )
        self.op.set_click("(//div)[131]")
        time.sleep(3)


        # test if insert into database correctly
        # check if insert into stock_history table
        
        query = """Select material.name as material,lot_number, starting_balance as quantity 
        from stock_history 
        join material_lot on material_lot_id = material_lot.id 
        join material on material_id = material.id 
        where lot_number = %s 
        order by stock_history.id desc 
        limit 1""" 
        database_list = get_data(query,(lot_number,))
        elements = [material, lot_number,quantity]
        stock_history_list  = [tuple(elements)]
        assert database_list == stock_history_list
        

        # check if insert into stock_history table
        
        query = """Select material.name as material,lot_number, balance_on_hand as quantity from balance_summary join material_lot on material_lot_id = material_lot.id join material on material_id = material.id where lot_number = %s """ 
        database_list = get_data(query,(lot_number,))
        print(database_list)
        elements = [material, lot_number,quantity+ self.old_balance_on_hand]
        balance_summary_list  = [tuple(elements)]
        print(balance_summary_list)
        assert database_list == balance_summary_list


    '''
    @pytest.mark.parametrize("material,lot_number,quantity",ReadData(restock_material_file))
    def test_update_balance_summary(self,material,lot_number,quantity):
        # test if insert into database correctly
        # check if insert into stock_history table
        
        query = """Select material.name as material,lot_number, balance_on_hand as quantity from balance_summary join material_lot on material_lot_id = material_lot.id join material on material_id = material.id where lot_number = %s """ 
        database_list = get_data(query,(lot_number,))
        print(database_list)
        elements = [material, lot_number,quantity+ self.old_balance_on_hand]
        balance_summary_list  = [tuple(elements)]
        print(balance_summary_list)
        assert database_list == balance_summary_list
    '''