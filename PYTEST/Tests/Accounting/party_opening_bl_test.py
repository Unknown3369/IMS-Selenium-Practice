from PYTEST.pages.Accounting.Login_accounting import Login
from PYTEST.pages.Accounting.party_opening_bl import MainPage
from selenium.webdriver.common.by import By
import time

def test_party_opening_bl_details(driver):
    # Login and get driver
    login = Login(driver)
    login.perform_login("Saga", "Ims@1234")
    # Initialize MainPage with the logged-in driver
    party_opening = MainPage(driver)
    # Navigate through the app
    party_opening.open_accounting_module()
    party_opening.open_party_opening_bl()
    # Add party opening details
    party_opening.add_party_opening_details("REF62201585", 250000, "Automation Test Party Opening")
    # Wait before closing
    assert True
