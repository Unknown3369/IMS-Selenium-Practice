from selenium import webdriver
from Payment_Vouchers import MainPage
from login_details import login_to_ims
import time

def payment_voucher_details():
    # Login and get driver
    driver = login_to_ims()

    # Initialize MainPage with the logged-in driver
    payment_voucher = MainPage(driver)

    # Navigate through the app
    payment_voucher.open_accounting_module()
    payment_voucher.open_payment_voucher()

    # Add voucher details
    payment_voucher.add_voucher_details("REF678909384", "Automation Test Payment", "John Doe", 1500, "CHQ12344857756", "15-06-2025")

    # Wait before closing
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    payment_voucher_details()