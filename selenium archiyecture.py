from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Selenium Driver Setup
driver = webdriver.Chrome()  # Ensure you have installed the ChromeDriver

# Open the given URL
driver.get("https://www.saucedemo.com/")

# Login using provided credentials
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
login_button.click()

time.sleep(3)  # Wait for the page to load

# 1. Get the title of the webpage
page_title = driver.title
print(f"Page Title: {page_title}")

# 2. Get the current URL of the webpage
current_url = driver.current_url
print(f"Current URL: {current_url}")

# 3. Extract the entire page source and save it into a file
page_source = driver.page_source
with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(page_source)

print("Page source saved successfully!")

# Close the browser
driver.quit()
