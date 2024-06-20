import configparser
import os

# Get the current directory of the script
curr_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the configuration file
config_path = os.path.join(curr_dir, '..', 'Configurations', 'config.ini')

# Create a ConfigParser object
config = configparser.RawConfigParser()

# Read the configuration file
config.read(config_path)

#config.read("C:\\Users\\LilyGuo\\OneDrive - ALPS Inc\\Lily_workspace\\02_Development\\Inventory-Testing-V2\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info','useremail')
        return username

    @staticmethod
    def getUsername():
        username=config.get('common info','username')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password

    @staticmethod
    def getOperator():
        operator=config.get('common info','operator')
        return operator

    @staticmethod
    def getOperatorPassword():
        operator_password=config.get('common info','operator_password')
        return operator_password
    
    @staticmethod
    def getFilePath(file_name):
        file_path=config.get('common info',file_name)
        return file_path
