
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

def perform_drag_and_drop():
    # Set up the WebDriver (Make sure the appropriate WebDriver is installed, e.g., chromedriver)
    driver = webdriver.Chrome()
    
    try:
        # Open the given URL
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        
        # Switch to the iframe containing the drag-and-drop elements
        iframe = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
        driver.switch_to.frame(iframe)
        
        # Locate the draggable and droppable elements
        draggable = driver.find_element(By.ID, "draggable")
        droppable = driver.find_element(By.ID, "droppable")
        
        # Perform drag and drop using ActionChains
        actions = ActionChains(driver)
        actions.drag_and_drop(draggable, droppable).perform()
        
        # Wait to observe the result
        time.sleep(3)
        
        print("Drag and drop operation performed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()

# Call the function to execute the task
if _name_ == "_main_":
    perform_drag_and_drop()