# Two simple test cases to verify:
#
# First successful login in to the given web page with valid credentials
# and in addition compatibility Testing for cross-browser testing.
#
# Second unsuccessful login in to the given web page with invalid credentials and combination.
#
# Usually it is recommended not to combine several scenarios in one test case 
# like we do at the successful case by verifying also the cross-browser testing.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Successful login in to the given web page with valid credentials
# and in addition compatibility Testing for cross-browser testing.
@pytest.mark.parametrize("webdriver_browser, input_username, input_password",
                         [
                             ('firefox', 'student', 'Password123'),
                             ('chrome', 'student', 'Password123')
                         ]
                         )
def test_successful_login(webdriver_browser, input_username, input_password):
    try:
        if webdriver_browser == "chrome":
            driver = webdriver.Chrome()
        elif webdriver_browser == "firefox":
            driver = webdriver.Firefox()

        # 1. Open the web application in a browser
        driver.get("https://practicetestautomation.com/practice-test-login")

        # 2. Enter valid credentials (username and password) and submit the login form
        username = driver.find_element(By.ID, "username")  # Replace with the correct element locator
        password = driver.find_element(By.ID, "password")  # Replace with the correct element locator

        username.send_keys(input_username)  # Replace with valid username
        password.send_keys(input_password)  # Replace with valid password

        login_button = driver.find_element(By.ID, "submit")  # Replace with the correct element locator
        login_button.click()

        # 3. Verify that the user is successfully logged in by checking for a specific element or page title
        # Example 1: Check for a specific element that appears only after login
        dashboard_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='loop-container']/div[*]//*[@class='post-title']"))  # Replace with the correct element locator
        )

        # Example 2: Check the page title
        WebDriverWait(driver, 10).until(EC.title_contains("Logged In Successfully"))  # Replace with the expected page title after login

        print("Login successful. Test passed.")

    except Exception as e:
        print(f"Test failed: {e}")

    finally:
        # Close the browser
        driver.quit()

# Unsuccessful login in to the given web page with invalid credentials and combination.
@pytest.mark.parametrize("webdriver_browser, input_username, input_password, error_txt",
                         [
                             ('chrome', 'student', 'wrong_password', 'Your password is invalid'),
                             ('chrome', 'wrong_student', 'Password123', 'Your username is invalid'),
                             ('chrome', '', '', 'Your username is invalid'),
                             ('chrome', 'student', '', 'Your password is invalid'),
                             ('chrome', '', 'Password123', 'Your username is invalid')
                         ]
                         )
def test_unsuccessful_login(webdriver_browser, input_username, input_password, error_txt):
    try:
        if webdriver_browser == "chrome":
            driver = webdriver.Chrome()
        elif webdriver_browser == "firefox":
            driver = webdriver.Firefox()

        # 1. Open the web application in a browser
        driver.get("https://practicetestautomation.com/practice-test-login")

        # 2. Enter invalid credentials (username and password) and submit the login form
        username = driver.find_element(By.ID, "username")  # Replace with the correct element locator
        password = driver.find_element(By.ID, "password")  # Replace with the correct element locator

        username.send_keys(input_username)  # Replace with invalid username
        password.send_keys(input_password)  # Replace with invalid password

        login_button = driver.find_element(By.ID, "submit")  # Replace with the correct element locator
        login_button.click()

        # 3. Verify that the user is unsuccessfully logged in by checking for a specific element or page title
        # Check for a specific element that appears only after unsuccessful login and the according error message
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, "error"), error_txt))

        print("Login unsuccessful (%s). Test passed." % (error_txt))

    except Exception as e:
        print(f"Test failed: {e}")

    finally:
        # Close the browser
        driver.quit()
