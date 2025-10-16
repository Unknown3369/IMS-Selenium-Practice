from selenium import webdriver
from Journal_Vouchers import MainPage
from login_details import login_to_ims
import time

def journal_voucher_details():
    # Step 1: Login and get driver
    driver = login_to_ims()

    # Step 2: Initialize MainPage with the logged-in driver
    journal_voucher = MainPage(driver)

    # Step 3: Navigate through the app
    journal_voucher.open_accounting_module()
    journal_voucher.open_journal_voucher()

    # Step 4: Add voucher details
    journal_voucher.add_voucher("REF26502858443", "Automation Test Voucher", 1000, 1000)

    # Step 5: Wait before closing
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    journal_voucher_details()