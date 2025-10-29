import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PYTEST.pages.Login import login


@allure.title("Login to IMS Application")
@allure.description("This test logs into the IMS application using valid credentials and verifies the dashboard.")
def test_login_to_ims(driver):
   """Login test using pytest fixture for driver"""
   login_page = login(driver)
   login_page.perform_login("Testuser", "Test@1234")
   print("Login process completed.")
   wait = WebDriverWait(driver, 30)
   wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='Date']")))
   print("Dashboard page loaded successfully!")
   assert driver.find_element(By.XPATH, "//input[@id='Date']"), "Date input not found"
