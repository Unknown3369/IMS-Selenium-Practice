# import pytest
# import allure
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By  
# from CICD_Compatible.Pages.login import login   

# @allure.title("Login to IMS Application")
# @allure.description("This test logs into the IMS application using valid credentials and verifies the dashboard.")
# def test_login_to_ims(driver):   
#    """Login test using pytest fixture for driver"""
#    login_page = login(driver)
#    login_page.perform_login("Saga", "Ims@1234")
#    print("Login process completed.")
#    wait = WebDriverWait(driver, 30)
#    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='Date']")))
#    print("Dashboard page loaded successfully!")
#    assert driver.find_element(By.XPATH, "//input[@id='Date']"), "Date input not found"


   
from pymsgbox import alert
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from CICD_Compatible.Pages.login import login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from CICD_Compatible.conftest import driver

@allure.title("Login to IMS Application")
@allure.description("This test logs into the IMS application using valid credentials")

# TC-LOGIN-001
# Successful login with valid credentials
def test_valid_login(driver: webdriver):

   """Login test using pytest valid creds"""

   login_page = login(driver)

   login_page.perform_login("Testuser", "Test@1234")

   assert login_page.verify_login_success()

# TC-LOGIN-002
# Invalid password

def test_invalid_password(driver: webdriver):

   """Login test using pytest invalid creds"""

   login_page = login(driver)

   login_page.perform_login("Testuser", "wrongpass")

   assert "invalid" in login_page.get_error_message().lower()

# TC-LOGIN-003
# Empty username and password

def test_empty_login(driver: webdriver):

   """Login test with empty credentials"""

   login_page = login(driver)

   login_page.open_login_page()
   login_page.click_login()

   assert not login_page.verify_login_success()

# TC-LOGIN-004
# Non-existent username

def test_non_existent_user(driver: webdriver):

   """Login test with non-existent username"""

   login_page = login(driver)
   login_page.perform_login("ghost_user_9999", "Test@1234")
   assert "invalid" in login_page.get_error_message().lower()

# TC-LOGIN-005
# Password masking validation

def test_password_masking(driver: webdriver):

   """Verify password field is masked"""

   login_page = login(driver)
   login_page.open_login_page()
   assert login_page.get_password_field_type() == "password"

# TC-LOGIN-006
# Account lock after multiple attempts

def test_account_lock(driver):

   """Verify account lockout after multiple failed login attempts"""

   login_page = login(driver)
   login_page.open_login_page()

   for _ in range(6):  # exceed threshold
      login_page.perform_login("AccountLock", "wrongpass")
      if login_page.is_account_locked():
         break

      login_page.invalid_login()

   assert login_page.is_account_locked()

# TC-LOGIN-007
# SQL Injection validation

def test_sql_injection(driver: webdriver):

   """Verify login is secure against SQL injection"""

   login_page = login(driver)
   sql_payload = "' OR '1'='1"
   login_page.perform_login(sql_payload, sql_payload)
   assert not login_page.verify_login_success()

# TC-LOGIN-008
# Logout validation

def test_logout(driver: webdriver):

   """Verify user can logout successfully"""

   login_page = login(driver)
   login_page.perform_login("Testuser", "Test@1234")
   assert login_page.verify_login_success()
   login_page.logout()
   WebDriverWait(driver, 10).until(EC.alert_is_present())
   alert = driver.switch_to.alert
   alert.accept()
   assert "login" in driver.current_url.lower()
