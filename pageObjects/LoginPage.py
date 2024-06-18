from selenium.webdriver.common.by import By
class LoginPage:
    # Login Page
    button_sign_path =" //span[normalize-space()='Sign in']"
    textbox_username_path = "//input[@name='username']"
    button_login_path = "//span[@class='button-message']"
    textbox_password_path = "//input[@name='password']"
    
    #button_sign_path =" //div[@id='login']"
    def __init__(self,driver):
        self.driver=driver

    def clickSignIn(self):
        self.driver.find_element(By.XPATH, self.button_sign_path).click()
       
    def setUserName(self, username):
        self.driver.find_element(By.XPATH,self.textbox_username_path).clear()
        self.driver.find_element(By.XPATH,self.textbox_username_path).send_keys(username)

    def clickContinue(self):
       self.driver.find_element(By.XPATH,self.button_login_path).click()

    def setPassword(self, password):
        self.driver.find_element(By.XPATH,self.textbox_password_path).clear()
        self.driver.find_element(By.XPATH,self.textbox_password_path).send_keys(password)


    

    