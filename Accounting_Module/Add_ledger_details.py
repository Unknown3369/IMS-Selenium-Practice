from selenium import webdriver
from Add_ledger import MainPage
from login_details import login_to_ims  # Make sure this path matches your folder
import time

def ledger_details():
    # Step 1: Login and get driver
    driver = login_to_ims()

    # Step 2: Initialize MainPage with the logged-in driver
    Add_ledger = MainPage(driver)

    # Step 3: Navigate through the app
    Add_ledger.open_accounting_module()
    Add_ledger.open_ledger_group_master()

    # Step 4: Add new ledger
    Add_ledger.add_new_ledger("Automation Ledger")

    # Step 5: Wait before closing
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    ledger_details()