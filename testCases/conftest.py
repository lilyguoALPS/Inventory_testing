import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pymysql
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utilities.connectDatabase import Mysql

@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()
    #driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    driver = webdriver.Chrome(options=options)
    return driver

@pytest.fixture()
def setup_database():
    conn_driver = Mysql()
    conn = conn_driver.get_conection()
    return conn
