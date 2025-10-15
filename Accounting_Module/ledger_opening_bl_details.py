from login_details import login_to_ims
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from ledger_opening_bl import MainPage
import time

def ledger_opening_bl_details():
    # Login and get driver
    driver = login_to_ims()
    # Initialize MainPage with the logged-in driver
    ledger_opening = MainPage(driver)
    # Navigate through the app
    ledger_opening.open_accounting_module()
    ledger_opening.open_ledger_opening_bl()
    # Add ledger opening details
    ledger_opening.add_ledger_opening_details("REF62201585", 250000, "Automation Test Ledger Opening")
    # Wait before closing
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    ledger_opening_bl_details()