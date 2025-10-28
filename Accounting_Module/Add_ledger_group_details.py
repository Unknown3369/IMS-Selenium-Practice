from selenium import webdriver
from Add_Ledger_Group import MainPage
from Tests.login_test import login_to_ims  # Make sure this path matches your folder
import time

def ledger_details():
    # Step 1: Login and get driver
    driver = login_to_ims()

    # Step 2: Initialize MainPage with the logged-in driver
    Add_Ledger_Group = MainPage(driver)

    # Step 3: Navigate through the app
    Add_Ledger_Group.open_accounting_module()
    Add_Ledger_Group.open_ledger_group_master()

    # Step 4: Add new ledger
    Add_Ledger_Group.add_new_ledger_group("Automation Ledger Testing")

    # Step 5: Wait before closing
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    ledger_details()