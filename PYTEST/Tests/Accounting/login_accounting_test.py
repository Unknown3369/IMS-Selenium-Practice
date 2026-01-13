from selenium import webdriver
from PYTEST.pages.Accounting.Login_accounting import Login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_login_to_ims():
    driver = webdriver.Edge()
    login =Login(driver)
    login.perform_login("Saga", "Ims@1234")
    print("Login process completed.")

    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='Date']")))
    print("Dashboard page loaded successfully!")
    assert True