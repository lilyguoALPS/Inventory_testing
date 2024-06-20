from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .OPE_Parameters import path as path
import pyautogui
import time

""" Helper method returns single (first) element using Xpath on element

This element is found using the elements Xpath.s
Prints a fail satement if no element is found

@returns element
"""
def getXpath(driver:object, xpath:str):
    try:
        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))
    except:
        print("%s doesnt Exist" %xpath)
    return element

""" Helper Methods

These methods are used throught the program inorder to aid in the 
development and readibility of the testing suit. 

Developed by: Aidan Larock 
Date: 20/12/2022
"""

"""Funciton for changing the page in ingition to test funcitonality in other pages.

@param driver: selenium webdriver object
@param pageName: page name to transfer webdriver to
"""
def changePage(driver:object,pageName:str):
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '"+pageName+"')]"))).click()
    except:
        print("%s Page doesnt Exist" %pageName)

""" Helper method returns single (first) element using text on element

This element is found using the elements text.
Prints a fail satement if no element is found

@returns element
"""
def getText(driver:object, text:str):
    try:
        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '"+text+"')]")))
    except:
        print("%s doesnt Exist" %text)
    return element

""" Helper method returns single (first) element using id of element

This element is found using the elements id.
Prints a fail satement if no element is found

@returns element
"""
def getId(driver:object, id:str):
    try:
        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, id)))
    except:
        print("%s doesnt Exist" %id)
    return element

""" Helper method returns single (first) element using element class name

This element is found using the class name.
Prints a fail satement if no element is found

@returns element
"""
def getClass(driver:object, classN:str):
    try: 
        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, classN)))
    except:
        print("%s doesnt Exist" %classN)
    return element
def dropdown_by_xpath(driver:object, xpath:str,item:str):
    try:
        getXpath(driver,xpath).click()
        pyautogui.typewrite(item, interval=0.1)
        try:
            pyautogui.press('down') 
            pyautogui.press('enter')
            time.sleep(15)
            #pyautogui.moveTo(500,500)
            #pyautogui.click()
           
        except:
            print("Cannot Find Item in Dropdown")
    except:
        print("Cannot type in dropdown")

def dropdown(driver:object, id:str, item:str):
    try:
        getId(driver,id).click()
        pyautogui.typewrite(item, interval=0.1)
        try:
            pyautogui.press('down') 
            pyautogui.press('enter')
            time.sleep(15)
            pyautogui.moveTo(500,500)
            pyautogui.click()
           
        except:
            print("Cannot Find Item in Dropdown")
    except:
        print("Cannot type in dropdown")

""" Helper methods returns multiple elements using class name

These elements are found using the class name.
Prints a fail satement if no elements found

@returns elements
"""
def getClasses(driver:object, classN:str):
    try: 
        elements = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, classN)))
    except:
        print("%s doesnt Exist" %classN)
    return elements

""" setup the driver for Selenium.

@return driver.
"""
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=(path), options=options)
    return driver

""" Sign-in procedure for OPE and Ignition.

Signs in using the user's password and username from the
OPE_Parameters file.
"""
def signIn(driver:object, username, password):
    print(" -- Signing In -- ")
    changePage(driver,"Sign In")
    userIn = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'username')))
    userIn.send_keys(username)
    userIn.send_keys(Keys.ENTER)
    passIn = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'password')))
    passIn.send_keys(password)
    passIn.send_keys(Keys.ENTER)
