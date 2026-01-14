from PYTEST.pages.Accounting.Login_accounting import Login
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Accounting.ledger_opening_bl import MainPage
import time
import random

random_ref = random.randint(1000, 9999)
ref_number = f"REF-82/83={random_ref}"

random_amount = random.randint(100000, 500000)

def test_ledger_opening_bl_details(driver):
    login = Login(driver)
    login.perform_login("Saga", "Ims@1234")
    # Initialize MainPage with the logged-in driver
    ledger_opening = MainPage(driver)
    # Navigate through the app
    ledger_opening.open_accounting_module()
    ledger_opening.open_ledger_opening_bl()
    # Add ledger opening details
    ledger_opening.add_ledger_opening_details(ref_number, random_amount, "Automation Test Ledger Opening")
    # Wait before closing
    time.sleep(5)
    assert True