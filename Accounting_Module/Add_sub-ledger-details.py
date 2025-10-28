from selenium import webdriver
from Add_Sub_Ledger import MainPage
from login_details import login_to_ims
import time

def sub_ledger_details():
    # Step 1: Login and get driver
    driver = login_to_ims()

    # Step 2: Initialize MainPage with the logged-in driver
    Add_sub_ledger = MainPage(driver)

    # Step 3: Navigate through the app
    Add_sub_ledger.open_accounting_module()
    Add_sub_ledger.open_sub_ledger_account_master()

    # Step 4: Add new sub ledger
    Add_sub_ledger.add_new_sub_ledger("Automation Sub Ledger", "ABCDE1234F")

    # Step 5: Wait before closing
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    sub_ledger_details()