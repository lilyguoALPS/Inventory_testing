import pytest
import time

from pageObjects.LoginPage import LoginPage
from pageObjects.StockMaterialPage import StockMaterialPage
from pageObjects.SuccessPage import SuccessPage

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
    stock_material_file = ReadConfig.getFilePath("stock_material_file")

    @pytest.mark.parametrize("material,lot_number,supplier,quantity,unit,location,stock_date,best_before",ReadData(stock_material_file))
    def test_stock_material_button(self,setup,material,lot_number,supplier,quantity,unit,location,stock_date,best_before):
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

        self.op = StockMaterialPage(self.driver)
        self.op.set_click("(//div[contains(text(),'Stock Material')])[1]")
    
        WebDriverWait(self.driver,10).until(EC.url_contains("Inventory/stock-material"))
        print(self.driver.current_url)
        assert "Inventory/stock-material" in self.driver.current_url
        
        #self.op.set_timepicker_value("(//input[@placeholder='Select date'])[2]","2029-01-01")
        #time.sleep(5)
        
        # Interact with the first dropdown
        self.op.set_dropdown("(//div[contains(@class,'iaDropdownCommon_container iaDropdownCommon_placeholder-container ia_dropdown__placeholder')])[1]", material)
        # Set input values
        self.op.set_input_value("//input[@id='LtNmbrVl']", lot_number)
        self.op.set_input_value("(//input[@id='SplrVl'])[1]", supplier)
        self.op.set_input_value("(//input[contains(@type,'text')])[4]",str(quantity))

        self.op.set_dropdown("(//div[@class='iaDropdownCommon_container iaDropdownCommon_placeholder-container ia_dropdown__placeholder'])[1]", unit)
        self.op.set_dropdown("(//div[@class='iaDropdownCommon_container iaDropdownCommon_placeholder-container ia_dropdown__placeholder'])[1]",location)
        # it doesn't succeed in setting value for the timepicker, but because it has default value, it doesn't give error
        #self.op.set_timepicker_value("(//input[contains(@placeholder,'Select date')])[2]","2025-12-12 10:55pm")
        self.op.set_timepicker_value("(//input[@value='2025-06-11'])[1]","2025-12-12")
    
        
        time.sleep(10)
        
        # Click to save or proceed
        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div)[126]"))
        )
        self.op.set_click("(//div)[126]")
        time.sleep(3)

        # test if insert into database correctly
        # check if insert into material_lot table

        query = """SELECT material.NAME AS 'material',lot_number, supplier, room.location AS 'location' FROM material_lot JOIN room on room.id = room_id join material on material_id = material.id WHERE lot_number = %s"""
        database_list = get_data(query,(lot_number,))
        elements = [material,lot_number,supplier,location]
        material_lot_list = [tuple(elements)]
        assert database_list == material_lot_list

        # check if insert into stock_history table
        query = """Select lot_number, starting_balance,unit.name as unit from stock_history join material_lot on material_lot_id = material_lot.id join unit on unit.id = unit_id where lot_number = %s order by stock_history.id desc limit 1""" 
        database_list = get_data(query,(lot_number))
        elements = [lot_number,quantity,unit]
        stock_history_list  = [tuple(elements)]
        assert database_list == stock_history_list

        # check if insert into balance_summary table
        query = """select lot_number,balance_on_hand, unit.name as unit from balance_summary join unit on unit_id = unit.id join material_lot on material_lot_id = material_lot.id where lot_number = %s """
        database_list = get_data(query,(lot_number))
        elements = [lot_number, quantity, unit]
        balance_summary_list = [tuple(elements)]
        assert database_list == balance_summary_list
