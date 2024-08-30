from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace with the path to your WebDriver if not in PATH
driver = webdriver.Chrome()

try:
    # 1. Open the web application in a browser
    driver.get("https://practicetestautomation.com/practice-test-login")
    
    # 2. Enter valid credentials (username and password) and submit the login form
    username = driver.find_element(By.ID, "username")  # Replace with the correct element locator
    password = driver.find_element(By.ID, "password")  # Replace with the correct element locator
    
    username.send_keys("your_username")  # Replace with valid username
    password.send_keys("your_password")  # Replace with valid password
    
    login_button = driver.find_element(By.ID, "loginButton")  # Replace with the correct element locator
    login_button.click()
    
    # 3. Verify that the user is successfully logged in by checking for a specific element or page title
    # Example 1: Check for a specific element that appears only after login
    dashboard_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "dashboard"))  # Replace with the correct element locator
    )
    
    # Example 2: Check the page title
    WebDriverWait(driver, 10).until(EC.title_contains("Dashboard"))  # Replace with the expected page title after login
    
    print("Login successful. Test passed.")

except Exception as e:
    print(f"Test failed: {e}")

finally:
    # Close the browser
    driver.quit()
