from selenium import webdriver
from Payment_Vouchers import MainPage
from login_details import login_to_ims
from datetime import datetime
import random
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
    def generate_random_refno():
        date_part = datetime.now().strftime("%y%m%d")  # e.g. 251019
        random_part = random.randint(100, 999)
        return f"JV{date_part}{random_part}"
    
    def generate_rendom_chequeno():
        random_num = random.randint(1000,9999)
        return f"{random_num}"
    
    def generate_random_amount():
        random_num = random.randfloat(1000.00,99999.99)
        return f"{random_num}"
    
    payment_voucher.add_voucher_details(generate_random_refno(), "Test Payment", "John Doe", generate_random_amount(), generate_rendom_chequeno())

    payment_voucher.save_voucher()
    # Wait before closing
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    payment_voucher_details()