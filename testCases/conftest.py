import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pymysql
import sys
import os
from selenium.webdriver.chrome.service import Service

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utilities.connectDatabase import Mysql

@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()
    chrome_driver_version = "126.0.6478.62"
    service = Service(ChromeDriverManager(version = chrome_driver_version ).install())
    driver = webdriver.Chrome(service=service,options=options) 

    #driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    # driver = webdriver.Chrome(options=options)  # works
    return driver

@pytest.fixture()
def setup_database():
    conn_driver = Mysql()
    conn = conn_driver.get_conection()
    return conn
