from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class insta:
    url="https://www.instagram.com/guviofficial/"
    username ="guviofficial"
class username:
    def __init__(self):
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def validation(self):
        self.driver.find_element(by=By.XPATH,value="//*[@id="mount_0_0_M/"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section/div[1]/div/h2")
    def number_of_followers(self):
        self.driver.find_element(by=By.XPATH,value="//*[@id="mount_0_0_M/"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/div[3]/ul/li[2]/div/button/span")
    def number_of_followings(self):
        self.driver.find_element(by=By.XPATH,value="//*[@id="mount_0_0_M/"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/div[3]/ul/li[3]/div/button/span")

